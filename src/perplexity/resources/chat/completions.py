# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
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
from ...types.chat.completion_create_response import CompletionCreateResponse
from ...types.shared_params.chat_message_input import ChatMessageInput

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
        messages: Iterable[ChatMessageInput],
        model: str,
        _debug_pro_search: bool | NotGiven = NOT_GIVEN,
        _inputs: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        _is_browser_agent: Optional[bool] | NotGiven = NOT_GIVEN,
        _prompt_token_length: Optional[int] | NotGiven = NOT_GIVEN,
        best_of: Optional[int] | NotGiven = NOT_GIVEN,
        country: Optional[str] | NotGiven = NOT_GIVEN,
        cum_logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        debug_params: Optional[completion_create_params.DebugParams] | NotGiven = NOT_GIVEN,
        disable_search: Optional[bool] | NotGiven = NOT_GIVEN,
        diverse_first_token: Optional[bool] | NotGiven = NOT_GIVEN,
        enable_search_classifier: Optional[bool] | NotGiven = NOT_GIVEN,
        file_workspace_id: Optional[str] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        has_image_url: bool | NotGiven = NOT_GIVEN,
        image_domain_filter: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        image_format_filter: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        last_updated_after_filter: Optional[str] | NotGiven = NOT_GIVEN,
        last_updated_before_filter: Optional[str] | NotGiven = NOT_GIVEN,
        latitude: Optional[float] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        longitude: Optional[float] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        num_images: int | NotGiven = NOT_GIVEN,
        num_search_results: int | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        ranking_model: Optional[str] | NotGiven = NOT_GIVEN,
        reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]] | NotGiven = NOT_GIVEN,
        response_format: Optional[completion_create_params.ResponseFormat] | NotGiven = NOT_GIVEN,
        response_metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        return_images: Optional[bool] | NotGiven = NOT_GIVEN,
        return_related_questions: Optional[bool] | NotGiven = NOT_GIVEN,
        safe_search: Optional[bool] | NotGiven = NOT_GIVEN,
        search_after_date_filter: Optional[str] | NotGiven = NOT_GIVEN,
        search_before_date_filter: Optional[str] | NotGiven = NOT_GIVEN,
        search_domain_filter: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        search_internal_properties: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        search_mode: Optional[Literal["web", "academic", "sec"]] | NotGiven = NOT_GIVEN,
        search_recency_filter: Optional[Literal["hour", "day", "week", "month", "year"]] | NotGiven = NOT_GIVEN,
        search_tenant: Optional[str] | NotGiven = NOT_GIVEN,
        stop: Union[str, SequenceNotStr[str], None] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: Optional[Literal["none", "auto", "required"]] | NotGiven = NOT_GIVEN,
        tools: Optional[Iterable[completion_create_params.Tool]] | NotGiven = NOT_GIVEN,
        top_k: Optional[int] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        updated_after_timestamp: Optional[int] | NotGiven = NOT_GIVEN,
        updated_before_timestamp: Optional[int] | NotGiven = NOT_GIVEN,
        web_search_options: completion_create_params.WebSearchOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionCreateResponse:
        """
        FastAPI wrapper around chat completions

        Args:
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
                    "_debug_pro_search": _debug_pro_search,
                    "_inputs": _inputs,
                    "_is_browser_agent": _is_browser_agent,
                    "_prompt_token_length": _prompt_token_length,
                    "best_of": best_of,
                    "country": country,
                    "cum_logprobs": cum_logprobs,
                    "debug_params": debug_params,
                    "disable_search": disable_search,
                    "diverse_first_token": diverse_first_token,
                    "enable_search_classifier": enable_search_classifier,
                    "file_workspace_id": file_workspace_id,
                    "frequency_penalty": frequency_penalty,
                    "has_image_url": has_image_url,
                    "image_domain_filter": image_domain_filter,
                    "image_format_filter": image_format_filter,
                    "last_updated_after_filter": last_updated_after_filter,
                    "last_updated_before_filter": last_updated_before_filter,
                    "latitude": latitude,
                    "logprobs": logprobs,
                    "longitude": longitude,
                    "max_tokens": max_tokens,
                    "n": n,
                    "num_images": num_images,
                    "num_search_results": num_search_results,
                    "parallel_tool_calls": parallel_tool_calls,
                    "presence_penalty": presence_penalty,
                    "ranking_model": ranking_model,
                    "reasoning_effort": reasoning_effort,
                    "response_format": response_format,
                    "response_metadata": response_metadata,
                    "return_images": return_images,
                    "return_related_questions": return_related_questions,
                    "safe_search": safe_search,
                    "search_after_date_filter": search_after_date_filter,
                    "search_before_date_filter": search_before_date_filter,
                    "search_domain_filter": search_domain_filter,
                    "search_internal_properties": search_internal_properties,
                    "search_mode": search_mode,
                    "search_recency_filter": search_recency_filter,
                    "search_tenant": search_tenant,
                    "stop": stop,
                    "stream": stream,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "updated_after_timestamp": updated_after_timestamp,
                    "updated_before_timestamp": updated_before_timestamp,
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
        messages: Iterable[ChatMessageInput],
        model: str,
        _debug_pro_search: bool | NotGiven = NOT_GIVEN,
        _inputs: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        _is_browser_agent: Optional[bool] | NotGiven = NOT_GIVEN,
        _prompt_token_length: Optional[int] | NotGiven = NOT_GIVEN,
        best_of: Optional[int] | NotGiven = NOT_GIVEN,
        country: Optional[str] | NotGiven = NOT_GIVEN,
        cum_logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        debug_params: Optional[completion_create_params.DebugParams] | NotGiven = NOT_GIVEN,
        disable_search: Optional[bool] | NotGiven = NOT_GIVEN,
        diverse_first_token: Optional[bool] | NotGiven = NOT_GIVEN,
        enable_search_classifier: Optional[bool] | NotGiven = NOT_GIVEN,
        file_workspace_id: Optional[str] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        has_image_url: bool | NotGiven = NOT_GIVEN,
        image_domain_filter: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        image_format_filter: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        last_updated_after_filter: Optional[str] | NotGiven = NOT_GIVEN,
        last_updated_before_filter: Optional[str] | NotGiven = NOT_GIVEN,
        latitude: Optional[float] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        longitude: Optional[float] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        num_images: int | NotGiven = NOT_GIVEN,
        num_search_results: int | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        ranking_model: Optional[str] | NotGiven = NOT_GIVEN,
        reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]] | NotGiven = NOT_GIVEN,
        response_format: Optional[completion_create_params.ResponseFormat] | NotGiven = NOT_GIVEN,
        response_metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        return_images: Optional[bool] | NotGiven = NOT_GIVEN,
        return_related_questions: Optional[bool] | NotGiven = NOT_GIVEN,
        safe_search: Optional[bool] | NotGiven = NOT_GIVEN,
        search_after_date_filter: Optional[str] | NotGiven = NOT_GIVEN,
        search_before_date_filter: Optional[str] | NotGiven = NOT_GIVEN,
        search_domain_filter: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        search_internal_properties: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        search_mode: Optional[Literal["web", "academic", "sec"]] | NotGiven = NOT_GIVEN,
        search_recency_filter: Optional[Literal["hour", "day", "week", "month", "year"]] | NotGiven = NOT_GIVEN,
        search_tenant: Optional[str] | NotGiven = NOT_GIVEN,
        stop: Union[str, SequenceNotStr[str], None] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: Optional[Literal["none", "auto", "required"]] | NotGiven = NOT_GIVEN,
        tools: Optional[Iterable[completion_create_params.Tool]] | NotGiven = NOT_GIVEN,
        top_k: Optional[int] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        updated_after_timestamp: Optional[int] | NotGiven = NOT_GIVEN,
        updated_before_timestamp: Optional[int] | NotGiven = NOT_GIVEN,
        web_search_options: completion_create_params.WebSearchOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionCreateResponse:
        """
        FastAPI wrapper around chat completions

        Args:
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
                    "_debug_pro_search": _debug_pro_search,
                    "_inputs": _inputs,
                    "_is_browser_agent": _is_browser_agent,
                    "_prompt_token_length": _prompt_token_length,
                    "best_of": best_of,
                    "country": country,
                    "cum_logprobs": cum_logprobs,
                    "debug_params": debug_params,
                    "disable_search": disable_search,
                    "diverse_first_token": diverse_first_token,
                    "enable_search_classifier": enable_search_classifier,
                    "file_workspace_id": file_workspace_id,
                    "frequency_penalty": frequency_penalty,
                    "has_image_url": has_image_url,
                    "image_domain_filter": image_domain_filter,
                    "image_format_filter": image_format_filter,
                    "last_updated_after_filter": last_updated_after_filter,
                    "last_updated_before_filter": last_updated_before_filter,
                    "latitude": latitude,
                    "logprobs": logprobs,
                    "longitude": longitude,
                    "max_tokens": max_tokens,
                    "n": n,
                    "num_images": num_images,
                    "num_search_results": num_search_results,
                    "parallel_tool_calls": parallel_tool_calls,
                    "presence_penalty": presence_penalty,
                    "ranking_model": ranking_model,
                    "reasoning_effort": reasoning_effort,
                    "response_format": response_format,
                    "response_metadata": response_metadata,
                    "return_images": return_images,
                    "return_related_questions": return_related_questions,
                    "safe_search": safe_search,
                    "search_after_date_filter": search_after_date_filter,
                    "search_before_date_filter": search_before_date_filter,
                    "search_domain_filter": search_domain_filter,
                    "search_internal_properties": search_internal_properties,
                    "search_mode": search_mode,
                    "search_recency_filter": search_recency_filter,
                    "search_tenant": search_tenant,
                    "stop": stop,
                    "stream": stream,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "updated_after_timestamp": updated_after_timestamp,
                    "updated_before_timestamp": updated_before_timestamp,
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
