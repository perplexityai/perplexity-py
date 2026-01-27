# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, overload

import httpx

from ..types import response_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._streaming import Stream, AsyncStream
from .._base_client import make_request_options
from ..types.input_item_param import InputItemParam
from ..types.response_stream_chunk import ResponseStreamChunk
from ..types.response_create_response import ResponseCreateResponse
from ..types.shared_params.response_format import ResponseFormat

__all__ = ["ResponsesResource", "AsyncResponsesResource"]


class ResponsesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return ResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return ResponsesResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        input: Union[str, Iterable[InputItemParam]],
        instructions: str | Omit = omit,
        language_preference: str | Omit = omit,
        max_output_tokens: int | Omit = omit,
        max_steps: int | Omit = omit,
        model: str | Omit = omit,
        models: SequenceNotStr[str] | Omit = omit,
        preset: str | Omit = omit,
        reasoning: response_create_params.Reasoning | Omit = omit,
        response_format: ResponseFormat | Omit = omit,
        stream: Literal[False] | Omit = omit,
        tools: Iterable[response_create_params.Tool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse:
        """
        Generate a response for the provided input with optional web search and
        reasoning.

        Args:
          input: Input content - either a string or array of input items

          instructions: System instructions for the model

          language_preference: ISO 639-1 language code for response language

          max_output_tokens: Maximum tokens to generate

          max_steps: Maximum number of research loop steps. If provided, overrides the preset's
              max_steps value. Must be >= 1 if specified. Maximum allowed is 10.

          model: Model ID in provider/model format (e.g., "xai/grok-4-1", "openai/gpt-4o"). If
              models is also provided, models takes precedence. Required if neither models nor
              preset is provided.

          models: Model fallback chain. Each model is in provider/model format. Models are tried
              in order until one succeeds. Max 5 models allowed. If set, takes precedence over
              single model field. The response.model will reflect the model that actually
              succeeded.

          preset: Preset configuration name (e.g., "sonar-pro", "sonar-reasoning"). Pre-configured
              model with system prompt and search parameters. Required if model is not
              provided.

          response_format: Specifies the desired output format for the model response

          stream: If true, returns SSE stream instead of JSON

          tools: Tools available to the model

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
        input: Union[str, Iterable[InputItemParam]],
        stream: Literal[True],
        instructions: str | Omit = omit,
        language_preference: str | Omit = omit,
        max_output_tokens: int | Omit = omit,
        max_steps: int | Omit = omit,
        model: str | Omit = omit,
        models: SequenceNotStr[str] | Omit = omit,
        preset: str | Omit = omit,
        reasoning: response_create_params.Reasoning | Omit = omit,
        response_format: ResponseFormat | Omit = omit,
        tools: Iterable[response_create_params.Tool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ResponseStreamChunk]:
        """
        Generate a response for the provided input with optional web search and
        reasoning.

        Args:
          input: Input content - either a string or array of input items

          stream: If true, returns SSE stream instead of JSON

          instructions: System instructions for the model

          language_preference: ISO 639-1 language code for response language

          max_output_tokens: Maximum tokens to generate

          max_steps: Maximum number of research loop steps. If provided, overrides the preset's
              max_steps value. Must be >= 1 if specified. Maximum allowed is 10.

          model: Model ID in provider/model format (e.g., "xai/grok-4-1", "openai/gpt-4o"). If
              models is also provided, models takes precedence. Required if neither models nor
              preset is provided.

          models: Model fallback chain. Each model is in provider/model format. Models are tried
              in order until one succeeds. Max 5 models allowed. If set, takes precedence over
              single model field. The response.model will reflect the model that actually
              succeeded.

          preset: Preset configuration name (e.g., "sonar-pro", "sonar-reasoning"). Pre-configured
              model with system prompt and search parameters. Required if model is not
              provided.

          response_format: Specifies the desired output format for the model response

          tools: Tools available to the model

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
        input: Union[str, Iterable[InputItemParam]],
        stream: bool,
        instructions: str | Omit = omit,
        language_preference: str | Omit = omit,
        max_output_tokens: int | Omit = omit,
        max_steps: int | Omit = omit,
        model: str | Omit = omit,
        models: SequenceNotStr[str] | Omit = omit,
        preset: str | Omit = omit,
        reasoning: response_create_params.Reasoning | Omit = omit,
        response_format: ResponseFormat | Omit = omit,
        tools: Iterable[response_create_params.Tool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse | Stream[ResponseStreamChunk]:
        """
        Generate a response for the provided input with optional web search and
        reasoning.

        Args:
          input: Input content - either a string or array of input items

          stream: If true, returns SSE stream instead of JSON

          instructions: System instructions for the model

          language_preference: ISO 639-1 language code for response language

          max_output_tokens: Maximum tokens to generate

          max_steps: Maximum number of research loop steps. If provided, overrides the preset's
              max_steps value. Must be >= 1 if specified. Maximum allowed is 10.

          model: Model ID in provider/model format (e.g., "xai/grok-4-1", "openai/gpt-4o"). If
              models is also provided, models takes precedence. Required if neither models nor
              preset is provided.

          models: Model fallback chain. Each model is in provider/model format. Models are tried
              in order until one succeeds. Max 5 models allowed. If set, takes precedence over
              single model field. The response.model will reflect the model that actually
              succeeded.

          preset: Preset configuration name (e.g., "sonar-pro", "sonar-reasoning"). Pre-configured
              model with system prompt and search parameters. Required if model is not
              provided.

          response_format: Specifies the desired output format for the model response

          tools: Tools available to the model

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["input"], ["input", "stream"])
    def create(
        self,
        *,
        input: Union[str, Iterable[InputItemParam]],
        instructions: str | Omit = omit,
        language_preference: str | Omit = omit,
        max_output_tokens: int | Omit = omit,
        max_steps: int | Omit = omit,
        model: str | Omit = omit,
        models: SequenceNotStr[str] | Omit = omit,
        preset: str | Omit = omit,
        reasoning: response_create_params.Reasoning | Omit = omit,
        response_format: ResponseFormat | Omit = omit,
        stream: Literal[False] | Literal[True] | Omit = omit,
        tools: Iterable[response_create_params.Tool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse | Stream[ResponseStreamChunk]:
        return self._post(
            "/v1/responses",
            body=maybe_transform(
                {
                    "input": input,
                    "instructions": instructions,
                    "language_preference": language_preference,
                    "max_output_tokens": max_output_tokens,
                    "max_steps": max_steps,
                    "model": model,
                    "models": models,
                    "preset": preset,
                    "reasoning": reasoning,
                    "response_format": response_format,
                    "stream": stream,
                    "tools": tools,
                },
                response_create_params.ResponseCreateParamsStreaming
                if stream
                else response_create_params.ResponseCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseCreateResponse,
            stream=stream or False,
            stream_cls=Stream[ResponseStreamChunk],
        )


class AsyncResponsesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return AsyncResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return AsyncResponsesResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        input: Union[str, Iterable[InputItemParam]],
        instructions: str | Omit = omit,
        language_preference: str | Omit = omit,
        max_output_tokens: int | Omit = omit,
        max_steps: int | Omit = omit,
        model: str | Omit = omit,
        models: SequenceNotStr[str] | Omit = omit,
        preset: str | Omit = omit,
        reasoning: response_create_params.Reasoning | Omit = omit,
        response_format: ResponseFormat | Omit = omit,
        stream: Literal[False] | Omit = omit,
        tools: Iterable[response_create_params.Tool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse:
        """
        Generate a response for the provided input with optional web search and
        reasoning.

        Args:
          input: Input content - either a string or array of input items

          instructions: System instructions for the model

          language_preference: ISO 639-1 language code for response language

          max_output_tokens: Maximum tokens to generate

          max_steps: Maximum number of research loop steps. If provided, overrides the preset's
              max_steps value. Must be >= 1 if specified. Maximum allowed is 10.

          model: Model ID in provider/model format (e.g., "xai/grok-4-1", "openai/gpt-4o"). If
              models is also provided, models takes precedence. Required if neither models nor
              preset is provided.

          models: Model fallback chain. Each model is in provider/model format. Models are tried
              in order until one succeeds. Max 5 models allowed. If set, takes precedence over
              single model field. The response.model will reflect the model that actually
              succeeded.

          preset: Preset configuration name (e.g., "sonar-pro", "sonar-reasoning"). Pre-configured
              model with system prompt and search parameters. Required if model is not
              provided.

          response_format: Specifies the desired output format for the model response

          stream: If true, returns SSE stream instead of JSON

          tools: Tools available to the model

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
        input: Union[str, Iterable[InputItemParam]],
        stream: Literal[True],
        instructions: str | Omit = omit,
        language_preference: str | Omit = omit,
        max_output_tokens: int | Omit = omit,
        max_steps: int | Omit = omit,
        model: str | Omit = omit,
        models: SequenceNotStr[str] | Omit = omit,
        preset: str | Omit = omit,
        reasoning: response_create_params.Reasoning | Omit = omit,
        response_format: ResponseFormat | Omit = omit,
        tools: Iterable[response_create_params.Tool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ResponseStreamChunk]:
        """
        Generate a response for the provided input with optional web search and
        reasoning.

        Args:
          input: Input content - either a string or array of input items

          stream: If true, returns SSE stream instead of JSON

          instructions: System instructions for the model

          language_preference: ISO 639-1 language code for response language

          max_output_tokens: Maximum tokens to generate

          max_steps: Maximum number of research loop steps. If provided, overrides the preset's
              max_steps value. Must be >= 1 if specified. Maximum allowed is 10.

          model: Model ID in provider/model format (e.g., "xai/grok-4-1", "openai/gpt-4o"). If
              models is also provided, models takes precedence. Required if neither models nor
              preset is provided.

          models: Model fallback chain. Each model is in provider/model format. Models are tried
              in order until one succeeds. Max 5 models allowed. If set, takes precedence over
              single model field. The response.model will reflect the model that actually
              succeeded.

          preset: Preset configuration name (e.g., "sonar-pro", "sonar-reasoning"). Pre-configured
              model with system prompt and search parameters. Required if model is not
              provided.

          response_format: Specifies the desired output format for the model response

          tools: Tools available to the model

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
        input: Union[str, Iterable[InputItemParam]],
        stream: bool,
        instructions: str | Omit = omit,
        language_preference: str | Omit = omit,
        max_output_tokens: int | Omit = omit,
        max_steps: int | Omit = omit,
        model: str | Omit = omit,
        models: SequenceNotStr[str] | Omit = omit,
        preset: str | Omit = omit,
        reasoning: response_create_params.Reasoning | Omit = omit,
        response_format: ResponseFormat | Omit = omit,
        tools: Iterable[response_create_params.Tool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse | AsyncStream[ResponseStreamChunk]:
        """
        Generate a response for the provided input with optional web search and
        reasoning.

        Args:
          input: Input content - either a string or array of input items

          stream: If true, returns SSE stream instead of JSON

          instructions: System instructions for the model

          language_preference: ISO 639-1 language code for response language

          max_output_tokens: Maximum tokens to generate

          max_steps: Maximum number of research loop steps. If provided, overrides the preset's
              max_steps value. Must be >= 1 if specified. Maximum allowed is 10.

          model: Model ID in provider/model format (e.g., "xai/grok-4-1", "openai/gpt-4o"). If
              models is also provided, models takes precedence. Required if neither models nor
              preset is provided.

          models: Model fallback chain. Each model is in provider/model format. Models are tried
              in order until one succeeds. Max 5 models allowed. If set, takes precedence over
              single model field. The response.model will reflect the model that actually
              succeeded.

          preset: Preset configuration name (e.g., "sonar-pro", "sonar-reasoning"). Pre-configured
              model with system prompt and search parameters. Required if model is not
              provided.

          response_format: Specifies the desired output format for the model response

          tools: Tools available to the model

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["input"], ["input", "stream"])
    async def create(
        self,
        *,
        input: Union[str, Iterable[InputItemParam]],
        instructions: str | Omit = omit,
        language_preference: str | Omit = omit,
        max_output_tokens: int | Omit = omit,
        max_steps: int | Omit = omit,
        model: str | Omit = omit,
        models: SequenceNotStr[str] | Omit = omit,
        preset: str | Omit = omit,
        reasoning: response_create_params.Reasoning | Omit = omit,
        response_format: ResponseFormat | Omit = omit,
        stream: Literal[False] | Literal[True] | Omit = omit,
        tools: Iterable[response_create_params.Tool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse | AsyncStream[ResponseStreamChunk]:
        return await self._post(
            "/v1/responses",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "instructions": instructions,
                    "language_preference": language_preference,
                    "max_output_tokens": max_output_tokens,
                    "max_steps": max_steps,
                    "model": model,
                    "models": models,
                    "preset": preset,
                    "reasoning": reasoning,
                    "response_format": response_format,
                    "stream": stream,
                    "tools": tools,
                },
                response_create_params.ResponseCreateParamsStreaming
                if stream
                else response_create_params.ResponseCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseCreateResponse,
            stream=stream or False,
            stream_cls=AsyncStream[ResponseStreamChunk],
        )


class ResponsesResourceWithRawResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.create = to_raw_response_wrapper(
            responses.create,
        )


class AsyncResponsesResourceWithRawResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.create = async_to_raw_response_wrapper(
            responses.create,
        )


class ResponsesResourceWithStreamingResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.create = to_streamed_response_wrapper(
            responses.create,
        )


class AsyncResponsesResourceWithStreamingResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.create = async_to_streamed_response_wrapper(
            responses.create,
        )
