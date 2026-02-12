# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import contextualized_embedding_create_params
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
from ..types.contextualized_embedding_create_response import ContextualizedEmbeddingCreateResponse

__all__ = ["ContextualizedEmbeddingsResource", "AsyncContextualizedEmbeddingsResource"]


class ContextualizedEmbeddingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContextualizedEmbeddingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return ContextualizedEmbeddingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContextualizedEmbeddingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return ContextualizedEmbeddingsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        input: Iterable[SequenceNotStr[str]],
        model: Literal["pplx-embed-context-v1-0.6b", "pplx-embed-context-v1-4b"],
        dimensions: int | Omit = omit,
        encoding_format: Literal["base64_int8", "base64_binary"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContextualizedEmbeddingCreateResponse:
        """Generate contextualized embeddings for document chunks.

        Chunks from the same
        document share context awareness, improving retrieval quality for document-based
        applications.

        Args:
          input: Nested array structure where each inner array contains chunks from a single
              document. Chunks within the same document are encoded with document-level
              context awareness. Maximum 512 documents. Total chunks across all documents must
              not exceed 16,000. Total tokens per document must not exceed 32K. All chunks in
              a single request must not exceed 120,000 tokens combined. Empty strings are not
              allowed.

          model: The contextualized embedding model to use

          dimensions: Number of dimensions for output embeddings (Matryoshka). Range: 128-1024 for
              pplx-embed-context-v1-0.6b, 128-2560 for pplx-embed-context-v1-4b. Defaults to
              full dimensions (1024 or 2560).

          encoding_format: Output encoding format for embeddings. base64_int8 returns base64-encoded signed
              int8 values. base64_binary returns base64-encoded packed binary (1 bit per
              dimension).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/contextualizedembeddings",
            body=maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "dimensions": dimensions,
                    "encoding_format": encoding_format,
                },
                contextualized_embedding_create_params.ContextualizedEmbeddingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextualizedEmbeddingCreateResponse,
        )


class AsyncContextualizedEmbeddingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContextualizedEmbeddingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/perplexityai/perplexity-py#accessing-raw-response-data-eg-headers
        """
        return AsyncContextualizedEmbeddingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContextualizedEmbeddingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/perplexityai/perplexity-py#with_streaming_response
        """
        return AsyncContextualizedEmbeddingsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        input: Iterable[SequenceNotStr[str]],
        model: Literal["pplx-embed-context-v1-0.6b", "pplx-embed-context-v1-4b"],
        dimensions: int | Omit = omit,
        encoding_format: Literal["base64_int8", "base64_binary"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContextualizedEmbeddingCreateResponse:
        """Generate contextualized embeddings for document chunks.

        Chunks from the same
        document share context awareness, improving retrieval quality for document-based
        applications.

        Args:
          input: Nested array structure where each inner array contains chunks from a single
              document. Chunks within the same document are encoded with document-level
              context awareness. Maximum 512 documents. Total chunks across all documents must
              not exceed 16,000. Total tokens per document must not exceed 32K. All chunks in
              a single request must not exceed 120,000 tokens combined. Empty strings are not
              allowed.

          model: The contextualized embedding model to use

          dimensions: Number of dimensions for output embeddings (Matryoshka). Range: 128-1024 for
              pplx-embed-context-v1-0.6b, 128-2560 for pplx-embed-context-v1-4b. Defaults to
              full dimensions (1024 or 2560).

          encoding_format: Output encoding format for embeddings. base64_int8 returns base64-encoded signed
              int8 values. base64_binary returns base64-encoded packed binary (1 bit per
              dimension).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/contextualizedembeddings",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "dimensions": dimensions,
                    "encoding_format": encoding_format,
                },
                contextualized_embedding_create_params.ContextualizedEmbeddingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextualizedEmbeddingCreateResponse,
        )


class ContextualizedEmbeddingsResourceWithRawResponse:
    def __init__(self, contextualized_embeddings: ContextualizedEmbeddingsResource) -> None:
        self._contextualized_embeddings = contextualized_embeddings

        self.create = to_raw_response_wrapper(
            contextualized_embeddings.create,
        )


class AsyncContextualizedEmbeddingsResourceWithRawResponse:
    def __init__(self, contextualized_embeddings: AsyncContextualizedEmbeddingsResource) -> None:
        self._contextualized_embeddings = contextualized_embeddings

        self.create = async_to_raw_response_wrapper(
            contextualized_embeddings.create,
        )


class ContextualizedEmbeddingsResourceWithStreamingResponse:
    def __init__(self, contextualized_embeddings: ContextualizedEmbeddingsResource) -> None:
        self._contextualized_embeddings = contextualized_embeddings

        self.create = to_streamed_response_wrapper(
            contextualized_embeddings.create,
        )


class AsyncContextualizedEmbeddingsResourceWithStreamingResponse:
    def __init__(self, contextualized_embeddings: AsyncContextualizedEmbeddingsResource) -> None:
        self._contextualized_embeddings = contextualized_embeddings

        self.create = async_to_streamed_response_wrapper(
            contextualized_embeddings.create,
        )
