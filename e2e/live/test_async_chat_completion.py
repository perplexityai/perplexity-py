from __future__ import annotations

import time

import pytest

from e2e.live.helpers import create_client


def test_async_chat_completion() -> None:
    with create_client() as client:
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
