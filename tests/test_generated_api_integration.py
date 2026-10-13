from __future__ import annotations

import json

import httpx

from perplexity import Perplexity, AsyncPerplexity
from perplexity.types import Model, ModelListResponse, SearchCreateResponse
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
