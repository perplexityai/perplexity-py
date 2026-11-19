from __future__ import annotations

import json
from typing import Any, Callable

import httpx
import pytest
from pydantic import ValidationError

from perplexity import Perplexity, AsyncPerplexity
from perplexity.types import EmbeddingObject, EmbeddingCreateResponse

USAGE = {"prompt_tokens": 5, "total_tokens": 5}
IMAGE = {"type": "image", "image": "data:image/png;base64,AAAA"}


def dense_response(model: str, count: int = 1) -> dict[str, Any]:
    return {
        "object": "list",
        "model": model,
        "data": [{"object": "embedding", "index": index, "embedding": "AAE="} for index in range(count)],
        "usage": USAGE,
    }


def chunked_response(model: str, chunks: list[int]) -> dict[str, Any]:
    return {
        "object": "list",
        "model": model,
        "data": [
            {
                "object": "list",
                "index": document,
                "data": [{"object": "embedding", "index": chunk, "embedding": "AgM="} for chunk in range(count)],
            }
            for document, count in enumerate(chunks)
        ],
        "usage": USAGE,
    }


def mock_client(body: dict[str, Any], requests: list[httpx.Request]) -> Perplexity:
    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json=body, request=request)

    return Perplexity(
        api_key="test",
        base_url="https://example.test",
        max_retries=0,
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )


def sent(requests: list[httpx.Request]) -> Any:
    assert len(requests) == 1
    assert requests[0].method == "POST"
    assert requests[0].url == "https://example.test/v1/embeddings"
    return json.loads(requests[0].content)


@pytest.mark.parametrize("model", ["pplx-embed-v1-0.6b", "pplx-embed-v1-4b"])
def test_v1_request_is_unchanged(model: Any) -> None:
    requests: list[httpx.Request] = []
    with mock_client(dense_response(model, 2), requests) as client:
        response = client.embeddings.create(
            model=model,
            input=["first", "second"],
            dimensions=128,
            encoding_format="base64_binary",
        )

    assert sent(requests) == {
        "model": model,
        "input": ["first", "second"],
        "dimensions": 128,
        "encoding_format": "base64_binary",
    }
    assert isinstance(response, EmbeddingCreateResponse)
    assert response.data is not None
    assert [item.index for item in response.data] == [0, 1]
    assert all(item.embedding == "AAE=" for item in response.data)


def test_v1_single_string_input() -> None:
    requests: list[httpx.Request] = []
    with mock_client(dense_response("pplx-embed-v1-0.6b"), requests) as client:
        client.embeddings.create(model="pplx-embed-v1-0.6b", input="Perplexity answers questions.")

    assert sent(requests) == {"model": "pplx-embed-v1-0.6b", "input": "Perplexity answers questions."}


@pytest.mark.parametrize("model", ["pplx-embed-v2-context-9b", "pplx-embed-v2-context-0.6b"])
def test_v2_query(model: Any) -> None:
    requests: list[httpx.Request] = []
    with mock_client(dense_response(model), requests) as client:
        response = client.embeddings.create(
            model=model,
            input_type="query",
            input=["What is late interaction retrieval?"],
            dimensions=1024,
        )

    assert sent(requests) == {
        "model": model,
        "input_type": "query",
        "input": ["What is late interaction retrieval?"],
        "dimensions": 1024,
    }
    assert response.model == model
    assert response.data is not None
    assert response.data[0].embedding == "AAE="
    assert response.data[0].data is None


@pytest.mark.parametrize("model", ["pplx-embed-v2-context-9b", "pplx-embed-v2-context-0.6b"])
def test_v2_whole_documents_return_one_embedding_per_document(model: Any) -> None:
    requests: list[httpx.Request] = []
    with mock_client(dense_response(model, 2), requests) as client:
        response = client.embeddings.create(
            model=model,
            input_type="document",
            input=["First document.", "Second document."],
        )

    assert sent(requests) == {
        "model": model,
        "input_type": "document",
        "input": ["First document.", "Second document."],
    }
    assert response.data is not None
    assert [(item.index, item.embedding, item.data) for item in response.data] == [(0, "AAE=", None), (1, "AAE=", None)]


