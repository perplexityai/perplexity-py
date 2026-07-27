from __future__ import annotations

import json

import httpx

from perplexity import Perplexity
from perplexity.types import SearchCreateResponse
from perplexity.generated.api import SearchCreateResponse as GeneratedSearchCreateResponse


def test_client_uses_generated_api_and_model() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(
            200,
            json={"id": "search-1", "results": []},
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
    assert requests[0].url == "https://example.test/search"
    assert json.loads(requests[0].content) == {"query": "perplexity"}
