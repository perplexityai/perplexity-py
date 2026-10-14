from __future__ import annotations

import json

import httpx
import pytest

import perplexity.generated.api as generated
from perplexity import Stream, Perplexity, AsyncStream, AsyncPerplexity
from perplexity.types import (
    Model,
    DecisionAnswer,
    DecisionQuestion,
    ModelListResponse,
    DecisionCreateParams,
    SearchCreateResponse,
    DecisionCreateResponse,
)
from perplexity.generated.api import (
    ApiSearchPageOutput,
    SearchCreateResponse as GeneratedSearchCreateResponse,
)


def test_client_uses_generated_api_and_model() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(
            200,
            json={
                "id": "search-1",
                "results": [
                    {
                        "snippet": "An answer engine.",
                        "title": "Perplexity",
                        "url": "https://www.perplexity.ai",
                    }
                ],
            },
            request=request,
        )

    with Perplexity(
        api_key="test",
        base_url="https://example.test",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    ) as client:
        response = client.search.create(query="perplexity")

    assert SearchCreateResponse is GeneratedSearchCreateResponse
    assert isinstance(response, GeneratedSearchCreateResponse)
    assert isinstance(response.results[0], ApiSearchPageOutput)
    assert response.results[0].title == "Perplexity"
    assert requests[0].url == "https://example.test/search"
    assert json.loads(requests[0].content) == {"query": "perplexity"}


def test_responses_cache_controls_and_tool_usage() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(
            200,
            json={
                "id": "resp-1",
                "object": "response",
                "created_at": 0,
                "model": "openai/gpt-5.4",
                "status": "completed",
                "output": [],
                "service_tier": "priority",
                "prompt_cache_key": "doc-1",
                "usage": {
                    "input_tokens": 10,
                    "output_tokens": 2,
                    "total_tokens": 12,
                    "tool_calls_details": {
                        "fetch_url": {
                            "invocation": 1,
                            "cost_usd": 0.0025,
                            "token_usage": [
                                {
                                    "model": "extractor",
                                    "input_tokens": 100,
                                    "input_tokens_details": {"cached_tokens": 40, "cache_read_input_tokens": 40},
                                    "output_tokens": 20,
                                    "output_tokens_details": {"reasoning_tokens": 5},
                                }
                            ],
                        }
                    },
                },
            },
            request=request,
        )

    with Perplexity(
        api_key="test",
        base_url="https://example.test",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    ) as client:
        response = client.responses.create(
            input=[{"role": "user", "content": "Summarize the file."}],
            service_tier="priority",
            prompt_cache_key="doc-1",
        )

    assert json.loads(requests[0].content) == {
        "input": [{"role": "user", "content": "Summarize the file."}],
        "service_tier": "priority",
        "prompt_cache_key": "doc-1",
    }
    assert response.service_tier == "priority"
    assert response.prompt_cache_key == "doc-1"
    assert response.usage is not None
    assert response.usage.tool_calls_details is not None
    details = response.usage.tool_calls_details["fetch_url"]
    assert details.cost_usd == 0.0025
    assert details.token_usage is not None
    usage = details.token_usage[0]
    assert usage.input_tokens_details.cached_tokens == 40
    assert usage.input_tokens_details.cache_read_input_tokens == 40
    assert usage.output_tokens_details.reasoning_tokens == 5


def model_catalog_handler(request: httpx.Request) -> httpx.Response:
    assert request.method == "GET"
    assert request.url == "https://example.test/v1/models"
    assert request.headers["authorization"] == "Bearer test"
    assert not request.content
    return httpx.Response(
        200,
        json={
            "object": "list",
            "data": [{"id": "provider/model", "object": "model", "created": 0, "owned_by": "provider"}],
        },
    )


