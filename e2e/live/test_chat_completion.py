from __future__ import annotations

import asyncio

from perplexity import AsyncPerplexity
from e2e.live.helpers import api_key


def test_chat_completion() -> None:
    async def run() -> None:
        async with AsyncPerplexity(api_key=api_key(), max_retries=0) as client:
            completion = await client.chat.completions.create(
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
