# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .sessions import (
    SessionsResource,
    AsyncSessionsResource,
    SessionsResourceWithRawResponse,
    AsyncSessionsResourceWithRawResponse,
    SessionsResourceWithStreamingResponse,
    AsyncSessionsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["BrowserResource", "AsyncBrowserResource"]


class BrowserResource(SyncAPIResource):
    @cached_property
    def sessions(self) -> SessionsResource:
        return SessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BrowserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return BrowserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrowserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return BrowserResourceWithStreamingResponse(self)


class AsyncBrowserResource(AsyncAPIResource):
    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        return AsyncSessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBrowserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return AsyncBrowserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrowserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return AsyncBrowserResourceWithStreamingResponse(self)


class BrowserResourceWithRawResponse:
    def __init__(self, browser: BrowserResource) -> None:
        self._browser = browser

    @cached_property
    def sessions(self) -> SessionsResourceWithRawResponse:
        return SessionsResourceWithRawResponse(self._browser.sessions)


class AsyncBrowserResourceWithRawResponse:
    def __init__(self, browser: AsyncBrowserResource) -> None:
        self._browser = browser

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithRawResponse:
        return AsyncSessionsResourceWithRawResponse(self._browser.sessions)


class BrowserResourceWithStreamingResponse:
    def __init__(self, browser: BrowserResource) -> None:
        self._browser = browser

    @cached_property
    def sessions(self) -> SessionsResourceWithStreamingResponse:
        return SessionsResourceWithStreamingResponse(self._browser.sessions)


class AsyncBrowserResourceWithStreamingResponse:
    def __init__(self, browser: AsyncBrowserResource) -> None:
        self._browser = browser

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithStreamingResponse:
        return AsyncSessionsResourceWithStreamingResponse(self._browser.sessions)