def test_v2_image_without_num_chunks_returns_one_embedding_per_image() -> None:
    requests: list[httpx.Request] = []
    with mock_client(dense_response("pplx-embed-v2-context-0.6b"), requests) as client:
        response = client.embeddings.create(
            model="pplx-embed-v2-context-0.6b",
            input_type="document",
            input=[IMAGE],
        )

    assert sent(requests) == {"model": "pplx-embed-v2-context-0.6b", "input_type": "document", "input": [IMAGE]}
    assert response.data is not None
    assert response.data[0].embedding == "AAE="


@pytest.mark.parametrize("model", ["pplx-embed-v2-context-9b", "pplx-embed-v2-context-0.6b"])
def test_v2_chunked_documents_return_one_embedding_per_chunk(model: Any) -> None:
    requests: list[httpx.Request] = []
    with mock_client(chunked_response(model, [2, 1]), requests) as client:
        response = client.embeddings.create(
            model=model,
            input_type="document",
            input=[["First chunk.", "Second chunk."], ["Another document."]],
        )

    assert sent(requests) == {
        "model": model,
        "input_type": "document",
        "input": [["First chunk.", "Second chunk."], ["Another document."]],
    }
    assert response.data is not None
    assert [document.index for document in response.data] == [0, 1]
    assert [len(document.data or []) for document in response.data] == [2, 1]
    first = response.data[0].data
    assert first is not None
    assert isinstance(first[1], EmbeddingObject)
    assert (first[1].index, first[1].embedding) == (1, "AgM=")


def test_v2_image_documents_with_num_chunks() -> None:
    requests: list[httpx.Request] = []
    with mock_client(chunked_response("pplx-embed-v2-context-9b", [4]), requests) as client:
        response = client.embeddings.create(
            model="pplx-embed-v2-context-9b",
            input_type="document",
            input=[IMAGE],
            num_chunks=4,
            encoding_format="base64_binary",
        )

    assert sent(requests) == {
        "model": "pplx-embed-v2-context-9b",
        "input_type": "document",
        "input": [IMAGE],
        "num_chunks": 4,
        "encoding_format": "base64_binary",
    }
    assert response.data is not None
    assert len(response.data[0].data or []) == 4


@pytest.mark.parametrize(
    "create",
    [
        lambda client: client.embeddings.create(model="pplx-embed-v3", input="x"),
        lambda client: client.embeddings.create(model="pplx-embed-v2-context-9b", input="x", input_type="passage"),
        lambda client: client.embeddings.create(model="pplx-embed-v2-context-9b", input="x", num_chunks=3),
    ],
    ids=["unknown-model", "unknown-input-type", "unsupported-num-chunks"],
)
def test_invalid_parameters_fail_before_sending(create: Callable[[Any], object]) -> None:
    requests: list[httpx.Request] = []
    with mock_client(dense_response("unused"), requests) as client, pytest.raises(ValidationError):
        create(client)

    assert requests == []


async def test_async_v2_chunked_documents() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json=chunked_response("pplx-embed-v2-context-0.6b", [2]), request=request)

    async with AsyncPerplexity(
        api_key="test",
        base_url="https://example.test",
        max_retries=0,
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
    ) as client:
        response = await client.embeddings.create(
            model="pplx-embed-v2-context-0.6b",
            input_type="document",
            input=[["First chunk.", "Second chunk."]],
        )

    assert sent(requests)["input"] == [["First chunk.", "Second chunk."]]
    assert response.data is not None
    assert len(response.data[0].data or []) == 2


def test_contextualized_embeddings_v1_is_unchanged() -> None:
    requests: list[httpx.Request] = []
    body = {
        "object": "list",
        "model": "pplx-embed-context-v1-0.6b",
        "data": [{"object": "list", "index": 0, "data": [{"object": "embedding", "index": 0, "embedding": "AAE="}]}],
        "usage": USAGE,
    }
    with mock_client(body, requests) as client:
        response = client.contextualized_embeddings.create(
            model="pplx-embed-context-v1-0.6b",
            input=[["Perplexity answers questions."]],
        )

    assert requests[0].url == "https://example.test/v1/contextualizedembeddings"
    assert json.loads(requests[0].content) == {
        "model": "pplx-embed-context-v1-0.6b",
        "input": [["Perplexity answers questions."]],
    }
    assert response.data is not None
    assert response.data[0].data is not None
    assert response.data[0].data[0].embedding == "AAE="
