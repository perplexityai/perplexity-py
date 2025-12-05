# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal

import httpx

from ..types import search_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.search_create_response import SearchCreateResponse

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        query: Union[str, SequenceNotStr[str]],
        country: Optional[str] | Omit = omit,
        display_server_time: bool | Omit = omit,
        last_updated_after_filter: Optional[str] | Omit = omit,
        last_updated_before_filter: Optional[str] | Omit = omit,
        max_results: int | Omit = omit,
        max_tokens: int | Omit = omit,
        max_tokens_per_page: int | Omit = omit,
        search_after_date_filter: Optional[str] | Omit = omit,
        search_before_date_filter: Optional[str] | Omit = omit,
        search_domain_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        search_language_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        search_mode: Optional[Literal["web", "academic", "sec"]] | Omit = omit,
        search_recency_filter: Optional[Literal["hour", "day", "week", "month", "year"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchCreateResponse:
        """
        Search the web and retrieve relevant web page contents.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/search",
            body=maybe_transform(
                {
                    "query": query,
                    "country": country,
                    "display_server_time": display_server_time,
                    "last_updated_after_filter": last_updated_after_filter,
                    "last_updated_before_filter": last_updated_before_filter,
                    "max_results": max_results,
                    "max_tokens": max_tokens,
                    "max_tokens_per_page": max_tokens_per_page,
                    "search_after_date_filter": search_after_date_filter,
                    "search_before_date_filter": search_before_date_filter,
                    "search_domain_filter": search_domain_filter,
                    "search_language_filter": search_language_filter,
                    "search_mode": search_mode,
                    "search_recency_filter": search_recency_filter,
                },
                search_create_params.SearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchCreateResponse,
        )


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        query: Union[str, SequenceNotStr[str]],
        country: Optional[str] | Omit = omit,
        display_server_time: bool | Omit = omit,
        last_updated_after_filter: Optional[str] | Omit = omit,
        last_updated_before_filter: Optional[str] | Omit = omit,
        max_results: int | Omit = omit,
        max_tokens: int | Omit = omit,
        max_tokens_per_page: int | Omit = omit,
        search_after_date_filter: Optional[str] | Omit = omit,
        search_before_date_filter: Optional[str] | Omit = omit,
        search_domain_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        search_language_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        search_mode: Optional[Literal["web", "academic", "sec"]] | Omit = omit,
        search_recency_filter: Optional[Literal["hour", "day", "week", "month", "year"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchCreateResponse:
        """
        Search the web and retrieve relevant web page contents.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "country": country,
                    "display_server_time": display_server_time,
                    "last_updated_after_filter": last_updated_after_filter,
                    "last_updated_before_filter": last_updated_before_filter,
                    "max_results": max_results,
                    "max_tokens": max_tokens,
                    "max_tokens_per_page": max_tokens_per_page,
                    "search_after_date_filter": search_after_date_filter,
                    "search_before_date_filter": search_before_date_filter,
                    "search_domain_filter": search_domain_filter,
                    "search_language_filter": search_language_filter,
                    "search_mode": search_mode,
                    "search_recency_filter": search_recency_filter,
                },
                search_create_params.SearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchCreateResponse,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.create = to_raw_response_wrapper(
            search.create,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.create = async_to_raw_response_wrapper(
            search.create,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.create = to_streamed_response_wrapper(
            search.create,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.create = async_to_streamed_response_wrapper(
            search.create,
        )
