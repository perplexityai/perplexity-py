from __future__ import annotations

from e2e.live.helpers import create_client


def test_embeddings() -> None:
    with create_client() as client:
        embeddings = client.embeddings.create(
            dimensions=128,
            input="Perplexity answers questions.",
            model="pplx-embed-v1-0.6b",
        )

    assert embeddings.model
    assert embeddings.data
    assert embeddings.data[0].index == 0
    assert embeddings.data[0].embedding


def test_embeddings_v2_query() -> None:
    with create_client() as client:
        embeddings = client.embeddings.create(
            input=["What does Perplexity do?"],
            input_type="query",
            model="pplx-embed-v2-context-0.6b",
        )

    assert embeddings.model
    assert embeddings.data
    assert embeddings.data[0].index == 0
    assert embeddings.data[0].embedding


def test_embeddings_v2_document() -> None:
    with create_client() as client:
        embeddings = client.embeddings.create(
            input=[["Perplexity answers questions.", "Its answers include citations."]],
            input_type="document",
            model="pplx-embed-v2-context-0.6b",
        )

    assert embeddings.model
    assert embeddings.data
    chunks = embeddings.data[0].data
    assert chunks
    assert [chunk.index for chunk in chunks] == [0, 1]
    assert all(chunk.embedding for chunk in chunks)
