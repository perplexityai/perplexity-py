# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.async_.chat import completion_get_params, completion_create_params
from ....types.async_.chat.completion_get_response import CompletionGetResponse
from ....types.async_.chat.completion_list_response import CompletionListResponse
from ....types.async_.chat.completion_create_response import CompletionCreateResponse

__all__ = ["CompletionsResource", "AsyncCompletionsResource"]


class CompletionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return CompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return CompletionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        request: completion_create_params.Request,
        idempotency_key: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse:
        """
        Submit an asynchronous chat completion request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/async/chat/completions",
            body=maybe_transform(
                {
                    "request": request,
                    "idempotency_key": idempotency_key,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionCreateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionListResponse:
        """Retrieve a list of all asynchronous chat completion requests for a given user."""
        return self._get(
            "/async/chat/completions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionListResponse,
        )

    def get(
        self,
        api_request: str,
        *,
        local_mode: bool | Omit = omit,
        x_client_env: str | Omit = omit,
        x_client_name: str | Omit = omit,
        x_created_at_epoch_seconds: str | Omit = omit,
        x_request_time: str | Omit = omit,
        x_usage_tier: str | Omit = omit,
        x_user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionGetResponse:
        """
        Retrieve the response for a given asynchronous chat completion request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_request:
            raise ValueError(f"Expected a non-empty value for `api_request` but received {api_request!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "x-client-env": x_client_env,
                    "x-client-name": x_client_name,
                    "x-created-at-epoch-seconds": x_created_at_epoch_seconds,
                    "x-request-time": x_request_time,
                    "x-usage-tier": x_usage_tier,
                    "x-user-id": x_user_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            f"/async/chat/completions/{api_request}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"local_mode": local_mode}, completion_get_params.CompletionGetParams),
            ),
            cast_to=CompletionGetResponse,
        )


class AsyncCompletionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return AsyncCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return AsyncCompletionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        request: completion_create_params.Request,
        idempotency_key: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse:
        """
        Submit an asynchronous chat completion request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/async/chat/completions",
            body=await async_maybe_transform(
                {
                    "request": request,
                    "idempotency_key": idempotency_key,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionCreateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionListResponse:
        """Retrieve a list of all asynchronous chat completion requests for a given user."""
        return await self._get(
            "/async/chat/completions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionListResponse,
        )

    async def get(
        self,
        api_request: str,
        *,
        local_mode: bool | Omit = omit,
        x_client_env: str | Omit = omit,
        x_client_name: str | Omit = omit,
        x_created_at_epoch_seconds: str | Omit = omit,
        x_request_time: str | Omit = omit,
        x_usage_tier: str | Omit = omit,
        x_user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionGetResponse:
        """
        Retrieve the response for a given asynchronous chat completion request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_request:
            raise ValueError(f"Expected a non-empty value for `api_request` but received {api_request!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "x-client-env": x_client_env,
                    "x-client-name": x_client_name,
                    "x-created-at-epoch-seconds": x_created_at_epoch_seconds,
                    "x-request-time": x_request_time,
                    "x-usage-tier": x_usage_tier,
                    "x-user-id": x_user_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            f"/async/chat/completions/{api_request}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"local_mode": local_mode}, completion_get_params.CompletionGetParams
                ),
            ),
            cast_to=CompletionGetResponse,
        )


class CompletionsResourceWithRawResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_raw_response_wrapper(
            completions.create,
        )
        self.list = to_raw_response_wrapper(
            completions.list,
        )
        self.get = to_raw_response_wrapper(
            completions.get,
        )


class AsyncCompletionsResourceWithRawResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_raw_response_wrapper(
            completions.create,
        )
        self.list = async_to_raw_response_wrapper(
            completions.list,
        )
        self.get = async_to_raw_response_wrapper(
            completions.get,
        )


class CompletionsResourceWithStreamingResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )
        self.list = to_streamed_response_wrapper(
            completions.list,
        )
        self.get = to_streamed_response_wrapper(
            completions.get,
        )


class AsyncCompletionsResourceWithStreamingResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            completions.list,
        )
        self.get = async_to_streamed_response_wrapper(
            completions.get,
        )
