# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ...types.chat import completion_create_params
from ..._base_client import make_request_options
from ...types.stream_chunk import StreamChunk
from ...types.shared_params.chat_message_input import ChatMessageInput
from ...types.shared_params.web_search_options import WebSearchOptions

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

    @overload
    def create(
        self,
        *,
        messages: Iterable[ChatMessageInput],
        model: str,
        _debug_pro_search: bool | Omit = omit,
        _force_new_agent: Optional[bool] | Omit = omit,
        _inputs: Optional[Iterable[int]] | Omit = omit,
        _prompt_token_length: Optional[int] | Omit = omit,
        best_of: Optional[int] | Omit = omit,
        country: Optional[str] | Omit = omit,
        cum_logprobs: Optional[bool] | Omit = omit,
        disable_search: Optional[bool] | Omit = omit,
        diverse_first_token: Optional[bool] | Omit = omit,
        enable_search_classifier: Optional[bool] | Omit = omit,
        file_workspace_id: Optional[str] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        has_image_url: bool | Omit = omit,
        image_domain_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        image_format_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        language_preference: Optional[str] | Omit = omit,
        last_updated_after_filter: Optional[str] | Omit = omit,
        last_updated_before_filter: Optional[str] | Omit = omit,
        latitude: Optional[float] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        longitude: Optional[float] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        n: Optional[int] | Omit = omit,
        num_images: int | Omit = omit,
        num_search_results: int | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        ranking_model: Optional[str] | Omit = omit,
        reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]] | Omit = omit,
        response_format: Optional[completion_create_params.ResponseFormat] | Omit = omit,
        response_metadata: Optional[Dict[str, object]] | Omit = omit,
        return_images: Optional[bool] | Omit = omit,
        return_related_questions: Optional[bool] | Omit = omit,
        safe_search: Optional[bool] | Omit = omit,
        search_after_date_filter: Optional[str] | Omit = omit,
        search_before_date_filter: Optional[str] | Omit = omit,
        search_domain_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        search_internal_properties: Optional[Dict[str, object]] | Omit = omit,
        search_language_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        search_mode: Optional[Literal["web", "academic", "sec"]] | Omit = omit,
        search_recency_filter: Optional[Literal["hour", "day", "week", "month", "year"]] | Omit = omit,
        search_tenant: Optional[str] | Omit = omit,
        stop: Union[str, SequenceNotStr[str], None] | Omit = omit,
        stream: Optional[Literal[False]] | Omit = omit,
        stream_mode: Literal["full", "concise"] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        thread_id: Optional[str] | Omit = omit,
        tool_choice: Optional[Literal["none", "auto", "required"]] | Omit = omit,
        tools: Optional[Iterable[completion_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        updated_after_timestamp: Optional[int] | Omit = omit,
        updated_before_timestamp: Optional[int] | Omit = omit,
        use_threads: Optional[bool] | Omit = omit,
        user_original_query: Optional[str] | Omit = omit,
        web_search_options: WebSearchOptions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamChunk:
        """
        Generate a chat completion response for the given conversation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        messages: Iterable[ChatMessageInput],
        model: str,
        stream: Literal[True],
        _debug_pro_search: bool | Omit = omit,
        _force_new_agent: Optional[bool] | Omit = omit,
        _inputs: Optional[Iterable[int]] | Omit = omit,
        _prompt_token_length: Optional[int] | Omit = omit,
        best_of: Optional[int] | Omit = omit,
        country: Optional[str] | Omit = omit,
        cum_logprobs: Optional[bool] | Omit = omit,
        disable_search: Optional[bool] | Omit = omit,
        diverse_first_token: Optional[bool] | Omit = omit,
        enable_search_classifier: Optional[bool] | Omit = omit,
        file_workspace_id: Optional[str] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        has_image_url: bool | Omit = omit,
        image_domain_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        image_format_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        language_preference: Optional[str] | Omit = omit,
        last_updated_after_filter: Optional[str] | Omit = omit,
        last_updated_before_filter: Optional[str] | Omit = omit,
        latitude: Optional[float] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        longitude: Optional[float] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        n: Optional[int] | Omit = omit,
        num_images: int | Omit = omit,
        num_search_results: int | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        ranking_model: Optional[str] | Omit = omit,
        reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]] | Omit = omit,
        response_format: Optional[completion_create_params.ResponseFormat] | Omit = omit,
        response_metadata: Optional[Dict[str, object]] | Omit = omit,
        return_images: Optional[bool] | Omit = omit,
        return_related_questions: Optional[bool] | Omit = omit,
        safe_search: Optional[bool] | Omit = omit,
        search_after_date_filter: Optional[str] | Omit = omit,
        search_before_date_filter: Optional[str] | Omit = omit,
        search_domain_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        search_internal_properties: Optional[Dict[str, object]] | Omit = omit,
        search_language_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        search_mode: Optional[Literal["web", "academic", "sec"]] | Omit = omit,
        search_recency_filter: Optional[Literal["hour", "day", "week", "month", "year"]] | Omit = omit,
        search_tenant: Optional[str] | Omit = omit,
        stop: Union[str, SequenceNotStr[str], None] | Omit = omit,
        stream_mode: Literal["full", "concise"] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        thread_id: Optional[str] | Omit = omit,
        tool_choice: Optional[Literal["none", "auto", "required"]] | Omit = omit,
        tools: Optional[Iterable[completion_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        updated_after_timestamp: Optional[int] | Omit = omit,
        updated_before_timestamp: Optional[int] | Omit = omit,
        use_threads: Optional[bool] | Omit = omit,
        user_original_query: Optional[str] | Omit = omit,
        web_search_options: WebSearchOptions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[StreamChunk]:
        """
        Generate a chat completion response for the given conversation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        messages: Iterable[ChatMessageInput],
        model: str,
        stream: bool,
        _debug_pro_search: bool | Omit = omit,
        _force_new_agent: Optional[bool] | Omit = omit,
        _inputs: Optional[Iterable[int]] | Omit = omit,
        _prompt_token_length: Optional[int] | Omit = omit,
        best_of: Optional[int] | Omit = omit,
        country: Optional[str] | Omit = omit,
        cum_logprobs: Optional[bool] | Omit = omit,
        disable_search: Optional[bool] | Omit = omit,
        diverse_first_token: Optional[bool] | Omit = omit,
        enable_search_classifier: Optional[bool] | Omit = omit,
        file_workspace_id: Optional[str] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        has_image_url: bool | Omit = omit,
        image_domain_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        image_format_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        language_preference: Optional[str] | Omit = omit,
        last_updated_after_filter: Optional[str] | Omit = omit,
        last_updated_before_filter: Optional[str] | Omit = omit,
        latitude: Optional[float] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        longitude: Optional[float] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        n: Optional[int] | Omit = omit,
        num_images: int | Omit = omit,
        num_search_results: int | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        ranking_model: Optional[str] | Omit = omit,
        reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]] | Omit = omit,
        response_format: Optional[completion_create_params.ResponseFormat] | Omit = omit,
        response_metadata: Optional[Dict[str, object]] | Omit = omit,
        return_images: Optional[bool] | Omit = omit,
        return_related_questions: Optional[bool] | Omit = omit,
        safe_search: Optional[bool] | Omit = omit,
        search_after_date_filter: Optional[str] | Omit = omit,
        search_before_date_filter: Optional[str] | Omit = omit,
        search_domain_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        search_internal_properties: Optional[Dict[str, object]] | Omit = omit,
        search_language_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        search_mode: Optional[Literal["web", "academic", "sec"]] | Omit = omit,
        search_recency_filter: Optional[Literal["hour", "day", "week", "month", "year"]] | Omit = omit,
        search_tenant: Optional[str] | Omit = omit,
        stop: Union[str, SequenceNotStr[str], None] | Omit = omit,
        stream_mode: Literal["full", "concise"] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        thread_id: Optional[str] | Omit = omit,
        tool_choice: Optional[Literal["none", "auto", "required"]] | Omit = omit,
        tools: Optional[Iterable[completion_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        updated_after_timestamp: Optional[int] | Omit = omit,
        updated_before_timestamp: Optional[int] | Omit = omit,
        use_threads: Optional[bool] | Omit = omit,
        user_original_query: Optional[str] | Omit = omit,
        web_search_options: WebSearchOptions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamChunk | Stream[StreamChunk]:
        """
        Generate a chat completion response for the given conversation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["messages", "model"], ["messages", "model", "stream"])
    def create(
        self,
        *,
        messages: Iterable[ChatMessageInput],
        model: str,
        _debug_pro_search: bool | Omit = omit,
        _force_new_agent: Optional[bool] | Omit = omit,
        _inputs: Optional[Iterable[int]] | Omit = omit,
        _prompt_token_length: Optional[int] | Omit = omit,
        best_of: Optional[int] | Omit = omit,
        country: Optional[str] | Omit = omit,
        cum_logprobs: Optional[bool] | Omit = omit,
        disable_search: Optional[bool] | Omit = omit,
        diverse_first_token: Optional[bool] | Omit = omit,
        enable_search_classifier: Optional[bool] | Omit = omit,
        file_workspace_id: Optional[str] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        has_image_url: bool | Omit = omit,
        image_domain_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        image_format_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        language_preference: Optional[str] | Omit = omit,
        last_updated_after_filter: Optional[str] | Omit = omit,
        last_updated_before_filter: Optional[str] | Omit = omit,
        latitude: Optional[float] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        longitude: Optional[float] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        n: Optional[int] | Omit = omit,
        num_images: int | Omit = omit,
        num_search_results: int | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        ranking_model: Optional[str] | Omit = omit,
        reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]] | Omit = omit,
        response_format: Optional[completion_create_params.ResponseFormat] | Omit = omit,
        response_metadata: Optional[Dict[str, object]] | Omit = omit,
        return_images: Optional[bool] | Omit = omit,
        return_related_questions: Optional[bool] | Omit = omit,
        safe_search: Optional[bool] | Omit = omit,
        search_after_date_filter: Optional[str] | Omit = omit,
        search_before_date_filter: Optional[str] | Omit = omit,
        search_domain_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        search_internal_properties: Optional[Dict[str, object]] | Omit = omit,
        search_language_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        search_mode: Optional[Literal["web", "academic", "sec"]] | Omit = omit,
        search_recency_filter: Optional[Literal["hour", "day", "week", "month", "year"]] | Omit = omit,
        search_tenant: Optional[str] | Omit = omit,
        stop: Union[str, SequenceNotStr[str], None] | Omit = omit,
        stream: Optional[Literal[False]] | Literal[True] | Omit = omit,
        stream_mode: Literal["full", "concise"] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        thread_id: Optional[str] | Omit = omit,
        tool_choice: Optional[Literal["none", "auto", "required"]] | Omit = omit,
        tools: Optional[Iterable[completion_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        updated_after_timestamp: Optional[int] | Omit = omit,
        updated_before_timestamp: Optional[int] | Omit = omit,
        use_threads: Optional[bool] | Omit = omit,
        user_original_query: Optional[str] | Omit = omit,
        web_search_options: WebSearchOptions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamChunk | Stream[StreamChunk]:
        return self._post(
            "/chat/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "_debug_pro_search": _debug_pro_search,
                    "_force_new_agent": _force_new_agent,
                    "_inputs": _inputs,
                    "_prompt_token_length": _prompt_token_length,
                    "best_of": best_of,
                    "country": country,
                    "cum_logprobs": cum_logprobs,
                    "disable_search": disable_search,
                    "diverse_first_token": diverse_first_token,
                    "enable_search_classifier": enable_search_classifier,
                    "file_workspace_id": file_workspace_id,
                    "frequency_penalty": frequency_penalty,
                    "has_image_url": has_image_url,
                    "image_domain_filter": image_domain_filter,
                    "image_format_filter": image_format_filter,
                    "language_preference": language_preference,
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
                    "search_language_filter": search_language_filter,
                    "search_mode": search_mode,
                    "search_recency_filter": search_recency_filter,
                    "search_tenant": search_tenant,
                    "stop": stop,
                    "stream": stream,
                    "stream_mode": stream_mode,
                    "temperature": temperature,
                    "thread_id": thread_id,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "updated_after_timestamp": updated_after_timestamp,
                    "updated_before_timestamp": updated_before_timestamp,
                    "use_threads": use_threads,
                    "user_original_query": user_original_query,
                    "web_search_options": web_search_options,
                },
                completion_create_params.CompletionCreateParamsStreaming
                if stream
                else completion_create_params.CompletionCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StreamChunk,
            stream=stream or False,
            stream_cls=Stream[StreamChunk],
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

    @overload
    async def create(
        self,
        *,
        messages: Iterable[ChatMessageInput],
        model: str,
        _debug_pro_search: bool | Omit = omit,
        _force_new_agent: Optional[bool] | Omit = omit,
        _inputs: Optional[Iterable[int]] | Omit = omit,
        _prompt_token_length: Optional[int] | Omit = omit,
        best_of: Optional[int] | Omit = omit,
        country: Optional[str] | Omit = omit,
        cum_logprobs: Optional[bool] | Omit = omit,
        disable_search: Optional[bool] | Omit = omit,
        diverse_first_token: Optional[bool] | Omit = omit,
        enable_search_classifier: Optional[bool] | Omit = omit,
        file_workspace_id: Optional[str] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        has_image_url: bool | Omit = omit,
        image_domain_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        image_format_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        language_preference: Optional[str] | Omit = omit,
        last_updated_after_filter: Optional[str] | Omit = omit,
        last_updated_before_filter: Optional[str] | Omit = omit,
        latitude: Optional[float] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        longitude: Optional[float] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        n: Optional[int] | Omit = omit,
        num_images: int | Omit = omit,
        num_search_results: int | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        ranking_model: Optional[str] | Omit = omit,
        reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]] | Omit = omit,
        response_format: Optional[completion_create_params.ResponseFormat] | Omit = omit,
        response_metadata: Optional[Dict[str, object]] | Omit = omit,
        return_images: Optional[bool] | Omit = omit,
        return_related_questions: Optional[bool] | Omit = omit,
        safe_search: Optional[bool] | Omit = omit,
        search_after_date_filter: Optional[str] | Omit = omit,
        search_before_date_filter: Optional[str] | Omit = omit,
        search_domain_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        search_internal_properties: Optional[Dict[str, object]] | Omit = omit,
        search_language_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        search_mode: Optional[Literal["web", "academic", "sec"]] | Omit = omit,
        search_recency_filter: Optional[Literal["hour", "day", "week", "month", "year"]] | Omit = omit,
        search_tenant: Optional[str] | Omit = omit,
        stop: Union[str, SequenceNotStr[str], None] | Omit = omit,
        stream: Optional[Literal[False]] | Omit = omit,
        stream_mode: Literal["full", "concise"] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        thread_id: Optional[str] | Omit = omit,
        tool_choice: Optional[Literal["none", "auto", "required"]] | Omit = omit,
        tools: Optional[Iterable[completion_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        updated_after_timestamp: Optional[int] | Omit = omit,
        updated_before_timestamp: Optional[int] | Omit = omit,
        use_threads: Optional[bool] | Omit = omit,
        user_original_query: Optional[str] | Omit = omit,
        web_search_options: WebSearchOptions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamChunk:
        """
        Generate a chat completion response for the given conversation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        messages: Iterable[ChatMessageInput],
        model: str,
        stream: Literal[True],
        _debug_pro_search: bool | Omit = omit,
        _force_new_agent: Optional[bool] | Omit = omit,
        _inputs: Optional[Iterable[int]] | Omit = omit,
        _prompt_token_length: Optional[int] | Omit = omit,
        best_of: Optional[int] | Omit = omit,
        country: Optional[str] | Omit = omit,
        cum_logprobs: Optional[bool] | Omit = omit,
        disable_search: Optional[bool] | Omit = omit,
        diverse_first_token: Optional[bool] | Omit = omit,
        enable_search_classifier: Optional[bool] | Omit = omit,
        file_workspace_id: Optional[str] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        has_image_url: bool | Omit = omit,
        image_domain_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        image_format_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        language_preference: Optional[str] | Omit = omit,
        last_updated_after_filter: Optional[str] | Omit = omit,
        last_updated_before_filter: Optional[str] | Omit = omit,
        latitude: Optional[float] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        longitude: Optional[float] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        n: Optional[int] | Omit = omit,
        num_images: int | Omit = omit,
        num_search_results: int | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        ranking_model: Optional[str] | Omit = omit,
        reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]] | Omit = omit,
        response_format: Optional[completion_create_params.ResponseFormat] | Omit = omit,
        response_metadata: Optional[Dict[str, object]] | Omit = omit,
        return_images: Optional[bool] | Omit = omit,
        return_related_questions: Optional[bool] | Omit = omit,
        safe_search: Optional[bool] | Omit = omit,
        search_after_date_filter: Optional[str] | Omit = omit,
        search_before_date_filter: Optional[str] | Omit = omit,
        search_domain_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        search_internal_properties: Optional[Dict[str, object]] | Omit = omit,
        search_language_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        search_mode: Optional[Literal["web", "academic", "sec"]] | Omit = omit,
        search_recency_filter: Optional[Literal["hour", "day", "week", "month", "year"]] | Omit = omit,
        search_tenant: Optional[str] | Omit = omit,
        stop: Union[str, SequenceNotStr[str], None] | Omit = omit,
        stream_mode: Literal["full", "concise"] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        thread_id: Optional[str] | Omit = omit,
        tool_choice: Optional[Literal["none", "auto", "required"]] | Omit = omit,
        tools: Optional[Iterable[completion_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        updated_after_timestamp: Optional[int] | Omit = omit,
        updated_before_timestamp: Optional[int] | Omit = omit,
        use_threads: Optional[bool] | Omit = omit,
        user_original_query: Optional[str] | Omit = omit,
        web_search_options: WebSearchOptions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[StreamChunk]:
        """
        Generate a chat completion response for the given conversation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        messages: Iterable[ChatMessageInput],
        model: str,
        stream: bool,
        _debug_pro_search: bool | Omit = omit,
        _force_new_agent: Optional[bool] | Omit = omit,
        _inputs: Optional[Iterable[int]] | Omit = omit,
        _prompt_token_length: Optional[int] | Omit = omit,
        best_of: Optional[int] | Omit = omit,
        country: Optional[str] | Omit = omit,
        cum_logprobs: Optional[bool] | Omit = omit,
        disable_search: Optional[bool] | Omit = omit,
        diverse_first_token: Optional[bool] | Omit = omit,
        enable_search_classifier: Optional[bool] | Omit = omit,
        file_workspace_id: Optional[str] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        has_image_url: bool | Omit = omit,
        image_domain_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        image_format_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        language_preference: Optional[str] | Omit = omit,
        last_updated_after_filter: Optional[str] | Omit = omit,
        last_updated_before_filter: Optional[str] | Omit = omit,
        latitude: Optional[float] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        longitude: Optional[float] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        n: Optional[int] | Omit = omit,
        num_images: int | Omit = omit,
        num_search_results: int | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        ranking_model: Optional[str] | Omit = omit,
        reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]] | Omit = omit,
        response_format: Optional[completion_create_params.ResponseFormat] | Omit = omit,
        response_metadata: Optional[Dict[str, object]] | Omit = omit,
        return_images: Optional[bool] | Omit = omit,
        return_related_questions: Optional[bool] | Omit = omit,
        safe_search: Optional[bool] | Omit = omit,
        search_after_date_filter: Optional[str] | Omit = omit,
        search_before_date_filter: Optional[str] | Omit = omit,
        search_domain_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        search_internal_properties: Optional[Dict[str, object]] | Omit = omit,
        search_language_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        search_mode: Optional[Literal["web", "academic", "sec"]] | Omit = omit,
        search_recency_filter: Optional[Literal["hour", "day", "week", "month", "year"]] | Omit = omit,
        search_tenant: Optional[str] | Omit = omit,
        stop: Union[str, SequenceNotStr[str], None] | Omit = omit,
        stream_mode: Literal["full", "concise"] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        thread_id: Optional[str] | Omit = omit,
        tool_choice: Optional[Literal["none", "auto", "required"]] | Omit = omit,
        tools: Optional[Iterable[completion_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        updated_after_timestamp: Optional[int] | Omit = omit,
        updated_before_timestamp: Optional[int] | Omit = omit,
        use_threads: Optional[bool] | Omit = omit,
        user_original_query: Optional[str] | Omit = omit,
        web_search_options: WebSearchOptions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamChunk | AsyncStream[StreamChunk]:
        """
        Generate a chat completion response for the given conversation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["messages", "model"], ["messages", "model", "stream"])
    async def create(
        self,
        *,
        messages: Iterable[ChatMessageInput],
        model: str,
        _debug_pro_search: bool | Omit = omit,
        _force_new_agent: Optional[bool] | Omit = omit,
        _inputs: Optional[Iterable[int]] | Omit = omit,
        _prompt_token_length: Optional[int] | Omit = omit,
        best_of: Optional[int] | Omit = omit,
        country: Optional[str] | Omit = omit,
        cum_logprobs: Optional[bool] | Omit = omit,
        disable_search: Optional[bool] | Omit = omit,
        diverse_first_token: Optional[bool] | Omit = omit,
        enable_search_classifier: Optional[bool] | Omit = omit,
        file_workspace_id: Optional[str] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        has_image_url: bool | Omit = omit,
        image_domain_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        image_format_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        language_preference: Optional[str] | Omit = omit,
        last_updated_after_filter: Optional[str] | Omit = omit,
        last_updated_before_filter: Optional[str] | Omit = omit,
        latitude: Optional[float] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        longitude: Optional[float] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        n: Optional[int] | Omit = omit,
        num_images: int | Omit = omit,
        num_search_results: int | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        ranking_model: Optional[str] | Omit = omit,
        reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]] | Omit = omit,
        response_format: Optional[completion_create_params.ResponseFormat] | Omit = omit,
        response_metadata: Optional[Dict[str, object]] | Omit = omit,
        return_images: Optional[bool] | Omit = omit,
        return_related_questions: Optional[bool] | Omit = omit,
        safe_search: Optional[bool] | Omit = omit,
        search_after_date_filter: Optional[str] | Omit = omit,
        search_before_date_filter: Optional[str] | Omit = omit,
        search_domain_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        search_internal_properties: Optional[Dict[str, object]] | Omit = omit,
        search_language_filter: Optional[SequenceNotStr[str]] | Omit = omit,
        search_mode: Optional[Literal["web", "academic", "sec"]] | Omit = omit,
        search_recency_filter: Optional[Literal["hour", "day", "week", "month", "year"]] | Omit = omit,
        search_tenant: Optional[str] | Omit = omit,
        stop: Union[str, SequenceNotStr[str], None] | Omit = omit,
        stream: Optional[Literal[False]] | Literal[True] | Omit = omit,
        stream_mode: Literal["full", "concise"] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        thread_id: Optional[str] | Omit = omit,
        tool_choice: Optional[Literal["none", "auto", "required"]] | Omit = omit,
        tools: Optional[Iterable[completion_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        updated_after_timestamp: Optional[int] | Omit = omit,
        updated_before_timestamp: Optional[int] | Omit = omit,
        use_threads: Optional[bool] | Omit = omit,
        user_original_query: Optional[str] | Omit = omit,
        web_search_options: WebSearchOptions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamChunk | AsyncStream[StreamChunk]:
        return await self._post(
            "/chat/completions",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "_debug_pro_search": _debug_pro_search,
                    "_force_new_agent": _force_new_agent,
                    "_inputs": _inputs,
                    "_prompt_token_length": _prompt_token_length,
                    "best_of": best_of,
                    "country": country,
                    "cum_logprobs": cum_logprobs,
                    "disable_search": disable_search,
                    "diverse_first_token": diverse_first_token,
                    "enable_search_classifier": enable_search_classifier,
                    "file_workspace_id": file_workspace_id,
                    "frequency_penalty": frequency_penalty,
                    "has_image_url": has_image_url,
                    "image_domain_filter": image_domain_filter,
                    "image_format_filter": image_format_filter,
                    "language_preference": language_preference,
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
                    "search_language_filter": search_language_filter,
                    "search_mode": search_mode,
                    "search_recency_filter": search_recency_filter,
                    "search_tenant": search_tenant,
                    "stop": stop,
                    "stream": stream,
                    "stream_mode": stream_mode,
                    "temperature": temperature,
                    "thread_id": thread_id,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "updated_after_timestamp": updated_after_timestamp,
                    "updated_before_timestamp": updated_before_timestamp,
                    "use_threads": use_threads,
                    "user_original_query": user_original_query,
                    "web_search_options": web_search_options,
                },
                completion_create_params.CompletionCreateParamsStreaming
                if stream
                else completion_create_params.CompletionCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StreamChunk,
            stream=stream or False,
            stream_cls=AsyncStream[StreamChunk],
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
