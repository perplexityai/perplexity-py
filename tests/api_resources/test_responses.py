# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from perplexity import Perplexity, AsyncPerplexity
from tests.utils import assert_matches_type
from perplexity.types import ResponseCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResponses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Perplexity) -> None:
        response = client.responses.create(
            input="string",
        )
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Perplexity) -> None:
        response = client.responses.create(
            input="string",
            instructions="instructions",
            language_preference="language_preference",
            max_output_tokens=1,
            max_steps=1,
            model="model",
            models=["string"],
            preset="preset",
            reasoning={"effort": "low"},
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "x",
                    "schema": {"foo": "bar"},
                    "description": "description",
                    "strict": True,
                },
            },
            stream=False,
            tools=[
                {
                    "type": "web_search",
                    "filters": {
                        "last_updated_after_filter": "last_updated_after_filter",
                        "last_updated_before_filter": "last_updated_before_filter",
                        "search_after_date_filter": "search_after_date_filter",
                        "search_before_date_filter": "search_before_date_filter",
                        "search_domain_filter": ["string"],
                        "search_recency_filter": "hour",
                    },
                    "max_tokens": 0,
                    "max_tokens_per_page": 0,
                    "user_location": {
                        "city": "city",
                        "country": "country",
                        "latitude": 0,
                        "longitude": 0,
                        "region": "region",
                    },
                }
            ],
        )
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Perplexity) -> None:
        http_response = client.responses.with_raw_response.create(
            input="string",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Perplexity) -> None:
        with client.responses.with_streaming_response.create(
            input="string",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert_matches_type(ResponseCreateResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Perplexity) -> None:
        response_stream = client.responses.create(
            input="string",
            stream=True,
        )
        response_stream.response.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Perplexity) -> None:
        response_stream = client.responses.create(
            input="string",
            stream=True,
            instructions="instructions",
            language_preference="language_preference",
            max_output_tokens=1,
            max_steps=1,
            model="model",
            models=["string"],
            preset="preset",
            reasoning={"effort": "low"},
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "x",
                    "schema": {"foo": "bar"},
                    "description": "description",
                    "strict": True,
                },
            },
            tools=[
                {
                    "type": "web_search",
                    "filters": {
                        "last_updated_after_filter": "last_updated_after_filter",
                        "last_updated_before_filter": "last_updated_before_filter",
                        "search_after_date_filter": "search_after_date_filter",
                        "search_before_date_filter": "search_before_date_filter",
                        "search_domain_filter": ["string"],
                        "search_recency_filter": "hour",
                    },
                    "max_tokens": 0,
                    "max_tokens_per_page": 0,
                    "user_location": {
                        "city": "city",
                        "country": "country",
                        "latitude": 0,
                        "longitude": 0,
                        "region": "region",
                    },
                }
            ],
        )
        response_stream.response.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Perplexity) -> None:
        response = client.responses.with_raw_response.create(
            input="string",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Perplexity) -> None:
        with client.responses.with_streaming_response.create(
            input="string",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncResponses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncPerplexity) -> None:
        response = await async_client.responses.create(
            input="string",
        )
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncPerplexity) -> None:
        response = await async_client.responses.create(
            input="string",
            instructions="instructions",
            language_preference="language_preference",
            max_output_tokens=1,
            max_steps=1,
            model="model",
            models=["string"],
            preset="preset",
            reasoning={"effort": "low"},
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "x",
                    "schema": {"foo": "bar"},
                    "description": "description",
                    "strict": True,
                },
            },
            stream=False,
            tools=[
                {
                    "type": "web_search",
                    "filters": {
                        "last_updated_after_filter": "last_updated_after_filter",
                        "last_updated_before_filter": "last_updated_before_filter",
                        "search_after_date_filter": "search_after_date_filter",
                        "search_before_date_filter": "search_before_date_filter",
                        "search_domain_filter": ["string"],
                        "search_recency_filter": "hour",
                    },
                    "max_tokens": 0,
                    "max_tokens_per_page": 0,
                    "user_location": {
                        "city": "city",
                        "country": "country",
                        "latitude": 0,
                        "longitude": 0,
                        "region": "region",
                    },
                }
            ],
        )
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncPerplexity) -> None:
        http_response = await async_client.responses.with_raw_response.create(
            input="string",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = await http_response.parse()
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncPerplexity) -> None:
        async with async_client.responses.with_streaming_response.create(
            input="string",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert_matches_type(ResponseCreateResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncPerplexity) -> None:
        response_stream = await async_client.responses.create(
            input="string",
            stream=True,
        )
        await response_stream.response.aclose()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncPerplexity) -> None:
        response_stream = await async_client.responses.create(
            input="string",
            stream=True,
            instructions="instructions",
            language_preference="language_preference",
            max_output_tokens=1,
            max_steps=1,
            model="model",
            models=["string"],
            preset="preset",
            reasoning={"effort": "low"},
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "x",
                    "schema": {"foo": "bar"},
                    "description": "description",
                    "strict": True,
                },
            },
            tools=[
                {
                    "type": "web_search",
                    "filters": {
                        "last_updated_after_filter": "last_updated_after_filter",
                        "last_updated_before_filter": "last_updated_before_filter",
                        "search_after_date_filter": "search_after_date_filter",
                        "search_before_date_filter": "search_before_date_filter",
                        "search_domain_filter": ["string"],
                        "search_recency_filter": "hour",
                    },
                    "max_tokens": 0,
                    "max_tokens_per_page": 0,
                    "user_location": {
                        "city": "city",
                        "country": "country",
                        "latitude": 0,
                        "longitude": 0,
                        "region": "region",
                    },
                }
            ],
        )
        await response_stream.response.aclose()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncPerplexity) -> None:
        response = await async_client.responses.with_raw_response.create(
            input="string",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncPerplexity) -> None:
        async with async_client.responses.with_streaming_response.create(
            input="string",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
