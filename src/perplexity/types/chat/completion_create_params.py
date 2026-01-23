# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..shared_params.chat_message_input import ChatMessageInput
from ..shared_params.web_search_options import WebSearchOptions

__all__ = [
    "CompletionCreateParamsBase",
    "ResponseFormat",
    "ResponseFormatResponseFormatText",
    "ResponseFormatResponseFormatJsonSchema",
    "ResponseFormatResponseFormatJsonSchemaJsonSchema",
    "ResponseFormatResponseFormatRegex",
    "ResponseFormatResponseFormatRegexRegex",
    "Tool",
    "ToolFunction",
    "ToolFunctionParameters",
    "CompletionCreateParamsNonStreaming",
    "CompletionCreateParamsStreaming",
]


class CompletionCreateParamsBase(TypedDict, total=False):
    messages: Required[Iterable[ChatMessageInput]]

    model: Required[str]

    _debug_pro_search: bool

    _force_new_agent: Optional[bool]

    _inputs: Optional[Iterable[int]]

    _prompt_token_length: Optional[int]

    best_of: Optional[int]

    country: Optional[str]

    cum_logprobs: Optional[bool]

    disable_search: Optional[bool]

    diverse_first_token: Optional[bool]

    enable_search_classifier: Optional[bool]

    file_workspace_id: Optional[str]

    frequency_penalty: Optional[float]

    has_image_url: bool

    image_domain_filter: Optional[SequenceNotStr[str]]

    image_format_filter: Optional[SequenceNotStr[str]]

    language_preference: Optional[str]

    last_updated_after_filter: Optional[str]

    last_updated_before_filter: Optional[str]

    latitude: Optional[float]

    logprobs: Optional[bool]

    longitude: Optional[float]

    max_tokens: Optional[int]

    n: Optional[int]

    num_images: int

    num_search_results: int

    parallel_tool_calls: Optional[bool]

    presence_penalty: Optional[float]

    ranking_model: Optional[str]

    reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]]

    response_format: Optional[ResponseFormat]

    response_metadata: Optional[Dict[str, object]]

    return_images: Optional[bool]

    return_related_questions: Optional[bool]

    safe_search: Optional[bool]

    search_after_date_filter: Optional[str]

    search_before_date_filter: Optional[str]

    search_domain_filter: Optional[SequenceNotStr[str]]

    search_internal_properties: Optional[Dict[str, object]]

    search_language_filter: Optional[SequenceNotStr[str]]

    search_mode: Optional[Literal["web", "academic", "sec"]]

    search_recency_filter: Optional[Literal["hour", "day", "week", "month", "year"]]

    search_tenant: Optional[str]

    stop: Union[str, SequenceNotStr[str], None]

    stream_mode: Literal["full", "concise"]

    temperature: Optional[float]

    thread_id: Optional[str]

    tool_choice: Optional[Literal["none", "auto", "required"]]

    tools: Optional[Iterable[Tool]]

    top_k: Optional[int]

    top_logprobs: Optional[int]

    top_p: Optional[float]

    updated_after_timestamp: Optional[int]

    updated_before_timestamp: Optional[int]

    use_threads: Optional[bool]

    user_original_query: Optional[str]

    web_search_options: WebSearchOptions


class ResponseFormatResponseFormatText(TypedDict, total=False):
    type: Required[Literal["text"]]


class ResponseFormatResponseFormatJsonSchemaJsonSchema(TypedDict, total=False):
    schema: Required[Dict[str, object]]

    description: Optional[str]

    name: Optional[str]

    strict: Optional[bool]


class ResponseFormatResponseFormatJsonSchema(TypedDict, total=False):
    json_schema: Required[ResponseFormatResponseFormatJsonSchemaJsonSchema]

    type: Required[Literal["json_schema"]]


class ResponseFormatResponseFormatRegexRegex(TypedDict, total=False):
    regex: Required[str]

    description: Optional[str]

    name: Optional[str]

    strict: Optional[bool]


class ResponseFormatResponseFormatRegex(TypedDict, total=False):
    regex: Required[ResponseFormatResponseFormatRegexRegex]

    type: Required[Literal["regex"]]


ResponseFormat: TypeAlias = Union[
    ResponseFormatResponseFormatText, ResponseFormatResponseFormatJsonSchema, ResponseFormatResponseFormatRegex
]


class ToolFunctionParameters(TypedDict, total=False):
    properties: Required[Dict[str, object]]

    type: Required[str]

    additional_properties: Optional[bool]

    required: Optional[SequenceNotStr[str]]


class ToolFunction(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    parameters: Required[ToolFunctionParameters]

    strict: Optional[bool]


class Tool(TypedDict, total=False):
    function: Required[ToolFunction]

    type: Required[Literal["function"]]


class CompletionCreateParamsNonStreaming(CompletionCreateParamsBase, total=False):
    stream: Optional[Literal[False]]


class CompletionCreateParamsStreaming(CompletionCreateParamsBase):
    stream: Required[Literal[True]]


CompletionCreateParams = Union[CompletionCreateParamsNonStreaming, CompletionCreateParamsStreaming]
