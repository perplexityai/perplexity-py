# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven, SequenceNotStr
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.chat import completion_create_params
from ..._base_client import make_request_options
from ...types.shared_params.chat_message import ChatMessage
from ...types.chat.completion_create_response import CompletionCreateResponse

__all__ = ["CompletionsResource", "AsyncCompletionsResource"]


class CompletionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ppl-ai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return CompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ppl-ai/perplexity-py#with_streaming_response
        """
        return CompletionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        messages: Iterable[ChatMessage],
        model: Literal["sonar", "sonar-pro", "sonar-deep-research", "sonar-reasoning", "sonar-reasoning-pro"],
        disable_search: bool | NotGiven = NOT_GIVEN,
        enable_search_classifier: bool | NotGiven = NOT_GIVEN,
        last_updated_after_filter: Optional[str] | NotGiven = NOT_GIVEN,
        last_updated_before_filter: Optional[str] | NotGiven = NOT_GIVEN,
        reasoning_effort: Optional[Literal["low", "medium", "high"]] | NotGiven = NOT_GIVEN,
        return_images: bool | NotGiven = NOT_GIVEN,
        return_related_questions: bool | NotGiven = NOT_GIVEN,
        search_after_date_filter: Optional[str] | NotGiven = NOT_GIVEN,
        search_before_date_filter: Optional[str] | NotGiven = NOT_GIVEN,
        search_domain_filter: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        search_mode: Optional[Literal["web", "academic", "sec"]] | NotGiven = NOT_GIVEN,
        search_recency_filter: Optional[Literal["hour", "day", "week", "month", "year"]] | NotGiven = NOT_GIVEN,
        web_search_options: completion_create_params.WebSearchOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionCreateResponse:
        """
        Generates a model's response for the given chat conversation with integrated
        search capabilities

        Args:
          messages: A list of messages comprising the conversation so far

          model: The name of the model that will complete your prompt

          disable_search: Disables web search completely - model uses only training data

          enable_search_classifier: Enables classifier that decides if web search is needed

          last_updated_after_filter: Only include content last updated after this date (YYYY-MM-DD)

          last_updated_before_filter: Only include content last updated before this date (YYYY-MM-DD)

          reasoning_effort: Controls computational effort for sonar-deep-research model. Higher effort =
              more thorough but more tokens

          return_images: Whether to include images in search results

          return_related_questions: Whether to return related questions

          search_after_date_filter: Only include content published after this date (YYYY-MM-DD)

          search_before_date_filter: Only include content published before this date (YYYY-MM-DD)

          search_domain_filter: List of domains to limit search results to. Use '-' prefix to exclude domains

          search_mode: Type of search: 'web' for general, 'academic' for scholarly, 'sec' for SEC
              filings

          search_recency_filter: Filter results by how recently they were published

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/chat/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "disable_search": disable_search,
                    "enable_search_classifier": enable_search_classifier,
                    "last_updated_after_filter": last_updated_after_filter,
                    "last_updated_before_filter": last_updated_before_filter,
                    "reasoning_effort": reasoning_effort,
                    "return_images": return_images,
                    "return_related_questions": return_related_questions,
                    "search_after_date_filter": search_after_date_filter,
                    "search_before_date_filter": search_before_date_filter,
                    "search_domain_filter": search_domain_filter,
                    "search_mode": search_mode,
                    "search_recency_filter": search_recency_filter,
                    "web_search_options": web_search_options,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionCreateResponse,
        )


class AsyncCompletionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ppl-ai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return AsyncCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ppl-ai/perplexity-py#with_streaming_response
        """
        return AsyncCompletionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        messages: Iterable[ChatMessage],
        model: Literal["sonar", "sonar-pro", "sonar-deep-research", "sonar-reasoning", "sonar-reasoning-pro"],
        disable_search: bool | NotGiven = NOT_GIVEN,
        enable_search_classifier: bool | NotGiven = NOT_GIVEN,
        last_updated_after_filter: Optional[str] | NotGiven = NOT_GIVEN,
        last_updated_before_filter: Optional[str] | NotGiven = NOT_GIVEN,
        reasoning_effort: Optional[Literal["low", "medium", "high"]] | NotGiven = NOT_GIVEN,
        return_images: bool | NotGiven = NOT_GIVEN,
        return_related_questions: bool | NotGiven = NOT_GIVEN,
        search_after_date_filter: Optional[str] | NotGiven = NOT_GIVEN,
        search_before_date_filter: Optional[str] | NotGiven = NOT_GIVEN,
        search_domain_filter: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        search_mode: Optional[Literal["web", "academic", "sec"]] | NotGiven = NOT_GIVEN,
        search_recency_filter: Optional[Literal["hour", "day", "week", "month", "year"]] | NotGiven = NOT_GIVEN,
        web_search_options: completion_create_params.WebSearchOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionCreateResponse:
        """
        Generates a model's response for the given chat conversation with integrated
        search capabilities

        Args:
          messages: A list of messages comprising the conversation so far

          model: The name of the model that will complete your prompt

          disable_search: Disables web search completely - model uses only training data

          enable_search_classifier: Enables classifier that decides if web search is needed

          last_updated_after_filter: Only include content last updated after this date (YYYY-MM-DD)

          last_updated_before_filter: Only include content last updated before this date (YYYY-MM-DD)

          reasoning_effort: Controls computational effort for sonar-deep-research model. Higher effort =
              more thorough but more tokens

          return_images: Whether to include images in search results

          return_related_questions: Whether to return related questions

          search_after_date_filter: Only include content published after this date (YYYY-MM-DD)

          search_before_date_filter: Only include content published before this date (YYYY-MM-DD)

          search_domain_filter: List of domains to limit search results to. Use '-' prefix to exclude domains

          search_mode: Type of search: 'web' for general, 'academic' for scholarly, 'sec' for SEC
              filings

          search_recency_filter: Filter results by how recently they were published

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/chat/completions",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "disable_search": disable_search,
                    "enable_search_classifier": enable_search_classifier,
                    "last_updated_after_filter": last_updated_after_filter,
                    "last_updated_before_filter": last_updated_before_filter,
                    "reasoning_effort": reasoning_effort,
                    "return_images": return_images,
                    "return_related_questions": return_related_questions,
                    "search_after_date_filter": search_after_date_filter,
                    "search_before_date_filter": search_before_date_filter,
                    "search_domain_filter": search_domain_filter,
                    "search_mode": search_mode,
                    "search_recency_filter": search_recency_filter,
                    "web_search_options": web_search_options,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionCreateResponse,
        )


class CompletionsResourceWithRawResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_raw_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithRawResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_raw_response_wrapper(
            completions.create,
        )


class CompletionsResourceWithStreamingResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithStreamingResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
