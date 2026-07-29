from __future__ import annotations

from e2e.live.helpers import create_client


def test_responses() -> None:
    with create_client() as client:
        response = client.responses.create(
            input="Reply with only the word pong.",
            max_output_tokens=128,
            preset="pro-search",
        )

    assert response.id
    assert response.object == "response"
    assert response.output
    assert response.status == "completed"
