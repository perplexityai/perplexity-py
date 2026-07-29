from __future__ import annotations

from e2e.live.helpers import create_client


def test_search() -> None:
    with create_client() as client:
        search = client.search.create(max_results=1, query="Perplexity AI")

    assert search.id
    assert search.results
    assert search.results[0].title
    assert search.results[0].url
    assert isinstance(search.results[0].snippet, str)
