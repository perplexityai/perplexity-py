from __future__ import annotations

from e2e.live.helpers import create_client


def test_streaming_responses() -> None:
    with create_client() as client:
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
