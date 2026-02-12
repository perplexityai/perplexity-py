# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from .pause import (
    PauseResource,
    AsyncPauseResource,
    PauseResourceWithRawResponse,
    AsyncPauseResourceWithRawResponse,
    PauseResourceWithStreamingResponse,
    AsyncPauseResourceWithStreamingResponse,
)
from .resume import (
    ResumeResource,
    AsyncResumeResource,
    ResumeResourceWithRawResponse,
    AsyncResumeResourceWithRawResponse,
    ResumeResourceWithStreamingResponse,
    AsyncResumeResourceWithStreamingResponse,
)
from .execute import (
    ExecuteResource,
    AsyncExecuteResource,
    ExecuteResourceWithRawResponse,
    AsyncExecuteResourceWithRawResponse,
    ExecuteResourceWithStreamingResponse,
    AsyncExecuteResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from .processes import (
    ProcessesResource,
    AsyncProcessesResource,
    ProcessesResourceWithRawResponse,
    AsyncProcessesResourceWithRawResponse,
    ProcessesResourceWithStreamingResponse,
    AsyncProcessesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.sandbox import session_create_params
from ....types.shared.sandbox_session_response import SandboxSessionResponse

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    @cached_property
    def execute(self) -> ExecuteResource:
        return ExecuteResource(self._client)

    @cached_property
    def pause(self) -> PauseResource:
        return PauseResource(self._client)

    @cached_property
    def resume(self) -> ResumeResource:
        return ResumeResource(self._client)

    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def processes(self) -> ProcessesResource:
        return ProcessesResource(self._client)

    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return SessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return SessionsResourceWithStreamingResponse(self)

    def create(
        self,
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
        Create a new isolated sandbox environment for code execution.

        Args:
          network_enabled: Enable network access in the sandbox

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/sandbox/sessions",
            body=maybe_transform({"network_enabled": network_enabled}, session_create_params.SessionCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxSessionResponse,
        )

    def delete(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Terminate and clean up a sandbox session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/sandbox/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxSessionResponse:
        """
        Retrieve the current status of a sandbox session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/v1/sandbox/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxSessionResponse,
        )


class AsyncSessionsResource(AsyncAPIResource):
    @cached_property
    def execute(self) -> AsyncExecuteResource:
        return AsyncExecuteResource(self._client)

    @cached_property
    def pause(self) -> AsyncPauseResource:
        return AsyncPauseResource(self._client)

    @cached_property
    def resume(self) -> AsyncResumeResource:
        return AsyncResumeResource(self._client)

    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def processes(self) -> AsyncProcessesResource:
        return AsyncProcessesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return AsyncSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
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
        Create a new isolated sandbox environment for code execution.

        Args:
          network_enabled: Enable network access in the sandbox

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/sandbox/sessions",
            body=await async_maybe_transform(
                {"network_enabled": network_enabled}, session_create_params.SessionCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxSessionResponse,
        )

    async def delete(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Terminate and clean up a sandbox session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/sandbox/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxSessionResponse:
        """
        Retrieve the current status of a sandbox session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/v1/sandbox/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxSessionResponse,
        )


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_raw_response_wrapper(
            sessions.create,
        )
        self.delete = to_raw_response_wrapper(
            sessions.delete,
        )
        self.get = to_raw_response_wrapper(
            sessions.get,
        )

    @cached_property
    def execute(self) -> ExecuteResourceWithRawResponse:
        return ExecuteResourceWithRawResponse(self._sessions.execute)

    @cached_property
    def pause(self) -> PauseResourceWithRawResponse:
        return PauseResourceWithRawResponse(self._sessions.pause)

    @cached_property
    def resume(self) -> ResumeResourceWithRawResponse:
        return ResumeResourceWithRawResponse(self._sessions.resume)

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._sessions.files)

    @cached_property
    def processes(self) -> ProcessesResourceWithRawResponse:
        return ProcessesResourceWithRawResponse(self._sessions.processes)


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_raw_response_wrapper(
            sessions.create,
        )
        self.delete = async_to_raw_response_wrapper(
            sessions.delete,
        )
        self.get = async_to_raw_response_wrapper(
            sessions.get,
        )

    @cached_property
    def execute(self) -> AsyncExecuteResourceWithRawResponse:
        return AsyncExecuteResourceWithRawResponse(self._sessions.execute)

    @cached_property
    def pause(self) -> AsyncPauseResourceWithRawResponse:
        return AsyncPauseResourceWithRawResponse(self._sessions.pause)

    @cached_property
    def resume(self) -> AsyncResumeResourceWithRawResponse:
        return AsyncResumeResourceWithRawResponse(self._sessions.resume)

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._sessions.files)

    @cached_property
    def processes(self) -> AsyncProcessesResourceWithRawResponse:
        return AsyncProcessesResourceWithRawResponse(self._sessions.processes)


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_streamed_response_wrapper(
            sessions.create,
        )
        self.delete = to_streamed_response_wrapper(
            sessions.delete,
        )
        self.get = to_streamed_response_wrapper(
            sessions.get,
        )

    @cached_property
    def execute(self) -> ExecuteResourceWithStreamingResponse:
        return ExecuteResourceWithStreamingResponse(self._sessions.execute)

    @cached_property
    def pause(self) -> PauseResourceWithStreamingResponse:
        return PauseResourceWithStreamingResponse(self._sessions.pause)

    @cached_property
    def resume(self) -> ResumeResourceWithStreamingResponse:
        return ResumeResourceWithStreamingResponse(self._sessions.resume)

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._sessions.files)

    @cached_property
    def processes(self) -> ProcessesResourceWithStreamingResponse:
        return ProcessesResourceWithStreamingResponse(self._sessions.processes)


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_streamed_response_wrapper(
            sessions.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            sessions.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            sessions.get,
        )

    @cached_property
    def execute(self) -> AsyncExecuteResourceWithStreamingResponse:
        return AsyncExecuteResourceWithStreamingResponse(self._sessions.execute)

    @cached_property
    def pause(self) -> AsyncPauseResourceWithStreamingResponse:
        return AsyncPauseResourceWithStreamingResponse(self._sessions.pause)

    @cached_property
    def resume(self) -> AsyncResumeResourceWithStreamingResponse:
        return AsyncResumeResourceWithStreamingResponse(self._sessions.resume)

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._sessions.files)

    @cached_property
    def processes(self) -> AsyncProcessesResourceWithStreamingResponse:
        return AsyncProcessesResourceWithStreamingResponse(self._sessions.processes)