def test_model_catalog() -> None:
    with Perplexity(
        api_key="test",
        base_url="https://example.test",
        http_client=httpx.Client(transport=httpx.MockTransport(model_catalog_handler)),
    ) as client:
        response = client.models.list()
        assert isinstance(response, ModelListResponse)
        assert isinstance(response.data[0], Model)
        assert response.object == "list"
        assert response.data[0].id == "provider/model"
        assert client.models.with_raw_response.list().parse().data[0].created == 0
        with client.models.with_streaming_response.list() as raw:
            assert raw.parse().data[0].owned_by == "provider"


async def test_async_model_catalog() -> None:
    async with AsyncPerplexity(
        api_key="test",
        base_url="https://example.test",
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(model_catalog_handler)),
    ) as client:
        response = await client.models.list()
        assert response.data[0].id == "provider/model"
        raw = await client.models.with_raw_response.list()
        assert (await raw.parse()).data[0].created == 0
        async with client.models.with_streaming_response.list() as streamed:
            assert (await streamed.parse()).data[0].owned_by == "provider"


DECISION_REQUEST = {
    "model": "pplx-decider-v1.1-27b",
    "state": {"review": "The battery stopped charging."},
    "questions": {
        "defect": {"type": "noul", "criteria": {"true": "Broken", "false": None}},
        "sentiment": {"type": "choice", "criteria": {"positive": None, "negative": "Dissatisfied"}},
        "severity": {"type": "score", "criteria": ["Cosmetic", {"description": "Unusable"}]},
    },
}
DECISION_RESPONSE = {
    "model": "pplx-decider-v1.1-27b",
    "answers": {
        "defect": {"type": "noul", "noul": 0.95},
        "sentiment": {
            "type": "choice",
            "choice": "negative",
            "confidence": 0.9,
            "probabilities": {"positive": 0.1, "negative": 0.9},
        },
        "severity": {
            "type": "score",
            "score": 0.9,
            "confidence": 0.9,
            "legend": {"0": "Cosmetic", "1": {"description": "Unusable"}},
            "probabilities": {"0": 0.1, "1": 0.9},
        },
    },
    "usage": {"input_tokens": 100, "output_tokens": 3},
}


def decision_handler(request: httpx.Request) -> httpx.Response:
    assert request.method == "POST"
    assert request.url == "https://example.test/v1/decisions"
    assert request.headers["authorization"] == "Bearer test"
    assert json.loads(request.content) == DECISION_REQUEST
    return httpx.Response(200, json=DECISION_RESPONSE)


def test_decisions() -> None:
    assert DecisionAnswer is generated.DecisionAnswer
    assert DecisionQuestion is generated.DecisionQuestion
    assert DecisionCreateParams is generated.DecisionCreateParams
    with Perplexity(
        api_key="test",
        base_url="https://example.test",
        http_client=httpx.Client(transport=httpx.MockTransport(decision_handler)),
    ) as client:
        response = client.decisions.create(**DECISION_REQUEST)
        assert isinstance(response, DecisionCreateResponse)
        assert response.answers["defect"].noul == 0.95
        assert response.answers["sentiment"].choice == "negative"
        assert response.answers["severity"].score == 0.9
        assert response.usage.output_tokens == 3
        raw = client.decisions.with_raw_response.create(**DECISION_REQUEST)
        assert raw.parse().to_dict(mode="json") == DECISION_RESPONSE


async def test_async_decisions() -> None:
    async with AsyncPerplexity(
        api_key="test",
        base_url="https://example.test",
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(decision_handler)),
    ) as client:
        response = await client.decisions.create(**DECISION_REQUEST)
        assert response.answers["defect"].noul == 0.95
        assert response.answers["sentiment"].choice == "negative"
        assert response.answers["severity"].score == 0.9
        assert response.usage.output_tokens == 3
        async with client.decisions.with_streaming_response.create(**DECISION_REQUEST) as raw:
            assert (await raw.parse()).to_dict(mode="json") == DECISION_RESPONSE


