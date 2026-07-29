from __future__ import annotations

from e2e.live.helpers import create_client


def test_streaming_chat() -> None:
    with create_client() as client:
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
