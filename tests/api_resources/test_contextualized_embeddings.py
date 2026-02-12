# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from perplexity import Perplexity, AsyncPerplexity
from tests.utils import assert_matches_type
from perplexity.types import ContextualizedEmbeddingCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContextualizedEmbeddings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Perplexity) -> None:
        contextualized_embedding = client.contextualized_embeddings.create(
            input=[["x"]],
            model="pplx-embed-context-v1-0.6b",
        )
        assert_matches_type(ContextualizedEmbeddingCreateResponse, contextualized_embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Perplexity) -> None:
        contextualized_embedding = client.contextualized_embeddings.create(
            input=[["x"]],
            model="pplx-embed-context-v1-0.6b",
            dimensions=128,
            encoding_format="base64_int8",
        )
        assert_matches_type(ContextualizedEmbeddingCreateResponse, contextualized_embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Perplexity) -> None:
        response = client.contextualized_embeddings.with_raw_response.create(
            input=[["x"]],
            model="pplx-embed-context-v1-0.6b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contextualized_embedding = response.parse()
        assert_matches_type(ContextualizedEmbeddingCreateResponse, contextualized_embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Perplexity) -> None:
        with client.contextualized_embeddings.with_streaming_response.create(
            input=[["x"]],
            model="pplx-embed-context-v1-0.6b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contextualized_embedding = response.parse()
            assert_matches_type(ContextualizedEmbeddingCreateResponse, contextualized_embedding, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContextualizedEmbeddings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPerplexity) -> None:
        contextualized_embedding = await async_client.contextualized_embeddings.create(
            input=[["x"]],
            model="pplx-embed-context-v1-0.6b",
        )
        assert_matches_type(ContextualizedEmbeddingCreateResponse, contextualized_embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPerplexity) -> None:
        contextualized_embedding = await async_client.contextualized_embeddings.create(
            input=[["x"]],
            model="pplx-embed-context-v1-0.6b",
            dimensions=128,
            encoding_format="base64_int8",
        )
        assert_matches_type(ContextualizedEmbeddingCreateResponse, contextualized_embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPerplexity) -> None:
        response = await async_client.contextualized_embeddings.with_raw_response.create(
            input=[["x"]],
            model="pplx-embed-context-v1-0.6b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contextualized_embedding = await response.parse()
        assert_matches_type(ContextualizedEmbeddingCreateResponse, contextualized_embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPerplexity) -> None:
        async with async_client.contextualized_embeddings.with_streaming_response.create(
            input=[["x"]],
            model="pplx-embed-context-v1-0.6b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contextualized_embedding = await response.parse()
            assert_matches_type(ContextualizedEmbeddingCreateResponse, contextualized_embedding, path=["response"])

        assert cast(Any, response.is_closed) is True
