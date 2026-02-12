# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from perplexity import Perplexity, AsyncPerplexity
from tests.utils import assert_matches_type
from perplexity.types.shared import ReadFileResponse, ListFilesResponse, WriteFileResponse, ModifiedFilesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Perplexity) -> None:
        file = client.sandbox.sessions.files.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListFilesResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Perplexity) -> None:
        file = client.sandbox.sessions.files.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            depth=1,
            path="path",
        )
        assert_matches_type(ListFilesResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Perplexity) -> None:
        response = client.sandbox.sessions.files.with_raw_response.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(ListFilesResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Perplexity) -> None:
        with client.sandbox.sessions.files.with_streaming_response.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(ListFilesResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Perplexity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sandbox.sessions.files.with_raw_response.list(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_modified(self, client: Perplexity) -> None:
        file = client.sandbox.sessions.files.modified(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ModifiedFilesResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_modified(self, client: Perplexity) -> None:
        response = client.sandbox.sessions.files.with_raw_response.modified(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(ModifiedFilesResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_modified(self, client: Perplexity) -> None:
        with client.sandbox.sessions.files.with_streaming_response.modified(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(ModifiedFilesResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_modified(self, client: Perplexity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sandbox.sessions.files.with_raw_response.modified(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read(self, client: Perplexity) -> None:
        file = client.sandbox.sessions.files.read(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="path",
        )
        assert_matches_type(ReadFileResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_read(self, client: Perplexity) -> None:
        response = client.sandbox.sessions.files.with_raw_response.read(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(ReadFileResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_read(self, client: Perplexity) -> None:
        with client.sandbox.sessions.files.with_streaming_response.read(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(ReadFileResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_read(self, client: Perplexity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sandbox.sessions.files.with_raw_response.read(
                session_id="",
                path="path",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_write(self, client: Perplexity) -> None:
        file = client.sandbox.sessions.files.write(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="content",
            path="path",
        )
        assert_matches_type(WriteFileResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_write(self, client: Perplexity) -> None:
        response = client.sandbox.sessions.files.with_raw_response.write(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="content",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(WriteFileResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_write(self, client: Perplexity) -> None:
        with client.sandbox.sessions.files.with_streaming_response.write(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="content",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(WriteFileResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_write(self, client: Perplexity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sandbox.sessions.files.with_raw_response.write(
                session_id="",
                content="content",
                path="path",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPerplexity) -> None:
        file = await async_client.sandbox.sessions.files.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListFilesResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPerplexity) -> None:
        file = await async_client.sandbox.sessions.files.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            depth=1,
            path="path",
        )
        assert_matches_type(ListFilesResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPerplexity) -> None:
        response = await async_client.sandbox.sessions.files.with_raw_response.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(ListFilesResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPerplexity) -> None:
        async with async_client.sandbox.sessions.files.with_streaming_response.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(ListFilesResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncPerplexity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sandbox.sessions.files.with_raw_response.list(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_modified(self, async_client: AsyncPerplexity) -> None:
        file = await async_client.sandbox.sessions.files.modified(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ModifiedFilesResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_modified(self, async_client: AsyncPerplexity) -> None:
        response = await async_client.sandbox.sessions.files.with_raw_response.modified(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(ModifiedFilesResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_modified(self, async_client: AsyncPerplexity) -> None:
        async with async_client.sandbox.sessions.files.with_streaming_response.modified(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(ModifiedFilesResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_modified(self, async_client: AsyncPerplexity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sandbox.sessions.files.with_raw_response.modified(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read(self, async_client: AsyncPerplexity) -> None:
        file = await async_client.sandbox.sessions.files.read(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="path",
        )
        assert_matches_type(ReadFileResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_read(self, async_client: AsyncPerplexity) -> None:
        response = await async_client.sandbox.sessions.files.with_raw_response.read(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(ReadFileResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncPerplexity) -> None:
        async with async_client.sandbox.sessions.files.with_streaming_response.read(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(ReadFileResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_read(self, async_client: AsyncPerplexity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sandbox.sessions.files.with_raw_response.read(
                session_id="",
                path="path",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_write(self, async_client: AsyncPerplexity) -> None:
        file = await async_client.sandbox.sessions.files.write(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="content",
            path="path",
        )
        assert_matches_type(WriteFileResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_write(self, async_client: AsyncPerplexity) -> None:
        response = await async_client.sandbox.sessions.files.with_raw_response.write(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="content",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(WriteFileResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_write(self, async_client: AsyncPerplexity) -> None:
        async with async_client.sandbox.sessions.files.with_streaming_response.write(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="content",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(WriteFileResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_write(self, async_client: AsyncPerplexity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sandbox.sessions.files.with_raw_response.write(
                session_id="",
                content="content",
                path="path",
            )
