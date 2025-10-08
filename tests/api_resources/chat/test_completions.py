# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from perplexity import Perplexity, AsyncPerplexity
from tests.utils import assert_matches_type
from perplexity.types import StreamChunk

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Perplexity) -> None:
        completion = client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
        )
        assert_matches_type(StreamChunk, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Perplexity) -> None:
        completion = client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                    "reasoning_steps": [
                        {
                            "thought": "thought",
                            "type": "web_search",
                            "agent_progress": {
                                "action": "action",
                                "screenshot": "screenshot",
                                "url": "url",
                            },
                            "browser_agent": {
                                "result": "result",
                                "url": "url",
                            },
                            "browser_tool_execution": {"tool": {"foo": "bar"}},
                            "execute_python": {
                                "code": "code",
                                "result": "result",
                            },
                            "fetch_url_content": {
                                "contents": [
                                    {
                                        "title": "title",
                                        "url": "url",
                                        "date": "date",
                                        "last_updated": "last_updated",
                                        "snippet": "snippet",
                                        "source": "web",
                                    }
                                ]
                            },
                            "file_attachment_search": {"attachment_urls": ["string"]},
                            "web_search": {
                                "search_keywords": ["string"],
                                "search_results": [
                                    {
                                        "title": "title",
                                        "url": "url",
                                        "date": "date",
                                        "last_updated": "last_updated",
                                        "snippet": "snippet",
                                        "source": "web",
                                    }
                                ],
                            },
                        }
                    ],
                    "tool_calls": [
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        }
                    ],
                }
            ],
            model="model",
            _debug_pro_search=True,
            _inputs=[0],
            _is_browser_agent=True,
            _prompt_token_length=0,
            best_of=0,
            country="country",
            cum_logprobs=True,
            debug_params={
                "summarizer_model_override": "summarizer_model_override",
                "summarizer_prompt_override": "summarizer_prompt_override",
            },
            disable_search=True,
            diverse_first_token=True,
            enable_search_classifier=True,
            file_workspace_id="file_workspace_id",
            frequency_penalty=-2,
            has_image_url=True,
            image_domain_filter=["string"],
            image_format_filter=["string"],
            language_preference="language_preference",
            last_updated_after_filter="last_updated_after_filter",
            last_updated_before_filter="last_updated_before_filter",
            latitude=0,
            logprobs=True,
            longitude=0,
            max_tokens=1,
            n=1,
            num_images=0,
            num_search_results=0,
            parallel_tool_calls=True,
            presence_penalty=-2,
            ranking_model="ranking_model",
            reasoning_effort="minimal",
            response_format={"type": "text"},
            response_metadata={"foo": "bar"},
            return_images=True,
            return_related_questions=True,
            safe_search=True,
            search_after_date_filter="search_after_date_filter",
            search_before_date_filter="search_before_date_filter",
            search_domain_filter=["string"],
            search_internal_properties={"foo": "bar"},
            search_mode="web",
            search_recency_filter="hour",
            search_tenant="search_tenant",
            stop="string",
            stream=False,
            stream_mode="full",
            temperature=0,
            thread_id="thread_id",
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "description": "description",
                        "name": "name",
                        "parameters": {
                            "properties": {"foo": "bar"},
                            "type": "type",
                            "additional_properties": True,
                            "required": ["string"],
                        },
                        "strict": True,
                    },
                    "type": "function",
                }
            ],
            top_k=0,
            top_logprobs=0,
            top_p=0,
            updated_after_timestamp=0,
            updated_before_timestamp=0,
            use_threads=True,
            web_search_options={
                "image_results_enhanced_relevance": True,
                "search_context_size": "low",
                "search_type": "fast",
                "user_location": {
                    "city": "city",
                    "country": "country",
                    "latitude": 0,
                    "longitude": 0,
                    "region": "region",
                },
            },
        )
        assert_matches_type(StreamChunk, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Perplexity) -> None:
        response = client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(StreamChunk, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Perplexity) -> None:
        with client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(StreamChunk, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Perplexity) -> None:
        completion_stream = client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
            stream=True,
        )
        completion_stream.response.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Perplexity) -> None:
        completion_stream = client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                    "reasoning_steps": [
                        {
                            "thought": "thought",
                            "type": "web_search",
                            "agent_progress": {
                                "action": "action",
                                "screenshot": "screenshot",
                                "url": "url",
                            },
                            "browser_agent": {
                                "result": "result",
                                "url": "url",
                            },
                            "browser_tool_execution": {"tool": {"foo": "bar"}},
                            "execute_python": {
                                "code": "code",
                                "result": "result",
                            },
                            "fetch_url_content": {
                                "contents": [
                                    {
                                        "title": "title",
                                        "url": "url",
                                        "date": "date",
                                        "last_updated": "last_updated",
                                        "snippet": "snippet",
                                        "source": "web",
                                    }
                                ]
                            },
                            "file_attachment_search": {"attachment_urls": ["string"]},
                            "web_search": {
                                "search_keywords": ["string"],
                                "search_results": [
                                    {
                                        "title": "title",
                                        "url": "url",
                                        "date": "date",
                                        "last_updated": "last_updated",
                                        "snippet": "snippet",
                                        "source": "web",
                                    }
                                ],
                            },
                        }
                    ],
                    "tool_calls": [
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        }
                    ],
                }
            ],
            model="model",
            stream=True,
            _debug_pro_search=True,
            _inputs=[0],
            _is_browser_agent=True,
            _prompt_token_length=0,
            best_of=0,
            country="country",
            cum_logprobs=True,
            debug_params={
                "summarizer_model_override": "summarizer_model_override",
                "summarizer_prompt_override": "summarizer_prompt_override",
            },
            disable_search=True,
            diverse_first_token=True,
            enable_search_classifier=True,
            file_workspace_id="file_workspace_id",
            frequency_penalty=-2,
            has_image_url=True,
            image_domain_filter=["string"],
            image_format_filter=["string"],
            language_preference="language_preference",
            last_updated_after_filter="last_updated_after_filter",
            last_updated_before_filter="last_updated_before_filter",
            latitude=0,
            logprobs=True,
            longitude=0,
            max_tokens=1,
            n=1,
            num_images=0,
            num_search_results=0,
            parallel_tool_calls=True,
            presence_penalty=-2,
            ranking_model="ranking_model",
            reasoning_effort="minimal",
            response_format={"type": "text"},
            response_metadata={"foo": "bar"},
            return_images=True,
            return_related_questions=True,
            safe_search=True,
            search_after_date_filter="search_after_date_filter",
            search_before_date_filter="search_before_date_filter",
            search_domain_filter=["string"],
            search_internal_properties={"foo": "bar"},
            search_mode="web",
            search_recency_filter="hour",
            search_tenant="search_tenant",
            stop="string",
            stream_mode="full",
            temperature=0,
            thread_id="thread_id",
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "description": "description",
                        "name": "name",
                        "parameters": {
                            "properties": {"foo": "bar"},
                            "type": "type",
                            "additional_properties": True,
                            "required": ["string"],
                        },
                        "strict": True,
                    },
                    "type": "function",
                }
            ],
            top_k=0,
            top_logprobs=0,
            top_p=0,
            updated_after_timestamp=0,
            updated_before_timestamp=0,
            use_threads=True,
            web_search_options={
                "image_results_enhanced_relevance": True,
                "search_context_size": "low",
                "search_type": "fast",
                "user_location": {
                    "city": "city",
                    "country": "country",
                    "latitude": 0,
                    "longitude": 0,
                    "region": "region",
                },
            },
        )
        completion_stream.response.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Perplexity) -> None:
        response = client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Perplexity) -> None:
        with client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncPerplexity) -> None:
        completion = await async_client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
        )
        assert_matches_type(StreamChunk, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncPerplexity) -> None:
        completion = await async_client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                    "reasoning_steps": [
                        {
                            "thought": "thought",
                            "type": "web_search",
                            "agent_progress": {
                                "action": "action",
                                "screenshot": "screenshot",
                                "url": "url",
                            },
                            "browser_agent": {
                                "result": "result",
                                "url": "url",
                            },
                            "browser_tool_execution": {"tool": {"foo": "bar"}},
                            "execute_python": {
                                "code": "code",
                                "result": "result",
                            },
                            "fetch_url_content": {
                                "contents": [
                                    {
                                        "title": "title",
                                        "url": "url",
                                        "date": "date",
                                        "last_updated": "last_updated",
                                        "snippet": "snippet",
                                        "source": "web",
                                    }
                                ]
                            },
                            "file_attachment_search": {"attachment_urls": ["string"]},
                            "web_search": {
                                "search_keywords": ["string"],
                                "search_results": [
                                    {
                                        "title": "title",
                                        "url": "url",
                                        "date": "date",
                                        "last_updated": "last_updated",
                                        "snippet": "snippet",
                                        "source": "web",
                                    }
                                ],
                            },
                        }
                    ],
                    "tool_calls": [
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        }
                    ],
                }
            ],
            model="model",
            _debug_pro_search=True,
            _inputs=[0],
            _is_browser_agent=True,
            _prompt_token_length=0,
            best_of=0,
            country="country",
            cum_logprobs=True,
            debug_params={
                "summarizer_model_override": "summarizer_model_override",
                "summarizer_prompt_override": "summarizer_prompt_override",
            },
            disable_search=True,
            diverse_first_token=True,
            enable_search_classifier=True,
            file_workspace_id="file_workspace_id",
            frequency_penalty=-2,
            has_image_url=True,
            image_domain_filter=["string"],
            image_format_filter=["string"],
            language_preference="language_preference",
            last_updated_after_filter="last_updated_after_filter",
            last_updated_before_filter="last_updated_before_filter",
            latitude=0,
            logprobs=True,
            longitude=0,
            max_tokens=1,
            n=1,
            num_images=0,
            num_search_results=0,
            parallel_tool_calls=True,
            presence_penalty=-2,
            ranking_model="ranking_model",
            reasoning_effort="minimal",
            response_format={"type": "text"},
            response_metadata={"foo": "bar"},
            return_images=True,
            return_related_questions=True,
            safe_search=True,
            search_after_date_filter="search_after_date_filter",
            search_before_date_filter="search_before_date_filter",
            search_domain_filter=["string"],
            search_internal_properties={"foo": "bar"},
            search_mode="web",
            search_recency_filter="hour",
            search_tenant="search_tenant",
            stop="string",
            stream=False,
            stream_mode="full",
            temperature=0,
            thread_id="thread_id",
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "description": "description",
                        "name": "name",
                        "parameters": {
                            "properties": {"foo": "bar"},
                            "type": "type",
                            "additional_properties": True,
                            "required": ["string"],
                        },
                        "strict": True,
                    },
                    "type": "function",
                }
            ],
            top_k=0,
            top_logprobs=0,
            top_p=0,
            updated_after_timestamp=0,
            updated_before_timestamp=0,
            use_threads=True,
            web_search_options={
                "image_results_enhanced_relevance": True,
                "search_context_size": "low",
                "search_type": "fast",
                "user_location": {
                    "city": "city",
                    "country": "country",
                    "latitude": 0,
                    "longitude": 0,
                    "region": "region",
                },
            },
        )
        assert_matches_type(StreamChunk, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncPerplexity) -> None:
        response = await async_client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(StreamChunk, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncPerplexity) -> None:
        async with async_client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(StreamChunk, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncPerplexity) -> None:
        completion_stream = await async_client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
            stream=True,
        )
        await completion_stream.response.aclose()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncPerplexity) -> None:
        completion_stream = await async_client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                    "reasoning_steps": [
                        {
                            "thought": "thought",
                            "type": "web_search",
                            "agent_progress": {
                                "action": "action",
                                "screenshot": "screenshot",
                                "url": "url",
                            },
                            "browser_agent": {
                                "result": "result",
                                "url": "url",
                            },
                            "browser_tool_execution": {"tool": {"foo": "bar"}},
                            "execute_python": {
                                "code": "code",
                                "result": "result",
                            },
                            "fetch_url_content": {
                                "contents": [
                                    {
                                        "title": "title",
                                        "url": "url",
                                        "date": "date",
                                        "last_updated": "last_updated",
                                        "snippet": "snippet",
                                        "source": "web",
                                    }
                                ]
                            },
                            "file_attachment_search": {"attachment_urls": ["string"]},
                            "web_search": {
                                "search_keywords": ["string"],
                                "search_results": [
                                    {
                                        "title": "title",
                                        "url": "url",
                                        "date": "date",
                                        "last_updated": "last_updated",
                                        "snippet": "snippet",
                                        "source": "web",
                                    }
                                ],
                            },
                        }
                    ],
                    "tool_calls": [
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        }
                    ],
                }
            ],
            model="model",
            stream=True,
            _debug_pro_search=True,
            _inputs=[0],
            _is_browser_agent=True,
            _prompt_token_length=0,
            best_of=0,
            country="country",
            cum_logprobs=True,
            debug_params={
                "summarizer_model_override": "summarizer_model_override",
                "summarizer_prompt_override": "summarizer_prompt_override",
            },
            disable_search=True,
            diverse_first_token=True,
            enable_search_classifier=True,
            file_workspace_id="file_workspace_id",
            frequency_penalty=-2,
            has_image_url=True,
            image_domain_filter=["string"],
            image_format_filter=["string"],
            language_preference="language_preference",
            last_updated_after_filter="last_updated_after_filter",
            last_updated_before_filter="last_updated_before_filter",
            latitude=0,
            logprobs=True,
            longitude=0,
            max_tokens=1,
            n=1,
            num_images=0,
            num_search_results=0,
            parallel_tool_calls=True,
            presence_penalty=-2,
            ranking_model="ranking_model",
            reasoning_effort="minimal",
            response_format={"type": "text"},
            response_metadata={"foo": "bar"},
            return_images=True,
            return_related_questions=True,
            safe_search=True,
            search_after_date_filter="search_after_date_filter",
            search_before_date_filter="search_before_date_filter",
            search_domain_filter=["string"],
            search_internal_properties={"foo": "bar"},
            search_mode="web",
            search_recency_filter="hour",
            search_tenant="search_tenant",
            stop="string",
            stream_mode="full",
            temperature=0,
            thread_id="thread_id",
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "description": "description",
                        "name": "name",
                        "parameters": {
                            "properties": {"foo": "bar"},
                            "type": "type",
                            "additional_properties": True,
                            "required": ["string"],
                        },
                        "strict": True,
                    },
                    "type": "function",
                }
            ],
            top_k=0,
            top_logprobs=0,
            top_p=0,
            updated_after_timestamp=0,
            updated_before_timestamp=0,
            use_threads=True,
            web_search_options={
                "image_results_enhanced_relevance": True,
                "search_context_size": "low",
                "search_type": "fast",
                "user_location": {
                    "city": "city",
                    "country": "country",
                    "latitude": 0,
                    "longitude": 0,
                    "region": "region",
                },
            },
        )
        await completion_stream.response.aclose()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncPerplexity) -> None:
        response = await async_client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncPerplexity) -> None:
        async with async_client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
