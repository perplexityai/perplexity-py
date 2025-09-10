# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from perplexity import Perplexity, AsyncPerplexity
from tests.utils import assert_matches_type
from perplexity.types.async_.chat import (
    CompletionGetResponse,
    CompletionListResponse,
    CompletionCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Perplexity) -> None:
        completion = client.async_.chat.completions.create(
            request={
                "messages": [
                    {
                        "content": "string",
                        "role": "system",
                    }
                ],
                "model": "sonar",
            },
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Perplexity) -> None:
        completion = client.async_.chat.completions.create(
            request={
                "messages": [
                    {
                        "content": "string",
                        "role": "system",
                    }
                ],
                "model": "sonar",
                "disable_search": True,
                "enable_search_classifier": True,
                "last_updated_after_filter": "last_updated_after_filter",
                "last_updated_before_filter": "last_updated_before_filter",
                "reasoning_effort": "low",
                "return_images": True,
                "return_related_questions": True,
                "search_after_date_filter": "search_after_date_filter",
                "search_before_date_filter": "search_before_date_filter",
                "search_domain_filter": ["string"],
                "search_mode": "web",
                "search_recency_filter": "hour",
                "web_search_options": {
                    "image_search_relevance_enhanced": True,
                    "search_context_size": "low",
                    "user_location": {
                        "city": "city",
                        "country": "country",
                        "latitude": 0,
                        "longitude": 0,
                        "region": "region",
                    },
                },
            },
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Perplexity) -> None:
        response = client.async_.chat.completions.with_raw_response.create(
            request={
                "messages": [
                    {
                        "content": "string",
                        "role": "system",
                    }
                ],
                "model": "sonar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Perplexity) -> None:
        with client.async_.chat.completions.with_streaming_response.create(
            request={
                "messages": [
                    {
                        "content": "string",
                        "role": "system",
                    }
                ],
                "model": "sonar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Perplexity) -> None:
        completion = client.async_.chat.completions.list()
        assert_matches_type(CompletionListResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Perplexity) -> None:
        completion = client.async_.chat.completions.list(
            limit=0,
            next_token="next_token",
        )
        assert_matches_type(CompletionListResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Perplexity) -> None:
        response = client.async_.chat.completions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(CompletionListResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Perplexity) -> None:
        with client.async_.chat.completions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(CompletionListResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Perplexity) -> None:
        completion = client.async_.chat.completions.get(
            "request_id",
        )
        assert_matches_type(CompletionGetResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Perplexity) -> None:
        response = client.async_.chat.completions.with_raw_response.get(
            "request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(CompletionGetResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Perplexity) -> None:
        with client.async_.chat.completions.with_streaming_response.get(
            "request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(CompletionGetResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Perplexity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.async_.chat.completions.with_raw_response.get(
                "",
            )


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPerplexity) -> None:
        completion = await async_client.async_.chat.completions.create(
            request={
                "messages": [
                    {
                        "content": "string",
                        "role": "system",
                    }
                ],
                "model": "sonar",
            },
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPerplexity) -> None:
        completion = await async_client.async_.chat.completions.create(
            request={
                "messages": [
                    {
                        "content": "string",
                        "role": "system",
                    }
                ],
                "model": "sonar",
                "disable_search": True,
                "enable_search_classifier": True,
                "last_updated_after_filter": "last_updated_after_filter",
                "last_updated_before_filter": "last_updated_before_filter",
                "reasoning_effort": "low",
                "return_images": True,
                "return_related_questions": True,
                "search_after_date_filter": "search_after_date_filter",
                "search_before_date_filter": "search_before_date_filter",
                "search_domain_filter": ["string"],
                "search_mode": "web",
                "search_recency_filter": "hour",
                "web_search_options": {
                    "image_search_relevance_enhanced": True,
                    "search_context_size": "low",
                    "user_location": {
                        "city": "city",
                        "country": "country",
                        "latitude": 0,
                        "longitude": 0,
                        "region": "region",
                    },
                },
            },
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPerplexity) -> None:
        response = await async_client.async_.chat.completions.with_raw_response.create(
            request={
                "messages": [
                    {
                        "content": "string",
                        "role": "system",
                    }
                ],
                "model": "sonar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPerplexity) -> None:
        async with async_client.async_.chat.completions.with_streaming_response.create(
            request={
                "messages": [
                    {
                        "content": "string",
                        "role": "system",
                    }
                ],
                "model": "sonar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPerplexity) -> None:
        completion = await async_client.async_.chat.completions.list()
        assert_matches_type(CompletionListResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPerplexity) -> None:
        completion = await async_client.async_.chat.completions.list(
            limit=0,
            next_token="next_token",
        )
        assert_matches_type(CompletionListResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPerplexity) -> None:
        response = await async_client.async_.chat.completions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(CompletionListResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPerplexity) -> None:
        async with async_client.async_.chat.completions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(CompletionListResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncPerplexity) -> None:
        completion = await async_client.async_.chat.completions.get(
            "request_id",
        )
        assert_matches_type(CompletionGetResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPerplexity) -> None:
        response = await async_client.async_.chat.completions.with_raw_response.get(
            "request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(CompletionGetResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPerplexity) -> None:
        async with async_client.async_.chat.completions.with_streaming_response.get(
            "request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(CompletionGetResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncPerplexity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.async_.chat.completions.with_raw_response.get(
                "",
            )