RESUMED_EVENT = {
    "type": "response.output_text.delta",
    "sequence_number": 4,
    "item_id": "msg-1",
    "output_index": 0,
    "content_index": 0,
    "delta": "resumed",
}


def response_reconnect_handler(request: httpx.Request) -> httpx.Response:
    assert request.method == "GET"
    assert request.url.path == "/v1/responses/resp-1"
    assert dict(request.url.params) == {"starting_after": "3", "stream": "true"}
    return httpx.Response(
        200,
        headers={"content-type": "text/event-stream"},
        content=f"data: {json.dumps(RESUMED_EVENT)}\n\n".encode(),
    )


def test_response_stream_reconnection() -> None:
    with Perplexity(
        api_key="test",
        base_url="https://example.test",
        http_client=httpx.Client(transport=httpx.MockTransport(response_reconnect_handler)),
    ) as client:
        stream = client.responses.retrieve("resp-1", stream=True, starting_after=3)
        assert isinstance(stream, Stream)
        events = list(stream)
    assert [event.to_dict(mode="json") for event in events] == [RESUMED_EVENT]


async def test_async_response_stream_reconnection() -> None:
    async with AsyncPerplexity(
        api_key="test",
        base_url="https://example.test",
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(response_reconnect_handler)),
    ) as client:
        stream = await client.responses.retrieve("resp-1", stream=True, starting_after=3)
        assert isinstance(stream, AsyncStream)
        events = [event async for event in stream]
    assert [event.to_dict(mode="json") for event in events] == [RESUMED_EVENT]


def test_response_stream_reconnection_requires_cursor_and_ignores_extra_query_stream() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert dict(request.url.params) == {"starting_after": "3", "stream": "false"}
        return httpx.Response(
            200,
            json={
                "id": "resp-1",
                "object": "response",
                "created_at": 0,
                "model": "openai/gpt-5.4",
                "status": "completed",
                "output": [],
            },
        )

    with Perplexity(
        api_key="test",
        base_url="https://example.test",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    ) as client:
        with pytest.raises(TypeError, match="stream=True requires starting_after"):
            client.responses.retrieve("resp-1", stream=True)
        response = client.responses.retrieve("resp-1", stream=False, starting_after=3, extra_query={"stream": True})
        assert not isinstance(response, Stream)


def plain_response_handler(request: httpx.Request) -> httpx.Response:
    assert dict(request.url.params) == {"starting_after": "3"}
    return httpx.Response(
        200,
        json={
            "id": "resp-1",
            "object": "response",
            "created_at": 0,
            "model": "openai/gpt-5.4",
            "status": "completed",
            "output": [],
        },
    )


def test_response_retrieve_strips_stream_from_extra_query() -> None:
    with Perplexity(
        api_key="test",
        base_url="https://example.test",
        http_client=httpx.Client(transport=httpx.MockTransport(plain_response_handler)),
    ) as client:
        response = client.responses.retrieve("resp-1", starting_after=3, extra_query={"stream": True})
        assert not isinstance(response, Stream)


async def test_async_response_stream_reconnection_requires_cursor_and_strips_extra_query_stream() -> None:
    async with AsyncPerplexity(
        api_key="test",
        base_url="https://example.test",
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(plain_response_handler)),
    ) as client:
        with pytest.raises(TypeError, match="stream=True requires starting_after"):
            await client.responses.retrieve("resp-1", stream=True)
        response = await client.responses.retrieve("resp-1", starting_after=3, extra_query={"stream": True})
        assert not isinstance(response, AsyncStream)


def test_response_retrieve_rejects_non_bool_stream() -> None:
    with Perplexity(
        api_key="test",
        base_url="https://example.test",
        http_client=httpx.Client(transport=httpx.MockTransport(plain_response_handler)),
    ) as client:
        with pytest.raises(TypeError, match="stream must be a bool"):
            client.responses.retrieve("resp-1", stream="true", starting_after=3)  # type: ignore[call-overload]
