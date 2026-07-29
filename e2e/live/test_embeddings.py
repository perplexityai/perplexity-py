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
