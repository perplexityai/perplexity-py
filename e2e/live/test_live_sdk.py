from __future__ import annotations

import os
import time
import asyncio
from collections.abc import Iterator

import pytest

from perplexity import Perplexity, AsyncPerplexity


def api_key() -> str:
    value = os.environ.get("PPLX_API_TOKEN")
    if not value:
        pytest.fail("PPLX_API_TOKEN must be set")
    return value


@pytest.fixture(scope="module")
def client() -> Iterator[Perplexity]:
    with Perplexity(api_key=api_key(), max_retries=0) as perplexity:
        yield perplexity


def test_chat_completion() -> None:
    async def run() -> None:
        async with AsyncPerplexity(api_key=api_key(), max_retries=0) as async_client:
            completion = await async_client.chat.completions.create(
                max_tokens=16,
                messages=[{"content": "Reply with only the word pong.", "role": "user"}],
                model="sonar",
                temperature=0,
            )

        assert completion.id
        assert completion.model
        assert completion.choices
        assert completion.choices[0].index == 0
        assert completion.choices[0].message.role == "assistant"
        assert isinstance(completion.choices[0].message.content, str)

    asyncio.run(run())


def test_search(client: Perplexity) -> None:
    search = client.search.create(max_results=1, query="Perplexity AI")

    assert search.id
    assert search.results
    assert search.results[0].title
    assert search.results[0].url
    assert search.results[0].snippet


def test_embeddings(client: Perplexity) -> None:
    embeddings = client.embeddings.create(
        dimensions=128,
        input="Perplexity answers questions.",
        model="pplx-embed-v1-0.6b",
    )

    assert embeddings.model
    assert embeddings.data
    assert embeddings.data[0].index == 0
    assert embeddings.data[0].embedding


def test_contextualized_embeddings(client: Perplexity) -> None:
    embeddings = client.contextualized_embeddings.create(
        dimensions=128,
        input=[["Perplexity answers questions.", "Its answers include citations."]],
        model="pplx-embed-context-v1-0.6b",
    )

    assert embeddings.model
    assert embeddings.data
    assert embeddings.data[0].data
    assert embeddings.data[0].data[0].embedding


def test_responses(client: Perplexity) -> None:
    response = client.responses.create(
        input="Reply with only the word pong.",
        max_output_tokens=16,
        preset="pro-search",
    )

    assert response.id
    assert response.object == "response"
    assert response.output
    assert response.status == "completed"


def test_streaming_chat(client: Perplexity) -> None:
    stream = client.chat.completions.create(
        max_tokens=16,
        messages=[{"content": "Reply with only the word pong.", "role": "user"}],
        model="sonar",
        stream=True,
        temperature=0,
    )
    chunks = list(stream)

    assert chunks
    chunk = next(item for item in chunks if item.choices)
    assert chunk.choices[0].index == 0
    assert chunk.choices[0].delta is not None


def test_streaming_responses(client: Perplexity) -> None:
    stream = client.responses.create(
        input="Reply with only the word pong.",
        max_output_tokens=16,
        preset="pro-search",
        stream=True,
    )
    event_types = {event.type for event in stream}

    assert "response.created" in event_types
    assert "response.completed" in event_types
    assert "response.output_text.delta" in event_types


def test_async_chat_completion(client: Perplexity) -> None:
    completion = client.async_.chat.completions.create(
        request={
            "max_tokens": 16,
            "messages": [{"content": "Reply with only the word pong.", "role": "user"}],
            "model": "sonar-deep-research",
        }
    )

    for _ in range(120):
        assert completion.status != "FAILED", completion.error_message
        if completion.status == "COMPLETED":
            break
        time.sleep(1)
        completion = client.async_.chat.completions.get(completion.id)
    else:
        pytest.fail(f"Async completion {completion.id} did not finish")

    assert completion.id
    assert completion.created_at
    assert completion.model
    assert completion.response
