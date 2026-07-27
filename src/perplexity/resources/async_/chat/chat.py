# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from .completions import (
    CompletionsResourceWithRawResponse,
    AsyncCompletionsResourceWithRawResponse,
    CompletionsResourceWithStreamingResponse,
    AsyncCompletionsResourceWithStreamingResponse,
)
from ....generated.api import (
    AsyncChatResource as GeneratedChatResource,
    AsyncClientAsyncChatResource as GeneratedAsyncChatResource,
)

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(GeneratedChatResource):
    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)


class AsyncChatResource(GeneratedAsyncChatResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)


class ChatResourceWithRawResponse:
    def __init__(self, chat: GeneratedChatResource) -> None:
        self._chat = chat

    @cached_property
    def completions(self) -> CompletionsResourceWithRawResponse:
        return CompletionsResourceWithRawResponse(self._chat.completions)


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: GeneratedAsyncChatResource) -> None:
        self._chat = chat

    @cached_property
    def completions(self) -> AsyncCompletionsResourceWithRawResponse:
        return AsyncCompletionsResourceWithRawResponse(self._chat.completions)


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: GeneratedChatResource) -> None:
        self._chat = chat

    @cached_property
    def completions(self) -> CompletionsResourceWithStreamingResponse:
        return CompletionsResourceWithStreamingResponse(self._chat.completions)


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: GeneratedAsyncChatResource) -> None:
        self._chat = chat

    @cached_property
    def completions(self) -> AsyncCompletionsResourceWithStreamingResponse:
        return AsyncCompletionsResourceWithStreamingResponse(self._chat.completions)
