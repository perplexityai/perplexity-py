# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.shared.pause_sandbox_response import PauseSandboxResponse

__all__ = ["PauseResource", "AsyncPauseResource"]


class PauseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PauseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return PauseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PauseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return PauseResourceWithStreamingResponse(self)

    def create(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PauseSandboxResponse:
        """
        Pause the sandbox and snapshot its state to S3 for later resumption.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/v1/sandbox/sessions/{session_id}/pause",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PauseSandboxResponse,
        )


class AsyncPauseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPauseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return AsyncPauseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPauseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return AsyncPauseResourceWithStreamingResponse(self)

    async def create(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PauseSandboxResponse:
        """
        Pause the sandbox and snapshot its state to S3 for later resumption.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/v1/sandbox/sessions/{session_id}/pause",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PauseSandboxResponse,
        )


class PauseResourceWithRawResponse:
    def __init__(self, pause: PauseResource) -> None:
        self._pause = pause

        self.create = to_raw_response_wrapper(
            pause.create,
        )


class AsyncPauseResourceWithRawResponse:
    def __init__(self, pause: AsyncPauseResource) -> None:
        self._pause = pause

        self.create = async_to_raw_response_wrapper(
            pause.create,
        )


class PauseResourceWithStreamingResponse:
    def __init__(self, pause: PauseResource) -> None:
        self._pause = pause

        self.create = to_streamed_response_wrapper(
            pause.create,
        )


class AsyncPauseResourceWithStreamingResponse:
    def __init__(self, pause: AsyncPauseResource) -> None:
        self._pause = pause

        self.create = async_to_streamed_response_wrapper(
            pause.create,
        )
