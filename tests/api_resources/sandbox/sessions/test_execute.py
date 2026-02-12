# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from perplexity import Perplexity, AsyncPerplexity
from tests.utils import assert_matches_type
from perplexity.types.shared import ExecuteCodeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExecute:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Perplexity) -> None:
        execute = client.sandbox.sessions.execute.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            language="python",
        )
        assert_matches_type(ExecuteCodeResponse, execute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Perplexity) -> None:
        execute = client.sandbox.sessions.execute.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            language="python",
            background=True,
            execution_timeout=1,
        )
        assert_matches_type(ExecuteCodeResponse, execute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Perplexity) -> None:
        response = client.sandbox.sessions.execute.with_raw_response.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            language="python",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execute = response.parse()
        assert_matches_type(ExecuteCodeResponse, execute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Perplexity) -> None:
        with client.sandbox.sessions.execute.with_streaming_response.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            language="python",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execute = response.parse()
            assert_matches_type(ExecuteCodeResponse, execute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Perplexity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sandbox.sessions.execute.with_raw_response.create(
                session_id="",
                code="code",
                language="python",
            )


class TestAsyncExecute:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPerplexity) -> None:
        execute = await async_client.sandbox.sessions.execute.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            language="python",
        )
        assert_matches_type(ExecuteCodeResponse, execute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPerplexity) -> None:
        execute = await async_client.sandbox.sessions.execute.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            language="python",
            background=True,
            execution_timeout=1,
        )
        assert_matches_type(ExecuteCodeResponse, execute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPerplexity) -> None:
        response = await async_client.sandbox.sessions.execute.with_raw_response.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            language="python",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execute = await response.parse()
        assert_matches_type(ExecuteCodeResponse, execute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPerplexity) -> None:
        async with async_client.sandbox.sessions.execute.with_streaming_response.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code="code",
            language="python",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execute = await response.parse()
            assert_matches_type(ExecuteCodeResponse, execute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncPerplexity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sandbox.sessions.execute.with_raw_response.create(
                session_id="",
                code="code",
                language="python",
            )
