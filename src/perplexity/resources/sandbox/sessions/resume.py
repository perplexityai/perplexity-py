# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.sandbox.sessions import resume_create_params
from ....types.shared.sandbox_session_response import SandboxSessionResponse

__all__ = ["ResumeResource", "AsyncResumeResource"]


class ResumeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResumeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return ResumeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResumeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return ResumeResourceWithStreamingResponse(self)

    def create(
        self,
        session_id: str,
        *,
        network_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxSessionResponse:
        """
        Resume a paused sandbox session from its S3 snapshot.

        Args:
          network_enabled: Override network setting when resuming

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/v1/sandbox/sessions/{session_id}/resume",
            body=maybe_transform({"network_enabled": network_enabled}, resume_create_params.ResumeCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxSessionResponse,
        )


class AsyncResumeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResumeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return AsyncResumeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResumeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return AsyncResumeResourceWithStreamingResponse(self)

    async def create(
        self,
        session_id: str,
        *,
        network_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxSessionResponse:
        """
        Resume a paused sandbox session from its S3 snapshot.

        Args:
          network_enabled: Override network setting when resuming

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/v1/sandbox/sessions/{session_id}/resume",
            body=await async_maybe_transform(
                {"network_enabled": network_enabled}, resume_create_params.ResumeCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxSessionResponse,
        )


class ResumeResourceWithRawResponse:
    def __init__(self, resume: ResumeResource) -> None:
        self._resume = resume

        self.create = to_raw_response_wrapper(
            resume.create,
        )


class AsyncResumeResourceWithRawResponse:
    def __init__(self, resume: AsyncResumeResource) -> None:
        self._resume = resume

        self.create = async_to_raw_response_wrapper(
            resume.create,
        )


class ResumeResourceWithStreamingResponse:
    def __init__(self, resume: ResumeResource) -> None:
        self._resume = resume

        self.create = to_streamed_response_wrapper(
            resume.create,
        )


class AsyncResumeResourceWithStreamingResponse:
    def __init__(self, resume: AsyncResumeResource) -> None:
        self._resume = resume

        self.create = async_to_streamed_response_wrapper(
            resume.create,
        )
