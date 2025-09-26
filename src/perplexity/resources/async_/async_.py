# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .chat.chat import (
    ChatResource,
    AsyncChatResource,
    ChatResourceWithRawResponse,
    AsyncChatResourceWithRawResponse,
    ChatResourceWithStreamingResponse,
    AsyncChatResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AsyncResource", "AsyncAsyncResource"]


class AsyncResource(SyncAPIResource):
    @cached_property
    def chat(self) -> ChatResource:
        return ChatResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return AsyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return AsyncResourceWithStreamingResponse(self)


class AsyncAsyncResource(AsyncAPIResource):
    @cached_property
    def chat(self) -> AsyncChatResource:
        return AsyncChatResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAsyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return AsyncAsyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAsyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return AsyncAsyncResourceWithStreamingResponse(self)


class AsyncResourceWithRawResponse:
    def __init__(self, async_: AsyncResource) -> None:
        self._async_ = async_

    @cached_property
    def chat(self) -> ChatResourceWithRawResponse:
        return ChatResourceWithRawResponse(self._async_.chat)


class AsyncAsyncResourceWithRawResponse:
    def __init__(self, async_: AsyncAsyncResource) -> None:
        self._async_ = async_

    @cached_property
    def chat(self) -> AsyncChatResourceWithRawResponse:
        return AsyncChatResourceWithRawResponse(self._async_.chat)


class AsyncResourceWithStreamingResponse:
    def __init__(self, async_: AsyncResource) -> None:
        self._async_ = async_

    @cached_property
    def chat(self) -> ChatResourceWithStreamingResponse:
        return ChatResourceWithStreamingResponse(self._async_.chat)


class AsyncAsyncResourceWithStreamingResponse:
    def __init__(self, async_: AsyncAsyncResource) -> None:
        self._async_ = async_

    @cached_property
    def chat(self) -> AsyncChatResourceWithStreamingResponse:
        return AsyncChatResourceWithStreamingResponse(self._async_.chat)
