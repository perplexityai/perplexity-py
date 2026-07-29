from __future__ import annotations

from e2e.live.helpers import create_client


def test_contextualized_embeddings() -> None:
    with create_client() as client:
        embeddings = client.contextualized_embeddings.create(
            dimensions=128,
            input=[["Perplexity answers questions.", "Its answers include citations."]],
            model="pplx-embed-context-v1-0.6b",
        )

    assert embeddings.model
    assert embeddings.data
    assert embeddings.data[0].data
    assert embeddings.data[0].data[0].embedding
