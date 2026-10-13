from typing import Union
from typing_extensions import assert_type

from perplexity import Perplexity, AsyncPerplexity
from perplexity.generated.api import (
    Stream,
    AsyncStream,
    ResponsesResponseOutput,
    ResponseStreamEventOutput,
)


def check_sync(client: Perplexity, flag: bool) -> None:
    assert_type(client.responses.retrieve("response-id"), ResponsesResponseOutput)
    assert_type(
        client.responses.retrieve("response-id", stream=False, starting_after=0),
        ResponsesResponseOutput,
    )
    assert_type(
        client.responses.retrieve("response-id", stream=True, starting_after=0),
        Stream[ResponseStreamEventOutput],
    )
    assert_type(
        client.responses.retrieve("response-id", stream=flag, starting_after=0),
        Union[ResponsesResponseOutput, Stream[ResponseStreamEventOutput]],
    )


async def check_async(client: AsyncPerplexity, flag: bool) -> None:
    assert_type(await client.responses.retrieve("response-id"), ResponsesResponseOutput)
    assert_type(
        await client.responses.retrieve("response-id", stream=False, starting_after=0),
        ResponsesResponseOutput,
    )
    assert_type(
        await client.responses.retrieve("response-id", stream=True, starting_after=0),
        AsyncStream[ResponseStreamEventOutput],
    )
    assert_type(
        await client.responses.retrieve("response-id", stream=flag, starting_after=0),
        Union[ResponsesResponseOutput, AsyncStream[ResponseStreamEventOutput]],
    )
