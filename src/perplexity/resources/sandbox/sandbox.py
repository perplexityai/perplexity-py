# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .sessions.sessions import (
    SessionsResource,
    AsyncSessionsResource,
    SessionsResourceWithRawResponse,
    AsyncSessionsResourceWithRawResponse,
    SessionsResourceWithStreamingResponse,
    AsyncSessionsResourceWithStreamingResponse,
)

__all__ = ["SandboxResource", "AsyncSandboxResource"]


class SandboxResource(SyncAPIResource):
    @cached_property
    def sessions(self) -> SessionsResource:
        return SessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SandboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return SandboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SandboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return SandboxResourceWithStreamingResponse(self)


class AsyncSandboxResource(AsyncAPIResource):
    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        return AsyncSessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSandboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return AsyncSandboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSandboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return AsyncSandboxResourceWithStreamingResponse(self)


class SandboxResourceWithRawResponse:
    def __init__(self, sandbox: SandboxResource) -> None:
        self._sandbox = sandbox

    @cached_property
    def sessions(self) -> SessionsResourceWithRawResponse:
        return SessionsResourceWithRawResponse(self._sandbox.sessions)


class AsyncSandboxResourceWithRawResponse:
    def __init__(self, sandbox: AsyncSandboxResource) -> None:
        self._sandbox = sandbox

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithRawResponse:
        return AsyncSessionsResourceWithRawResponse(self._sandbox.sessions)


class SandboxResourceWithStreamingResponse:
    def __init__(self, sandbox: SandboxResource) -> None:
        self._sandbox = sandbox

    @cached_property
    def sessions(self) -> SessionsResourceWithStreamingResponse:
        return SessionsResourceWithStreamingResponse(self._sandbox.sessions)


class AsyncSandboxResourceWithStreamingResponse:
    def __init__(self, sandbox: AsyncSandboxResource) -> None:
        self._sandbox = sandbox

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithStreamingResponse:
        return AsyncSessionsResourceWithStreamingResponse(self._sandbox.sessions)
