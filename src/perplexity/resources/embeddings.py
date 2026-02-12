# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal

import httpx

from ..types import embedding_create_params
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
from ..types.embedding_create_response import EmbeddingCreateResponse

__all__ = ["EmbeddingsResource", "AsyncEmbeddingsResource"]


class EmbeddingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmbeddingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return EmbeddingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmbeddingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return EmbeddingsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        input: Union[str, SequenceNotStr[str]],
        model: Literal["pplx-embed-v1-0.6b", "pplx-embed-v1-4b"],
        dimensions: int | Omit = omit,
        encoding_format: Literal["base64_int8", "base64_binary"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmbeddingCreateResponse:
        """Generate embeddings for a list of texts.

        Use these embeddings for semantic
        search, clustering, and other machine learning applications.

        Args:
          input: Input text to embed, encoded as a string or array of strings. Maximum 512 texts
              per request. Each input must not exceed 32K tokens. All inputs in a single
              request must not exceed 120,000 tokens combined. Empty strings are not allowed.

          model: The embedding model to use

          dimensions: Number of dimensions for output embeddings (Matryoshka). Range: 128-1024 for
              pplx-embed-v1-0.6b, 128-2560 for pplx-embed-v1-4b. Defaults to full dimensions
              (1024 or 2560).

          encoding_format: Output encoding format for embeddings. base64_int8 returns base64-encoded signed
              int8 values. base64_binary returns base64-encoded packed binary (1 bit per
              dimension).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/embeddings",
            body=maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "dimensions": dimensions,
                    "encoding_format": encoding_format,
                },
                embedding_create_params.EmbeddingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingCreateResponse,
        )


class AsyncEmbeddingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmbeddingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return AsyncEmbeddingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmbeddingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return AsyncEmbeddingsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        input: Union[str, SequenceNotStr[str]],
        model: Literal["pplx-embed-v1-0.6b", "pplx-embed-v1-4b"],
        dimensions: int | Omit = omit,
        encoding_format: Literal["base64_int8", "base64_binary"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmbeddingCreateResponse:
        """Generate embeddings for a list of texts.

        Use these embeddings for semantic
        search, clustering, and other machine learning applications.

        Args:
          input: Input text to embed, encoded as a string or array of strings. Maximum 512 texts
              per request. Each input must not exceed 32K tokens. All inputs in a single
              request must not exceed 120,000 tokens combined. Empty strings are not allowed.

          model: The embedding model to use

          dimensions: Number of dimensions for output embeddings (Matryoshka). Range: 128-1024 for
              pplx-embed-v1-0.6b, 128-2560 for pplx-embed-v1-4b. Defaults to full dimensions
              (1024 or 2560).

          encoding_format: Output encoding format for embeddings. base64_int8 returns base64-encoded signed
              int8 values. base64_binary returns base64-encoded packed binary (1 bit per
              dimension).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/embeddings",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "dimensions": dimensions,
                    "encoding_format": encoding_format,
                },
                embedding_create_params.EmbeddingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingCreateResponse,
        )


class EmbeddingsResourceWithRawResponse:
    def __init__(self, embeddings: EmbeddingsResource) -> None:
        self._embeddings = embeddings

        self.create = to_raw_response_wrapper(
            embeddings.create,
        )


class AsyncEmbeddingsResourceWithRawResponse:
    def __init__(self, embeddings: AsyncEmbeddingsResource) -> None:
        self._embeddings = embeddings

        self.create = async_to_raw_response_wrapper(
            embeddings.create,
        )


class EmbeddingsResourceWithStreamingResponse:
    def __init__(self, embeddings: EmbeddingsResource) -> None:
        self._embeddings = embeddings

        self.create = to_streamed_response_wrapper(
            embeddings.create,
        )


class AsyncEmbeddingsResourceWithStreamingResponse:
    def __init__(self, embeddings: AsyncEmbeddingsResource) -> None:
        self._embeddings = embeddings

        self.create = async_to_streamed_response_wrapper(
            embeddings.create,
        )
