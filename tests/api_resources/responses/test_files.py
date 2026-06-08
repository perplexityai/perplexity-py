# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from perplexity import Perplexity, AsyncPerplexity
from tests.utils import assert_matches_type
from perplexity.types import ResponseFileList
from perplexity._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Perplexity) -> None:
        file = client.responses.files.list(
            "response_id",
        )
        assert_matches_type(ResponseFileList, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Perplexity) -> None:
        response = client.responses.files.with_raw_response.list(
            "response_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(ResponseFileList, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Perplexity) -> None:
        with client.responses.files.with_streaming_response.list(
            "response_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(ResponseFileList, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Perplexity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            client.responses.files.with_raw_response.list(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_content(self, client: Perplexity, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/responses/response_id/files/file_id/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        file = client.responses.files.content(
            file_id="file_id",
            response_id="response_id",
        )
        assert file.is_closed
        assert file.json() == {"foo": "bar"}
        assert cast(Any, file.is_closed) is True
        assert isinstance(file, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_content(self, client: Perplexity, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/responses/response_id/files/file_id/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        file = client.responses.files.with_raw_response.content(
            file_id="file_id",
            response_id="response_id",
        )

        assert file.is_closed is True
        assert file.http_request.headers.get("X-Stainless-Lang") == "python"
        assert file.json() == {"foo": "bar"}
        assert isinstance(file, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_content(self, client: Perplexity, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/responses/response_id/files/file_id/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.responses.files.with_streaming_response.content(
            file_id="file_id",
            response_id="response_id",
        ) as file:
            assert not file.is_closed
            assert file.http_request.headers.get("X-Stainless-Lang") == "python"

            assert file.json() == {"foo": "bar"}
            assert cast(Any, file.is_closed) is True
            assert isinstance(file, StreamedBinaryAPIResponse)

        assert cast(Any, file.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_content(self, client: Perplexity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            client.responses.files.with_raw_response.content(
                file_id="file_id",
                response_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.responses.files.with_raw_response.content(
                file_id="",
                response_id="response_id",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPerplexity) -> None:
        file = await async_client.responses.files.list(
            "response_id",
        )
        assert_matches_type(ResponseFileList, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPerplexity) -> None:
        response = await async_client.responses.files.with_raw_response.list(
            "response_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(ResponseFileList, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPerplexity) -> None:
        async with async_client.responses.files.with_streaming_response.list(
            "response_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(ResponseFileList, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncPerplexity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            await async_client.responses.files.with_raw_response.list(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_content(self, async_client: AsyncPerplexity, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/responses/response_id/files/file_id/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        file = await async_client.responses.files.content(
            file_id="file_id",
            response_id="response_id",
        )
        assert file.is_closed
        assert await file.json() == {"foo": "bar"}
        assert cast(Any, file.is_closed) is True
        assert isinstance(file, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_content(self, async_client: AsyncPerplexity, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/responses/response_id/files/file_id/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        file = await async_client.responses.files.with_raw_response.content(
            file_id="file_id",
            response_id="response_id",
        )

        assert file.is_closed is True
        assert file.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await file.json() == {"foo": "bar"}
        assert isinstance(file, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_content(self, async_client: AsyncPerplexity, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/responses/response_id/files/file_id/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.responses.files.with_streaming_response.content(
            file_id="file_id",
            response_id="response_id",
        ) as file:
            assert not file.is_closed
            assert file.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await file.json() == {"foo": "bar"}
            assert cast(Any, file.is_closed) is True
            assert isinstance(file, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, file.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_content(self, async_client: AsyncPerplexity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            await async_client.responses.files.with_raw_response.content(
                file_id="file_id",
                response_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.responses.files.with_raw_response.content(
                file_id="",
                response_id="response_id",
            )
