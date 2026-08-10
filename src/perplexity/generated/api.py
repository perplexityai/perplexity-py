# ruff: noqa
# Generated from SDK OpenAPI. Do not edit.
from __future__ import annotations
from functools import cached_property
from pydantic import Field
from typing import Any, Mapping, Optional, Sequence, Union, cast, overload
from typing_extensions import Literal, TypeAlias
from typing_extensions import Never as Never
from .runtime import (
    AsyncAPIResource,
    AsyncBinaryAPIResponse,
    AsyncStream,
    BaseModel,
    BinaryAPIResponse,
    Body,
    Headers,
    NoneType,
    NotGiven,
    Omit,
    Query,
    Stream,
    SyncAPIResource,
    Timeout,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    make_request_options,
    not_given,
    omit,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)


def _without_omitted(values: Mapping[str, object]) -> dict[str, object]:
    return {key: value for key, value in values.items() if value is not omit}


def _without_omitted_headers(values: Mapping[str, object]) -> dict[str, str]:
    return {key: str(value) for key, value in values.items() if value is not omit}


class AdvisorResultOutputItemInput(BaseModel):
    advice: Optional[str] = None
    arguments: Optional[str] = None
    call_id: str
    error_code: Optional[str] = None
    error_message: Optional[str] = None
    question: Optional[str] = None
    status: "StatusInput"
    type: Literal["advisor_result"]


class AdvisorResultOutputItemOutput(BaseModel):
    advice: Optional[str] = None
    arguments: Optional[str] = None
    call_id: str
    error_code: Optional[str] = None
    error_message: Optional[str] = None
    question: Optional[str] = None
    status: "StatusOutput"
    type: Literal["advisor_result"]


class AnnotationInput(BaseModel):
    end_index: Optional[int] = None
    start_index: Optional[int] = None
    title: Optional[str] = None
    type: Optional[str] = None
    url: Optional[str] = None


class AnnotationOutput(BaseModel):
    end_index: Optional[int] = None
    start_index: Optional[int] = None
    title: Optional[str] = None
    type: Optional[str] = None
    url: Optional[str] = None


class ApiChatCompletionsRequestInput(BaseModel):
    _debug_pro_search: Optional[bool] = None
    _force_new_agent: Union[bool, None] = None
    _inputs: Union[list[int], None] = None
    _prompt_token_length: Union[int, None] = None
    best_of: Union[int, None] = None
    country: Union[str, None] = None
    cum_logprobs: Union[bool, None] = None
    disable_search: Union[bool, None] = None
    diverse_first_token: Union[bool, None] = None
    enable_search_classifier: Union[bool, None] = None
    file_workspace_id: Union[str, None] = None
    frequency_penalty: Union[float, None] = None
    has_image_url: Optional[bool] = None
    image_domain_filter: Union[list[str], None] = None
    image_format_filter: Union[list[str], None] = None
    language_preference: Union[str, None] = None
    last_updated_after_filter: Union[str, None] = None
    last_updated_before_filter: Union[str, None] = None
    latitude: Union[float, None] = None
    logprobs: Union[bool, None] = None
    longitude: Union[float, None] = None
    max_tokens: Union[int, None] = None
    messages: list["ChatMessageInputInput"]
    model: str
    n: Union[int, None] = None
    num_images: Optional[int] = None
    num_search_results: Optional[int] = None
    parallel_tool_calls: Union[bool, None] = None
    presence_penalty: Union[float, None] = None
    ranking_model: Union[str, None] = None
    reasoning_effort: Union[Literal["minimal", "low", "medium", "high"], None] = None
    response_format: Union[
        "ResponseFormatTextInput",
        "ResponseFormatJSONSchemaInput",
        "ResponseFormatRegexInput",
        None,
    ] = None
    response_formatting_locale: Union[str, None] = None
    response_metadata: Union[dict[str, Any], None] = None
    return_images: Union[bool, None] = None
    return_related_questions: Union[bool, None] = None
    safe_search: Union[bool, None] = None
    search_after_date_filter: Union[str, None] = None
    search_before_date_filter: Union[str, None] = None
    search_domain_filter: Union[list[str], None] = None
    search_internal_properties: Union[dict[str, Any], None] = None
    search_language_filter: Union[list[str], None] = None
    search_mode: Union[Literal["web", "academic", "sec"], None] = None
    search_recency_filter: Union[
        Literal["hour", "day", "week", "month", "year"], None
    ] = None
    search_tenant: Union[str, None] = None
    stop: Union[str, list[str], None] = None
    stream: Union[bool, None] = None
    stream_mode: Optional[Literal["full", "concise"]] = None
    temperature: Union[float, None] = None
    thread_id: Union[str, None] = None
    tool_choice: Union[Literal["none", "auto", "required"], None] = None
    tools: Union[list["ToolSpecInput"], None] = None
    top_k: Union[int, None] = None
    top_logprobs: Union[int, None] = None
    top_p: Union[float, None] = None
    updated_after_timestamp: Union[int, None] = None
    updated_before_timestamp: Union[int, None] = None
    use_threads: Union[bool, None] = None
    user_original_query: Union[str, None] = None
    web_search_options: Optional["WebSearchOptionsInput"] = None


class ApiChatCompletionsRequestOutput(BaseModel):
    _debug_pro_search: Optional[bool] = None
    _force_new_agent: Union[bool, None] = None
    _inputs: Union[list[int], None] = None
    _prompt_token_length: Union[int, None] = None
    best_of: Union[int, None] = None
    country: Union[str, None] = None
    cum_logprobs: Union[bool, None] = None
    disable_search: Union[bool, None] = None
    diverse_first_token: Union[bool, None] = None
    enable_search_classifier: Union[bool, None] = None
    file_workspace_id: Union[str, None] = None
    frequency_penalty: Union[float, None] = None
    has_image_url: Optional[bool] = None
    image_domain_filter: Union[list[str], None] = None
    image_format_filter: Union[list[str], None] = None
    language_preference: Union[str, None] = None
    last_updated_after_filter: Union[str, None] = None
    last_updated_before_filter: Union[str, None] = None
    latitude: Union[float, None] = None
    logprobs: Union[bool, None] = None
    longitude: Union[float, None] = None
    max_tokens: Union[int, None] = None
    messages: list["ChatMessageInputOutput"]
    model: str
    n: Union[int, None] = None
    num_images: Optional[int] = None
    num_search_results: Optional[int] = None
    parallel_tool_calls: Union[bool, None] = None
    presence_penalty: Union[float, None] = None
    ranking_model: Union[str, None] = None
    reasoning_effort: Union[Literal["minimal", "low", "medium", "high"], None] = None
    response_format: Union[
        "ResponseFormatTextOutput",
        "ResponseFormatJSONSchemaOutput",
        "ResponseFormatRegexOutput",
        None,
    ] = None
    response_formatting_locale: Union[str, None] = None
    response_metadata: Union[dict[str, Any], None] = None
    return_images: Union[bool, None] = None
    return_related_questions: Union[bool, None] = None
    safe_search: Union[bool, None] = None
    search_after_date_filter: Union[str, None] = None
    search_before_date_filter: Union[str, None] = None
    search_domain_filter: Union[list[str], None] = None
    search_internal_properties: Union[dict[str, Any], None] = None
    search_language_filter: Union[list[str], None] = None
    search_mode: Union[Literal["web", "academic", "sec"], None] = None
    search_recency_filter: Union[
        Literal["hour", "day", "week", "month", "year"], None
    ] = None
    search_tenant: Union[str, None] = None
    stop: Union[str, list[str], None] = None
    stream: Union[bool, None] = None
    stream_mode: Optional[Literal["full", "concise"]] = None
    temperature: Union[float, None] = None
    thread_id: Union[str, None] = None
    tool_choice: Union[Literal["none", "auto", "required"], None] = None
    tools: Union[list["ToolSpecOutput"], None] = None
    top_k: Union[int, None] = None
    top_logprobs: Union[int, None] = None
    top_p: Union[float, None] = None
    updated_after_timestamp: Union[int, None] = None
    updated_before_timestamp: Union[int, None] = None
    use_threads: Union[bool, None] = None
    user_original_query: Union[str, None] = None
    web_search_options: Optional["WebSearchOptionsOutput"] = None


class ApiPublicSearchResultInput(BaseModel):
    date: Union[str, None] = None
    last_updated: Union[str, None] = None
    snippet: Optional[str] = None
    source: Optional[Literal["web", "attachment"]] = None
    title: str
    url: str


class ApiPublicSearchResultOutput(BaseModel):
    date: Union[str, None] = None
    last_updated: Union[str, None] = None
    snippet: Optional[str] = None
    source: Optional[Literal["web", "attachment"]] = None
    title: str
    url: str


class ApiSearchPageInput(BaseModel):
    date: Union[str, None] = None
    last_updated: Union[str, None] = None
    snippet: str
    title: str
    url: str


class ApiSearchPageOutput(BaseModel):
    date: Union[str, None] = None
    last_updated: Union[str, None] = None
    snippet: str
    title: str
    url: str


class ApiSearchRequestInput(BaseModel):
    country: Union[str, None] = None
    display_server_time: Optional[bool] = None
    last_updated_after_filter: Union[str, None] = None
    last_updated_before_filter: Union[str, None] = None
    max_results: Optional[int] = None
    max_tokens: Optional[int] = None
    max_tokens_per_page: Optional[int] = None
    query: Union[str, list[str]]
    search_after_date_filter: Union[str, None] = None
    search_before_date_filter: Union[str, None] = None
    search_context_size: Optional[Literal["low", "medium", "high"]] = None
    search_domain_filter: Union[list[str], None] = None
    search_language_filter: Union[list[str], None] = None
    search_mode: Union[Literal["web", "academic", "sec"], None] = None
    search_recency_filter: Union[
        Literal["hour", "day", "week", "month", "year"], None
    ] = None
    search_type: Union[Literal["web", "people"], None] = None


class ApiSearchRequestOutput(BaseModel):
    country: Union[str, None] = None
    display_server_time: Optional[bool] = None
    last_updated_after_filter: Union[str, None] = None
    last_updated_before_filter: Union[str, None] = None
    max_results: Optional[int] = None
    max_tokens: Optional[int] = None
    max_tokens_per_page: Optional[int] = None
    query: Union[str, list[str]]
    search_after_date_filter: Union[str, None] = None
    search_before_date_filter: Union[str, None] = None
    search_context_size: Optional[Literal["low", "medium", "high"]] = None
    search_domain_filter: Union[list[str], None] = None
    search_language_filter: Union[list[str], None] = None
    search_mode: Union[Literal["web", "academic", "sec"], None] = None
    search_recency_filter: Union[
        Literal["hour", "day", "week", "month", "year"], None
    ] = None
    search_type: Union[Literal["web", "people"], None] = None


class ApiSearchResponseInput(BaseModel):
    id: str
    results: list["ApiSearchPageInput"]
    server_time: Union[str, None] = None


class ApiSearchResponseOutput(BaseModel):
    id: str
    results: list["ApiSearchPageOutput"]
    server_time: Union[str, None] = None


class AsyncApiChatCompletionsRequestInput(BaseModel):
    idempotency_key: Union[str, None] = None
    request: "ApiChatCompletionsRequestInput"


class AsyncApiChatCompletionsRequestOutput(BaseModel):
    idempotency_key: Union[str, None] = None
    request: "ApiChatCompletionsRequestOutput"


class AsyncApiChatCompletionsResponseInput(BaseModel):
    completed_at: Union[int, None] = None
    created_at: int
    error_message: Union[str, None] = None
    failed_at: Union[int, None] = None
    id: str
    model: str
    response: Union["CompletionResponseInput", None] = None
    started_at: Union[int, None] = None
    status: "AsyncProcessingStatusInput"


class AsyncApiChatCompletionsResponseOutput(BaseModel):
    completed_at: Union[int, None] = None
    created_at: int
    error_message: Union[str, None] = None
    failed_at: Union[int, None] = None
    id: str
    model: str
    response: Union["CompletionResponseOutput", None] = None
    started_at: Union[int, None] = None
    status: "AsyncProcessingStatusOutput"


class AsyncApiChatCompletionsResponseSummaryInput(BaseModel):
    completed_at: Union[int, None] = None
    created_at: int
    failed_at: Union[int, None] = None
    id: str
    model: str
    started_at: Union[int, None] = None
    status: "AsyncProcessingStatusInput"


class AsyncApiChatCompletionsResponseSummaryOutput(BaseModel):
    completed_at: Union[int, None] = None
    created_at: int
    failed_at: Union[int, None] = None
    id: str
    model: str
    started_at: Union[int, None] = None
    status: "AsyncProcessingStatusOutput"


AsyncProcessingStatusInput: TypeAlias = Literal[
    "CREATED", "IN_PROGRESS", "COMPLETED", "FAILED"
]
AsyncProcessingStatusOutput: TypeAlias = Literal[
    "CREATED", "IN_PROGRESS", "COMPLETED", "FAILED"
]


class BrowserSessionResponseInput(BaseModel):
    session_id: Optional[str] = None
    status: Optional[Literal["running", "stopped"]] = None


class BrowserSessionResponseOutput(BaseModel):
    session_id: Optional[str] = None
    status: Optional[Literal["running", "stopped"]] = None


class BuiltinSkillInput(BaseModel):
    name: Literal["office", "office/docx", "office/pdf", "office/pptx", "office/xlsx"]
    type: Literal["builtin"]


class BuiltinSkillOutput(BaseModel):
    name: Literal["office", "office/docx", "office/pdf", "office/pptx", "office/xlsx"]
    type: Literal["builtin"]


class ChatMessageInputInput(BaseModel):
    content: Union[
        str,
        list[
            Union[
                "ChatMessageContentTextChunkInput",
                "ChatMessageContentImageChunkInput",
                "ChatMessageContentFileChunkInput",
                "ChatMessageContentPDFChunkInput",
                "ChatMessageContentVideoChunkInput",
            ]
        ],
        None,
    ]
    reasoning_steps: Union[list["ReasoningStepInputInput"], None] = None
    role: "ChatMessageRoleInput"
    tool_call_id: Union[str, None] = None
    tool_calls: Union[list["ToolCallInput"], None] = None


class ChatMessageInputOutput(BaseModel):
    content: Union[
        str,
        list[
            Union[
                "ChatMessageContentTextChunkOutput",
                "ChatMessageContentImageChunkOutput",
                "ChatMessageContentFileChunkOutput",
                "ChatMessageContentPDFChunkOutput",
                "ChatMessageContentVideoChunkOutput",
            ]
        ],
        None,
    ] = None
    reasoning_steps: Union[list["ReasoningStepInputOutput"], None] = None
    role: "ChatMessageRoleOutput"
    tool_call_id: Union[str, None] = None
    tool_calls: Union[list["ToolCallOutput"], None] = None


class ChatMessageOutputInput(BaseModel):
    content: Union[
        str,
        list[
            Union[
                "ChatMessageContentTextChunkInput",
                "ChatMessageContentImageChunkInput",
                "ChatMessageContentFileChunkInput",
                "ChatMessageContentPDFChunkInput",
                "ChatMessageContentVideoChunkInput",
            ]
        ],
        None,
    ]
    reasoning_steps: Union[list["ReasoningStepOutputInput"], None] = None
    role: "ChatMessageRoleInput"
    tool_call_id: Union[str, None] = None
    tool_calls: Union[list["ToolCallInput"], None] = None


class ChatMessageOutputOutput(BaseModel):
    content: Union[
        str,
        list[
            Union[
                "ChatMessageContentTextChunkOutput",
                "ChatMessageContentImageChunkOutput",
                "ChatMessageContentFileChunkOutput",
                "ChatMessageContentPDFChunkOutput",
                "ChatMessageContentVideoChunkOutput",
            ]
        ],
        None,
    ] = None
    reasoning_steps: Union[list["ReasoningStepOutputOutput"], None] = None
    role: "ChatMessageRoleOutput"
    tool_call_id: Union[str, None] = None
    tool_calls: Union[list["ToolCallOutput"], None] = None


class ChatMessageContentFileChunkInput(BaseModel):
    file_name: Union[str, None] = None
    file_url: Union["URLInput", str]
    type: Literal["file_url"]


class ChatMessageContentFileChunkOutput(BaseModel):
    file_name: Union[str, None] = None
    file_url: Union["URLOutput", str]
    type: Literal["file_url"]


class ChatMessageContentImageChunkInput(BaseModel):
    image_url: Union["URLInput", str]
    type: Literal["image_url"]


class ChatMessageContentImageChunkOutput(BaseModel):
    image_url: Union["URLOutput", str]
    type: Literal["image_url"]


class ChatMessageContentPDFChunkInput(BaseModel):
    pdf_url: Union["URLInput", str]
    type: Literal["pdf_url"]


class ChatMessageContentPDFChunkOutput(BaseModel):
    pdf_url: Union["URLOutput", str]
    type: Literal["pdf_url"]


class ChatMessageContentTextChunkInput(BaseModel):
    text: str
    type: Literal["text"]


class ChatMessageContentTextChunkOutput(BaseModel):
    text: str
    type: Literal["text"]


class ChatMessageContentVideoChunkInput(BaseModel):
    type: Literal["video_url"]
    video_url: Union["VideoURLInput", str]


class ChatMessageContentVideoChunkOutput(BaseModel):
    type: Literal["video_url"]
    video_url: Union["VideoURLOutput", str]


ChatMessageRoleInput: TypeAlias = Literal["system", "user", "assistant", "tool"]
ChatMessageRoleOutput: TypeAlias = Literal["system", "user", "assistant", "tool"]


class ChoiceInput(BaseModel):
    delta: "ChatMessageOutputInput"
    finish_reason: Union[Literal["stop", "length"], None] = None
    index: int
    message: "ChatMessageOutputInput"


class ChoiceOutput(BaseModel):
    delta: "ChatMessageOutputOutput"
    finish_reason: Union[Literal["stop", "length"], None] = None
    index: int
    message: "ChatMessageOutputOutput"


class CompletionResponseInput(BaseModel):
    choices: list["ChoiceInput"]
    citations: Union[list[str], None] = None
    created: int
    id: str
    model: str
    object: Optional[str] = None
    search_results: Union[list["ApiPublicSearchResultInput"], None] = None
    status: Union["CompletionResponseStatusInput", None] = None
    type: Union["CompletionResponseTypeInput", None] = None
    usage: Union["UsageInfoInput", None] = None


class CompletionResponseOutput(BaseModel):
    choices: list["ChoiceOutput"]
    citations: Union[list[str], None] = None
    created: int
    id: str
    model: str
    object: Optional[str] = None
    search_results: Union[list["ApiPublicSearchResultOutput"], None] = None
    status: Union["CompletionResponseStatusOutput", None] = None
    type: Union["CompletionResponseTypeOutput", None] = None
    usage: Union["UsageInfoOutput", None] = None


CompletionResponseStatusInput: TypeAlias = Literal["PENDING", "COMPLETED"]
CompletionResponseStatusOutput: TypeAlias = Literal["PENDING", "COMPLETED"]
CompletionResponseTypeInput: TypeAlias = Literal["message", "info", "end_of_stream"]
CompletionResponseTypeOutput: TypeAlias = Literal["message", "info", "end_of_stream"]


class ContentPartInput(BaseModel):
    annotations: Optional[list["AnnotationInput"]] = None
    text: str
    type: "ContentPartTypeInput"


class ContentPartOutput(BaseModel):
    annotations: Optional[list["AnnotationOutput"]] = None
    text: str
    type: "ContentPartTypeOutput"


ContentPartTypeInput: TypeAlias = Literal["output_text"]
ContentPartTypeOutput: TypeAlias = Literal["output_text"]


class ContextualizedEmbeddingObjectInput(BaseModel):
    data: Optional[list["EmbeddingObjectInput"]] = None
    index: Optional[int] = None
    object: Optional[str] = None


class ContextualizedEmbeddingObjectOutput(BaseModel):
    data: Optional[list["EmbeddingObjectOutput"]] = None
    index: Optional[int] = None
    object: Optional[str] = None


class ContextualizedEmbeddingsRequestInput(BaseModel):
    dimensions: Optional[int] = None
    encoding_format: Optional[Literal["base64_int8", "base64_binary"]] = None
    input: list[list[str]]
    model: Literal["pplx-embed-context-v1-0.6b", "pplx-embed-context-v1-4b"]


class ContextualizedEmbeddingsRequestOutput(BaseModel):
    dimensions: Optional[int] = None
    encoding_format: Optional[Literal["base64_int8", "base64_binary"]] = None
    input: list[list[str]]
    model: Literal["pplx-embed-context-v1-0.6b", "pplx-embed-context-v1-4b"]


class ContextualizedEmbeddingsResponseInput(BaseModel):
    data: Optional[list["ContextualizedEmbeddingObjectInput"]] = None
    model: Optional[str] = None
    object: Optional[str] = None
    usage: Optional["EmbeddingsUsageInput"] = None


class ContextualizedEmbeddingsResponseOutput(BaseModel):
    data: Optional[list["ContextualizedEmbeddingObjectOutput"]] = None
    model: Optional[str] = None
    object: Optional[str] = None
    usage: Optional["EmbeddingsUsageOutput"] = None


class CostInput(BaseModel):
    citation_tokens_cost: Union[float, None] = None
    input_tokens_cost: float
    output_tokens_cost: float
    reasoning_tokens_cost: Union[float, None] = None
    request_cost: Union[float, None] = None
    search_queries_cost: Union[float, None] = None
    total_cost: float


class CostOutput(BaseModel):
    citation_tokens_cost: Union[float, None] = None
    input_tokens_cost: float
    output_tokens_cost: float
    reasoning_tokens_cost: Union[float, None] = None
    request_cost: Union[float, None] = None
    search_queries_cost: Union[float, None] = None
    total_cost: float


class CreateBrowserSessionRequestInput(BaseModel):
    pass


class CreateBrowserSessionRequestOutput(BaseModel):
    pass


CurrencyInput: TypeAlias = Literal["USD"]
CurrencyOutput: TypeAlias = Literal["USD"]
DateInput: TypeAlias = str
DateOutput: TypeAlias = str


class DateFiltersInput(BaseModel):
    last_updated_after_filter: Optional["DateInput"] = None
    last_updated_before_filter: Optional["DateInput"] = None
    search_after_date_filter: Optional["DateInput"] = None
    search_before_date_filter: Optional["DateInput"] = None
    search_recency_filter: Optional["SearchRecencyFilterInput"] = None


class DateFiltersOutput(BaseModel):
    last_updated_after_filter: Optional["DateOutput"] = None
    last_updated_before_filter: Optional["DateOutput"] = None
    search_after_date_filter: Optional["DateOutput"] = None
    search_before_date_filter: Optional["DateOutput"] = None
    search_recency_filter: Optional["SearchRecencyFilterOutput"] = None


class EmbeddingObjectInput(BaseModel):
    embedding: Optional[str] = None
    index: Optional[int] = None
    object: Optional[str] = None


class EmbeddingObjectOutput(BaseModel):
    embedding: Optional[str] = None
    index: Optional[int] = None
    object: Optional[str] = None


class EmbeddingsRequestInput(BaseModel):
    dimensions: Optional[int] = None
    encoding_format: Optional[Literal["base64_int8", "base64_binary"]] = None
    input: Union[str, list[str]]
    model: Literal["pplx-embed-v1-0.6b", "pplx-embed-v1-4b"]


class EmbeddingsRequestOutput(BaseModel):
    dimensions: Optional[int] = None
    encoding_format: Optional[Literal["base64_int8", "base64_binary"]] = None
    input: Union[str, list[str]]
    model: Literal["pplx-embed-v1-0.6b", "pplx-embed-v1-4b"]


class EmbeddingsResponseInput(BaseModel):
    data: Optional[list["EmbeddingObjectInput"]] = None
    model: Optional[str] = None
    object: Optional[str] = None
    usage: Optional["EmbeddingsUsageInput"] = None


class EmbeddingsResponseOutput(BaseModel):
    data: Optional[list["EmbeddingObjectOutput"]] = None
    model: Optional[str] = None
    object: Optional[str] = None
    usage: Optional["EmbeddingsUsageOutput"] = None


class EmbeddingsUsageInput(BaseModel):
    cost: Optional["EmbeddingsUsageCostInput"] = None
    prompt_tokens: Optional[int] = None
    total_tokens: Optional[int] = None


class EmbeddingsUsageOutput(BaseModel):
    cost: Optional["EmbeddingsUsageCostOutput"] = None
    prompt_tokens: Optional[int] = None
    total_tokens: Optional[int] = None


class EmbeddingsUsageCostInput(BaseModel):
    currency: Optional[Literal["USD"]] = None
    input_cost: Optional[float] = None
    total_cost: Optional[float] = None


class EmbeddingsUsageCostOutput(BaseModel):
    currency: Optional[Literal["USD"]] = None
    input_cost: Optional[float] = None
    total_cost: Optional[float] = None


class ErrorInfoInput(BaseModel):
    code: Optional[str] = None
    message: str
    type: Optional[str] = None


class ErrorInfoOutput(BaseModel):
    code: Optional[str] = None
    message: str
    type: Optional[str] = None


EventTypeInput: TypeAlias = Literal[
    "response.created",
    "response.in_progress",
    "response.completed",
    "response.failed",
    "response.output_item.added",
    "response.output_item.done",
    "response.output_text.delta",
    "response.output_text.done",
    "response.reasoning.started",
    "response.reasoning.search_queries",
    "response.reasoning.search_results",
    "response.reasoning.fetch_url_queries",
    "response.reasoning.fetch_url_results",
    "response.reasoning.stopped",
    "response.skill.loaded",
]
EventTypeOutput: TypeAlias = Literal[
    "response.created",
    "response.in_progress",
    "response.completed",
    "response.failed",
    "response.output_item.added",
    "response.output_item.done",
    "response.output_text.delta",
    "response.output_text.done",
    "response.reasoning.started",
    "response.reasoning.search_queries",
    "response.reasoning.search_results",
    "response.reasoning.fetch_url_queries",
    "response.reasoning.fetch_url_results",
    "response.reasoning.stopped",
    "response.skill.loaded",
]


class ExecutePythonStepDetailsInput(BaseModel):
    code: str
    result: str


class ExecutePythonStepDetailsOutput(BaseModel):
    code: str
    result: str


class FetchUrlContentStepDetailsInput(BaseModel):
    contents: list["ApiPublicSearchResultInput"]


class FetchUrlContentStepDetailsOutput(BaseModel):
    contents: list["ApiPublicSearchResultOutput"]


class FetchUrlQueriesEventInput(BaseModel):
    sequence_number: int
    thought: Optional[str] = None
    type: Literal["response.reasoning.fetch_url_queries"]
    urls: list[str]


class FetchUrlQueriesEventOutput(BaseModel):
    sequence_number: int
    thought: Optional[str] = None
    type: Literal["response.reasoning.fetch_url_queries"]
    urls: list[str]


class FetchUrlResultsEventInput(BaseModel):
    contents: list["UrlContentInput"]
    sequence_number: int
    thought: Optional[str] = None
    type: Literal["response.reasoning.fetch_url_results"]


class FetchUrlResultsEventOutput(BaseModel):
    contents: list["UrlContentOutput"]
    sequence_number: int
    thought: Optional[str] = None
    type: Literal["response.reasoning.fetch_url_results"]


class FetchUrlResultsOutputItemInput(BaseModel):
    contents: list["UrlContentInput"]
    type: Literal["fetch_url_results"]


class FetchUrlResultsOutputItemOutput(BaseModel):
    contents: list["UrlContentOutput"]
    type: Literal["fetch_url_results"]


class FetchUrlToolInput(BaseModel):
    max_urls: Optional[int] = None
    type: Literal["fetch_url"]


class FetchUrlToolOutput(BaseModel):
    max_urls: Optional[int] = None
    type: Literal["fetch_url"]


class FinanceSearchToolInput(BaseModel):
    type: Literal["finance_search"]


class FinanceSearchToolOutput(BaseModel):
    type: Literal["finance_search"]


class FunctionCallInputInput(BaseModel):
    arguments: str
    call_id: str
    name: str
    thought_signature: Optional[str] = None
    type: Literal["function_call"]


class FunctionCallInputOutput(BaseModel):
    arguments: str
    call_id: str
    name: str
    thought_signature: Optional[str] = None
    type: Literal["function_call"]


class FunctionCallOutputInputInput(BaseModel):
    call_id: str
    name: Optional[str] = None
    output: str
    thought_signature: Optional[str] = None
    type: Literal["function_call_output"]


class FunctionCallOutputInputOutput(BaseModel):
    call_id: str
    name: Optional[str] = None
    output: str
    thought_signature: Optional[str] = None
    type: Literal["function_call_output"]


class FunctionCallOutputItemInput(BaseModel):
    arguments: str
    call_id: str
    id: str
    name: str
    status: "StatusInput"
    thought_signature: Optional[str] = None
    type: Literal["function_call"]


class FunctionCallOutputItemOutput(BaseModel):
    arguments: str
    call_id: str
    id: str
    name: str
    status: "StatusOutput"
    thought_signature: Optional[str] = None
    type: Literal["function_call"]


class FunctionSpecInput(BaseModel):
    description: str
    name: str
    parameters: "ParameterSpecInput"
    strict: Union[bool, None] = None


class FunctionSpecOutput(BaseModel):
    description: str
    name: str
    parameters: "ParameterSpecOutput"
    strict: Union[bool, None] = None


class FunctionToolInput(BaseModel):
    description: Optional[str] = None
    name: str
    parameters: Optional[dict[str, Any]] = None
    strict: Optional[bool] = None
    type: Literal["function"]


class FunctionToolOutput(BaseModel):
    description: Optional[str] = None
    name: str
    parameters: Optional[dict[str, Any]] = None
    strict: Optional[bool] = None
    type: Literal["function"]


class HTTPValidationErrorInput(BaseModel):
    detail: Optional[list["ValidationErrorInput"]] = None


class HTTPValidationErrorOutput(BaseModel):
    detail: Optional[list["ValidationErrorOutput"]] = None


class InlineSkillInput(BaseModel):
    description: str
    instructions: str
    name: str
    type: Literal["inline"]


class InlineSkillOutput(BaseModel):
    description: str
    instructions: str
    name: str
    type: Literal["inline"]


InputInput: TypeAlias = Union[str, list["InputItemInput"]]
InputOutput: TypeAlias = Union[str, list["InputItemOutput"]]
InputContentInput: TypeAlias = Union[str, list["InputContentPartInput"]]
InputContentOutput: TypeAlias = Union[str, list["InputContentPartOutput"]]


class InputContentPartInput(BaseModel):
    image_url: Optional[str] = None
    text: Optional[str] = None
    type: Literal["input_text", "input_image"]


class InputContentPartOutput(BaseModel):
    image_url: Optional[str] = None
    text: Optional[str] = None
    type: Literal["input_text", "input_image"]


InputItemInput: TypeAlias = Union[
    "InputMessageInput", "FunctionCallOutputInputInput", "FunctionCallInputInput"
]
InputItemOutput: TypeAlias = Union[
    "InputMessageOutput", "FunctionCallOutputInputOutput", "FunctionCallInputOutput"
]


class InputMessageInput(BaseModel):
    content: "InputContentInput"
    role: Literal["user", "assistant", "system", "developer"]
    type: Literal["message"]


class InputMessageOutput(BaseModel):
    content: "InputContentOutput"
    role: Literal["user", "assistant", "system", "developer"]
    type: Literal["message"]


class JSONSchemaInput(BaseModel):
    description: Union[str, None] = None
    name: Union[str, None] = None
    schema_: dict[str, Any] = Field(alias="schema")
    strict: Union[bool, None] = None


class JSONSchemaOutput(BaseModel):
    description: Union[str, None] = None
    name: Union[str, None] = None
    schema_: dict[str, Any] = Field(alias="schema")
    strict: Union[bool, None] = None


class JSONSchemaFormatInput(BaseModel):
    description: Optional[str] = None
    name: str
    schema_: dict[str, Any] = Field(alias="schema")
    strict: Optional[bool] = None


class JSONSchemaFormatOutput(BaseModel):
    description: Optional[str] = None
    name: str
    schema_: dict[str, Any] = Field(alias="schema")
    strict: Optional[bool] = None


class ListAsyncApiChatCompletionsResponseInput(BaseModel):
    next_token: Union[str, None] = None
    requests: list["AsyncApiChatCompletionsResponseSummaryInput"]


class ListAsyncApiChatCompletionsResponseOutput(BaseModel):
    next_token: Union[str, None] = None
    requests: list["AsyncApiChatCompletionsResponseSummaryOutput"]


class McpCallOutputItemInput(BaseModel):
    arguments: str
    error: Union[str, None] = None
    id: str
    name: str
    output: Optional[str] = None
    server_label: str
    type: Literal["mcp_call"]


class McpCallOutputItemOutput(BaseModel):
    arguments: str
    error: Union[str, None] = None
    id: str
    name: str
    output: Optional[str] = None
    server_label: str
    type: Literal["mcp_call"]


class McpListToolsOutputItemInput(BaseModel):
    error: Optional[str] = None
    id: str
    server_label: str
    tools: list["McpToolDefInput"]
    type: Literal["mcp_list_tools"]


class McpListToolsOutputItemOutput(BaseModel):
    error: Optional[str] = None
    id: str
    server_label: str
    tools: list["McpToolDefOutput"]
    type: Literal["mcp_list_tools"]


class McpToolInput(BaseModel):
    allowed_tools: Optional[list[str]] = None
    authorization: Optional[str] = None
    defer_loading: Optional[bool] = None
    headers: Optional[dict[str, str]] = None
    server_label: str
    server_url: str
    type: Literal["mcp"]


class McpToolOutput(BaseModel):
    allowed_tools: Optional[list[str]] = None
    authorization: Optional[str] = None
    defer_loading: Optional[bool] = None
    headers: Optional[dict[str, str]] = None
    server_label: str
    server_url: str
    type: Literal["mcp"]


class McpToolDefInput(BaseModel):
    description: Optional[str] = None
    input_schema: dict[str, Any]
    name: str


class McpToolDefOutput(BaseModel):
    description: Optional[str] = None
    input_schema: dict[str, Any]
    name: str


class MessageOutputItemInput(BaseModel):
    content: list["ContentPartInput"]
    id: str
    role: "RoleTypeInput"
    status: "StatusInput"
    type: Literal["message"]


class MessageOutputItemOutput(BaseModel):
    content: list["ContentPartOutput"]
    id: str
    role: "RoleTypeOutput"
    status: "StatusOutput"
    type: Literal["message"]


OutputItemInput: TypeAlias = Union[
    "MessageOutputItemInput",
    "SearchResultsOutputItemInput",
    "FetchUrlResultsOutputItemInput",
    "FunctionCallOutputItemInput",
    "McpListToolsOutputItemInput",
    "McpCallOutputItemInput",
    "SkillLoadedOutputItemInput",
    "AdvisorResultOutputItemInput",
    "SandboxResultsOutputItemInput",
    "SandboxWriteFileOutputItemInput",
    "SandboxReadFileOutputItemInput",
    "SandboxEditFileOutputItemInput",
    "SandboxGrepOutputItemInput",
    "SandboxGlobOutputItemInput",
    "SandboxApplyPatchOutputItemInput",
    "ShareFileOutputItemInput",
    "UnknownOutputItemInput",
]
OutputItemOutput: TypeAlias = Union[
    "MessageOutputItemOutput",
    "SearchResultsOutputItemOutput",
    "FetchUrlResultsOutputItemOutput",
    "FunctionCallOutputItemOutput",
    "McpListToolsOutputItemOutput",
    "McpCallOutputItemOutput",
    "SkillLoadedOutputItemOutput",
    "AdvisorResultOutputItemOutput",
    "SandboxResultsOutputItemOutput",
    "SandboxWriteFileOutputItemOutput",
    "SandboxReadFileOutputItemOutput",
    "SandboxEditFileOutputItemOutput",
    "SandboxGrepOutputItemOutput",
    "SandboxGlobOutputItemOutput",
    "SandboxApplyPatchOutputItemOutput",
    "ShareFileOutputItemOutput",
    "UnknownOutputItemOutput",
]


class OutputItemAddedEventInput(BaseModel):
    item: "OutputItemInput"
    output_index: int
    sequence_number: int
    type: Literal["response.output_item.added"]


class OutputItemAddedEventOutput(BaseModel):
    item: "OutputItemOutput"
    output_index: int
    sequence_number: int
    type: Literal["response.output_item.added"]


class OutputItemDoneEventInput(BaseModel):
    item: "OutputItemInput"
    output_index: int
    sequence_number: int
    type: Literal["response.output_item.done"]


class OutputItemDoneEventOutput(BaseModel):
    item: "OutputItemOutput"
    output_index: int
    sequence_number: int
    type: Literal["response.output_item.done"]


class ParameterSpecInput(BaseModel):
    additional_properties: Union[bool, None] = None
    properties: dict[str, Any]
    required: Union[list[str], None] = None
    type: str


class ParameterSpecOutput(BaseModel):
    additional_properties: Union[bool, None] = None
    properties: dict[str, Any]
    required: Union[list[str], None] = None
    type: str


class PeopleSearchToolInput(BaseModel):
    type: Literal["people_search"]


class PeopleSearchToolOutput(BaseModel):
    type: Literal["people_search"]


class ReasoningConfigInput(BaseModel):
    effort: Optional[Literal["minimal", "low", "medium", "high", "xhigh"]] = None


class ReasoningConfigOutput(BaseModel):
    effort: Optional[Literal["minimal", "low", "medium", "high", "xhigh"]] = None


class ReasoningStartedEventInput(BaseModel):
    sequence_number: int
    thought: Optional[str] = None
    type: Literal["response.reasoning.started"]


class ReasoningStartedEventOutput(BaseModel):
    sequence_number: int
    thought: Optional[str] = None
    type: Literal["response.reasoning.started"]


class ReasoningStepInputInput(BaseModel):
    execute_python: Union["ExecutePythonStepDetailsInput", None] = None
    fetch_url_content: Union["FetchUrlContentStepDetailsInput", None] = None
    thought: str
    type: Union[str, None] = None
    web_search: Union["WebSearchStepDetailsInput", None] = None


class ReasoningStepInputOutput(BaseModel):
    execute_python: Union["ExecutePythonStepDetailsOutput", None] = None
    fetch_url_content: Union["FetchUrlContentStepDetailsOutput", None] = None
    thought: str
    type: Union[str, None] = None
    web_search: Union["WebSearchStepDetailsOutput", None] = None


class ReasoningStepOutputInput(BaseModel):
    execute_python: Union["ExecutePythonStepDetailsInput", None] = None
    fetch_url_content: Union["FetchUrlContentStepDetailsInput", None] = None
    thought: str
    type: Union[str, None] = None
    web_search: Union["WebSearchStepDetailsInput", None] = None


class ReasoningStepOutputOutput(BaseModel):
    execute_python: Union["ExecutePythonStepDetailsOutput", None] = None
    fetch_url_content: Union["FetchUrlContentStepDetailsOutput", None] = None
    thought: str
    type: Union[str, None] = None
    web_search: Union["WebSearchStepDetailsOutput", None] = None


class ReasoningStoppedEventInput(BaseModel):
    sequence_number: int
    thought: Optional[str] = None
    type: Literal["response.reasoning.stopped"]


class ReasoningStoppedEventOutput(BaseModel):
    sequence_number: int
    thought: Optional[str] = None
    type: Literal["response.reasoning.stopped"]


class RegexSchemaInput(BaseModel):
    description: Union[str, None] = None
    name: Union[str, None] = None
    regex: str
    strict: Union[bool, None] = None


class RegexSchemaOutput(BaseModel):
    description: Union[str, None] = None
    name: Union[str, None] = None
    regex: str
    strict: Union[bool, None] = None


class ResponseCompletedEventInput(BaseModel):
    response: Optional["ResponsesResponseInput"] = None
    sequence_number: int
    type: Literal["response.completed"]


class ResponseCompletedEventOutput(BaseModel):
    response: Optional["ResponsesResponseOutput"] = None
    sequence_number: int
    type: Literal["response.completed"]


class ResponseCreatedEventInput(BaseModel):
    response: Optional["ResponsesResponseInput"] = None
    sequence_number: int
    type: Literal["response.created"]


class ResponseCreatedEventOutput(BaseModel):
    response: Optional["ResponsesResponseOutput"] = None
    sequence_number: int
    type: Literal["response.created"]


class ResponseFailedEventInput(BaseModel):
    error: "ErrorInfoInput"
    sequence_number: int
    type: Literal["response.failed"]


class ResponseFailedEventOutput(BaseModel):
    error: "ErrorInfoOutput"
    sequence_number: int
    type: Literal["response.failed"]


class ResponseFileInput(BaseModel):
    bytes: int
    created_at: int
    filename: str
    id: str
    object: Literal["file"]


class ResponseFileOutput(BaseModel):
    bytes: int
    created_at: int
    filename: str
    id: str
    object: Literal["file"]


class ResponseFileListInput(BaseModel):
    data: list["ResponseFileInput"]
    object: Literal["list"]


class ResponseFileListOutput(BaseModel):
    data: list["ResponseFileOutput"]
    object: Literal["list"]


class ResponseFormatInput(BaseModel):
    json_schema: Optional["JSONSchemaFormatInput"] = None
    type: Literal["json_schema"]


class ResponseFormatOutput(BaseModel):
    json_schema: Optional["JSONSchemaFormatOutput"] = None
    type: Literal["json_schema"]


class ResponseFormatJSONSchemaInput(BaseModel):
    json_schema: "JSONSchemaInput"
    type: Literal["json_schema"]


class ResponseFormatJSONSchemaOutput(BaseModel):
    json_schema: "JSONSchemaOutput"
    type: Literal["json_schema"]


class ResponseFormatRegexInput(BaseModel):
    regex: "RegexSchemaInput"
    type: Literal["regex"]


class ResponseFormatRegexOutput(BaseModel):
    regex: "RegexSchemaOutput"
    type: Literal["regex"]


class ResponseFormatTextInput(BaseModel):
    type: Literal["text"]


class ResponseFormatTextOutput(BaseModel):
    type: Literal["text"]


class ResponseInProgressEventInput(BaseModel):
    response: Optional["ResponsesResponseInput"] = None
    sequence_number: int
    type: Literal["response.in_progress"]


class ResponseInProgressEventOutput(BaseModel):
    response: Optional["ResponsesResponseOutput"] = None
    sequence_number: int
    type: Literal["response.in_progress"]


class ResponseSkillLoadedEventInput(BaseModel):
    name: str
    sequence_number: int
    type: Literal["response.skill.loaded"]


class ResponseSkillLoadedEventOutput(BaseModel):
    name: str
    sequence_number: int
    type: Literal["response.skill.loaded"]


ResponseStreamEventInput: TypeAlias = Union[
    "ResponseCreatedEventInput",
    "ResponseInProgressEventInput",
    "ResponseCompletedEventInput",
    "ResponseFailedEventInput",
    "OutputItemAddedEventInput",
    "OutputItemDoneEventInput",
    "TextDeltaEventInput",
    "TextDoneEventInput",
    "ReasoningStartedEventInput",
    "SearchQueriesEventInput",
    "SearchResultsEventInput",
    "FetchUrlQueriesEventInput",
    "FetchUrlResultsEventInput",
    "ReasoningStoppedEventInput",
    "ResponseSkillLoadedEventInput",
]
ResponseStreamEventOutput: TypeAlias = Union[
    "ResponseCreatedEventOutput",
    "ResponseInProgressEventOutput",
    "ResponseCompletedEventOutput",
    "ResponseFailedEventOutput",
    "OutputItemAddedEventOutput",
    "OutputItemDoneEventOutput",
    "TextDeltaEventOutput",
    "TextDoneEventOutput",
    "ReasoningStartedEventOutput",
    "SearchQueriesEventOutput",
    "SearchResultsEventOutput",
    "FetchUrlQueriesEventOutput",
    "FetchUrlResultsEventOutput",
    "ReasoningStoppedEventOutput",
    "ResponseSkillLoadedEventOutput",
]


class ResponsesCostInput(BaseModel):
    cache_creation_cost: Optional[float] = None
    cache_read_cost: Optional[float] = None
    currency: "CurrencyInput"
    input_cost: float
    output_cost: float
    tool_calls_cost: Optional[float] = None
    total_cost: float


class ResponsesCostOutput(BaseModel):
    cache_creation_cost: Optional[float] = None
    cache_read_cost: Optional[float] = None
    currency: "CurrencyOutput"
    input_cost: float
    output_cost: float
    tool_calls_cost: Optional[float] = None
    total_cost: float


ResponsesObjectTypeInput: TypeAlias = Literal["response"]
ResponsesObjectTypeOutput: TypeAlias = Literal["response"]


class ResponsesRequestInput(BaseModel):
    background: Union[bool, None] = None
    input: "InputInput"
    instructions: Optional[str] = None
    language_preference: Optional[str] = None
    max_output_tokens: Optional[int] = None
    max_steps: Optional[int] = None
    model: Optional[str] = None
    models: Optional[list[str]] = None
    preset: Optional[str] = None
    previous_response_id: Optional[str] = None
    reasoning: Optional["ReasoningConfigInput"] = None
    response_format: Optional["ResponseFormatInput"] = None
    skills: Optional[list["SkillInput"]] = None
    store: Optional[bool] = None
    stream: Optional[bool] = None
    temperature: Optional[float] = None
    tools: Optional[list["ToolInput"]] = None
    top_p: Optional[float] = None


class ResponsesRequestOutput(BaseModel):
    background: Union[bool, None] = None
    input: "InputOutput"
    instructions: Optional[str] = None
    language_preference: Optional[str] = None
    max_output_tokens: Optional[int] = None
    max_steps: Optional[int] = None
    model: Optional[str] = None
    models: Optional[list[str]] = None
    preset: Optional[str] = None
    previous_response_id: Optional[str] = None
    reasoning: Optional["ReasoningConfigOutput"] = None
    response_format: Optional["ResponseFormatOutput"] = None
    skills: Optional[list["SkillOutput"]] = None
    store: Optional[bool] = None
    stream: Optional[bool] = None
    temperature: Optional[float] = None
    tools: Optional[list["ToolOutput"]] = None
    top_p: Optional[float] = None


class ResponsesResponseInput(BaseModel):
    background: Optional[bool] = None
    created_at: int
    error: Optional["ErrorInfoInput"] = None
    id: str
    model: str
    object: "ResponsesObjectTypeInput"
    output: list["OutputItemInput"]
    previous_response_id: Union[str, None] = None
    status: "StatusInput"
    store: Optional[bool] = None
    usage: Optional["ResponsesUsageInput"] = None


class ResponsesResponseOutput(BaseModel):
    background: Optional[bool] = None
    created_at: int
    error: Optional["ErrorInfoOutput"] = None
    id: str
    model: str
    object: "ResponsesObjectTypeOutput"
    output: list["OutputItemOutput"]
    previous_response_id: Union[str, None] = None
    status: "StatusOutput"
    store: Optional[bool] = None
    usage: Optional["ResponsesUsageOutput"] = None

    @property
    def output_text(self) -> str:
        return "".join(
            content.text
            for item in self.output
            if isinstance(item, MessageOutputItemOutput)
            for content in item.content
            if content.type == "output_text"
        )


class ResponsesUsageInput(BaseModel):
    cost: Optional["ResponsesCostInput"] = None
    input_tokens: int
    input_tokens_details: Optional["ResponsesUsageInputTokensDetailsInput"] = None
    output_tokens: int
    tool_calls_details: Optional[dict[str, "ToolCallDetailsInput"]] = None
    total_tokens: int


class ResponsesUsageOutput(BaseModel):
    cost: Optional["ResponsesCostOutput"] = None
    input_tokens: int
    input_tokens_details: Optional["ResponsesUsageInputTokensDetailsOutput"] = None
    output_tokens: int
    tool_calls_details: Optional[dict[str, "ToolCallDetailsOutput"]] = None
    total_tokens: int


class ResponsesUsageInputTokensDetailsInput(BaseModel):
    cache_creation_input_tokens: Optional[int] = None
    cache_read_input_tokens: Optional[int] = None


class ResponsesUsageInputTokensDetailsOutput(BaseModel):
    cache_creation_input_tokens: Optional[int] = None
    cache_read_input_tokens: Optional[int] = None


RoleTypeInput: TypeAlias = Literal["assistant"]
RoleTypeOutput: TypeAlias = Literal["assistant"]


class SandboxApplyPatchOutputItemInput(BaseModel):
    added: Optional[list[str]] = None
    call_id: str
    deleted: Optional[list[str]] = None
    error: Optional[str] = None
    modified: Optional[list[str]] = None
    type: Literal["sandbox_apply_patch"]


class SandboxApplyPatchOutputItemOutput(BaseModel):
    added: Optional[list[str]] = None
    call_id: str
    deleted: Optional[list[str]] = None
    error: Optional[str] = None
    modified: Optional[list[str]] = None
    type: Literal["sandbox_apply_patch"]


class SandboxEditFileOutputItemInput(BaseModel):
    call_id: str
    error: Optional[str] = None
    file_path: Optional[str] = None
    message: Optional[str] = None
    type: Literal["sandbox_edit_file"]


class SandboxEditFileOutputItemOutput(BaseModel):
    call_id: str
    error: Optional[str] = None
    file_path: Optional[str] = None
    message: Optional[str] = None
    type: Literal["sandbox_edit_file"]


class SandboxGlobOutputItemInput(BaseModel):
    call_id: str
    count: Optional[int] = None
    error: Optional[str] = None
    files: Optional[list[str]] = None
    truncated: Optional[bool] = None
    type: Literal["sandbox_glob"]


class SandboxGlobOutputItemOutput(BaseModel):
    call_id: str
    count: Optional[int] = None
    error: Optional[str] = None
    files: Optional[list[str]] = None
    truncated: Optional[bool] = None
    type: Literal["sandbox_glob"]


class SandboxGrepOutputItemInput(BaseModel):
    call_id: str
    count: Optional[int] = None
    error: Optional[str] = None
    files: Optional[list[str]] = None
    truncated: Optional[bool] = None
    type: Literal["sandbox_grep"]


class SandboxGrepOutputItemOutput(BaseModel):
    call_id: str
    count: Optional[int] = None
    error: Optional[str] = None
    files: Optional[list[str]] = None
    truncated: Optional[bool] = None
    type: Literal["sandbox_grep"]


class SandboxReadFileOutputItemInput(BaseModel):
    call_id: str
    content: Optional[str] = None
    error: Optional[str] = None
    file_path: str
    start_line: Optional[int] = None
    total_lines: Optional[int] = None
    type: Literal["sandbox_read_file"]


class SandboxReadFileOutputItemOutput(BaseModel):
    call_id: str
    content: Optional[str] = None
    error: Optional[str] = None
    file_path: str
    start_line: Optional[int] = None
    total_lines: Optional[int] = None
    type: Literal["sandbox_read_file"]


class SandboxResultInput(BaseModel):
    duration_ms: int
    exit_code: int
    status: Literal["in_progress", "completed", "failed", "timed_out"]
    stderr: str
    stdout: str


class SandboxResultOutput(BaseModel):
    duration_ms: int
    exit_code: int
    status: Literal["in_progress", "completed", "failed", "timed_out"]
    stderr: str
    stdout: str


class SandboxResultsOutputItemInput(BaseModel):
    call_id: str
    code: str
    container_id: Optional[str] = None
    language: Literal["python", "bash"]
    results: list["SandboxResultInput"]
    status: Literal["in_progress", "completed", "failed", "timed_out"]
    type: Literal["sandbox_results"]


class SandboxResultsOutputItemOutput(BaseModel):
    call_id: str
    code: str
    container_id: Optional[str] = None
    language: Literal["python", "bash"]
    results: list["SandboxResultOutput"]
    status: Literal["in_progress", "completed", "failed", "timed_out"]
    type: Literal["sandbox_results"]


class SandboxToolInput(BaseModel):
    type: Literal["sandbox"]


class SandboxToolOutput(BaseModel):
    type: Literal["sandbox"]


class SandboxWriteFileOutputItemInput(BaseModel):
    call_id: str
    error: Optional[str] = None
    file_path: str
    size_bytes: Optional[int] = None
    type: Literal["sandbox_write_file"]


class SandboxWriteFileOutputItemOutput(BaseModel):
    call_id: str
    error: Optional[str] = None
    file_path: str
    size_bytes: Optional[int] = None
    type: Literal["sandbox_write_file"]


class SearchDomainFilterInput(BaseModel):
    search_domain_filter: Optional[list[str]] = None


class SearchDomainFilterOutput(BaseModel):
    search_domain_filter: Optional[list[str]] = None


class SearchQueriesEventInput(BaseModel):
    queries: list[str]
    sequence_number: int
    thought: Optional[str] = None
    type: Literal["response.reasoning.search_queries"]


class SearchQueriesEventOutput(BaseModel):
    queries: list[str]
    sequence_number: int
    thought: Optional[str] = None
    type: Literal["response.reasoning.search_queries"]


SearchRecencyFilterInput: TypeAlias = Literal["hour", "day", "week", "month", "year"]
SearchRecencyFilterOutput: TypeAlias = Literal["hour", "day", "week", "month", "year"]


class SearchResultInput(BaseModel):
    date: Optional[str] = None
    id: int
    last_updated: Optional[str] = None
    snippet: str
    source: Optional["SearchSourceInput"] = None
    title: str
    url: str


class SearchResultOutput(BaseModel):
    date: Optional[str] = None
    id: int
    last_updated: Optional[str] = None
    snippet: str
    source: Optional["SearchSourceOutput"] = None
    title: str
    url: str


class SearchResultsEventInput(BaseModel):
    results: list["SearchResultInput"]
    sequence_number: int
    thought: Optional[str] = None
    type: Literal["response.reasoning.search_results"]
    usage: Optional["ResponsesUsageInput"] = None


class SearchResultsEventOutput(BaseModel):
    results: list["SearchResultOutput"]
    sequence_number: int
    thought: Optional[str] = None
    type: Literal["response.reasoning.search_results"]
    usage: Optional["ResponsesUsageOutput"] = None


class SearchResultsOutputItemInput(BaseModel):
    queries: Optional[list[str]] = None
    results: list["SearchResultInput"]
    type: Literal["search_results"]


class SearchResultsOutputItemOutput(BaseModel):
    queries: Optional[list[str]] = None
    results: list["SearchResultOutput"]
    type: Literal["search_results"]


SearchSourceInput: TypeAlias = Literal["web"]
SearchSourceOutput: TypeAlias = Literal["web"]


class ShareFileOutputItemInput(BaseModel):
    call_id: str
    error: Optional[str] = None
    file_id: Optional[str] = None
    filename: Optional[str] = None
    size_bytes: Optional[int] = None
    type: Literal["share_file"]
    url: Optional[str] = None


class ShareFileOutputItemOutput(BaseModel):
    call_id: str
    error: Optional[str] = None
    file_id: Optional[str] = None
    filename: Optional[str] = None
    size_bytes: Optional[int] = None
    type: Literal["share_file"]
    url: Optional[str] = None


SkillInput: TypeAlias = Union["BuiltinSkillInput", "InlineSkillInput"]
SkillOutput: TypeAlias = Union["BuiltinSkillOutput", "InlineSkillOutput"]


class SkillLoadedOutputItemInput(BaseModel):
    name: str
    type: Literal["skill_loaded"]


class SkillLoadedOutputItemOutput(BaseModel):
    name: str
    type: Literal["skill_loaded"]


StatusInput: TypeAlias = Literal[
    "completed", "failed", "in_progress", "queued", "cancelled", "requires_action"
]
StatusOutput: TypeAlias = Literal[
    "completed", "failed", "in_progress", "queued", "cancelled", "requires_action"
]


class TextDeltaEventInput(BaseModel):
    content_index: int
    delta: str
    item_id: str
    output_index: int
    sequence_number: int
    type: Literal["response.output_text.delta"]


class TextDeltaEventOutput(BaseModel):
    content_index: int
    delta: str
    item_id: str
    output_index: int
    sequence_number: int
    type: Literal["response.output_text.delta"]


class TextDoneEventInput(BaseModel):
    content_index: int
    item_id: str
    output_index: int
    sequence_number: int
    text: str
    type: Literal["response.output_text.done"]


class TextDoneEventOutput(BaseModel):
    content_index: int
    item_id: str
    output_index: int
    sequence_number: int
    text: str
    type: Literal["response.output_text.done"]


ToolInput: TypeAlias = Union[
    "WebSearchToolInput",
    "FetchUrlToolInput",
    "PeopleSearchToolInput",
    "FunctionToolInput",
    "FinanceSearchToolInput",
    "SandboxToolInput",
    "McpToolInput",
]
ToolOutput: TypeAlias = Union[
    "WebSearchToolOutput",
    "FetchUrlToolOutput",
    "PeopleSearchToolOutput",
    "FunctionToolOutput",
    "FinanceSearchToolOutput",
    "SandboxToolOutput",
    "McpToolOutput",
]


class ToolCallInput(BaseModel):
    function: Union["ToolCallFunctionInput", None] = None
    id: Union[str, None] = None
    type: Union[Literal["function"], None] = None


class ToolCallOutput(BaseModel):
    function: Union["ToolCallFunctionOutput", None] = None
    id: Union[str, None] = None
    type: Union[Literal["function"], None] = None


class ToolCallDetailsInput(BaseModel):
    invocation: Optional[int] = None


class ToolCallDetailsOutput(BaseModel):
    invocation: Optional[int] = None


class ToolCallFunctionInput(BaseModel):
    arguments: Union[str, None] = None
    name: Union[str, None] = None


class ToolCallFunctionOutput(BaseModel):
    arguments: Union[str, None] = None
    name: Union[str, None] = None


class ToolSpecInput(BaseModel):
    function: "FunctionSpecInput"
    type: Literal["function"]


class ToolSpecOutput(BaseModel):
    function: "FunctionSpecOutput"
    type: Literal["function"]


class ToolUserLocationInput(BaseModel):
    city: Optional[str] = None
    country: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    region: Optional[str] = None


class ToolUserLocationOutput(BaseModel):
    city: Optional[str] = None
    country: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    region: Optional[str] = None


class URLInput(BaseModel):
    url: str


class URLOutput(BaseModel):
    url: str


class UnknownOutputItemInput(BaseModel):
    item_name: str
    payload: dict[str, Any]
    type: Literal["unknown"]


class UnknownOutputItemOutput(BaseModel):
    item_name: str
    payload: dict[str, Any]
    type: Literal["unknown"]


class UrlContentInput(BaseModel):
    snippet: str
    title: str
    url: str


class UrlContentOutput(BaseModel):
    snippet: str
    title: str
    url: str


class UsageInfoInput(BaseModel):
    citation_tokens: Union[int, None] = None
    completion_tokens: int
    cost: "CostInput"
    num_search_queries: Union[int, None] = None
    prompt_tokens: int
    reasoning_tokens: Union[int, None] = None
    search_context_size: Union[str, None] = None
    total_tokens: int


class UsageInfoOutput(BaseModel):
    citation_tokens: Union[int, None] = None
    completion_tokens: int
    cost: "CostOutput"
    num_search_queries: Union[int, None] = None
    prompt_tokens: int
    reasoning_tokens: Union[int, None] = None
    search_context_size: Union[str, None] = None
    total_tokens: int


class UserLocationInput(BaseModel):
    city: Union[str, None] = None
    country: Union[str, None] = None
    latitude: Union[float, None] = None
    longitude: Union[float, None] = None
    region: Union[str, None] = None


class UserLocationOutput(BaseModel):
    city: Union[str, None] = None
    country: Union[str, None] = None
    latitude: Union[float, None] = None
    longitude: Union[float, None] = None
    region: Union[str, None] = None


class ValidationErrorInput(BaseModel):
    loc: list[Union[str, int]]
    msg: str
    type: str


class ValidationErrorOutput(BaseModel):
    loc: list[Union[str, int]]
    msg: str
    type: str


class VideoURLInput(BaseModel):
    frame_interval: Optional[Union[str, int]] = None
    url: str


class VideoURLOutput(BaseModel):
    frame_interval: Optional[Union[str, int]] = None
    url: str


class WebSearchFiltersInput(BaseModel):
    search_domain_filter: Optional[list[str]] = None
    last_updated_after_filter: Optional["DateInput"] = None
    last_updated_before_filter: Optional["DateInput"] = None
    search_after_date_filter: Optional["DateInput"] = None
    search_before_date_filter: Optional["DateInput"] = None
    search_recency_filter: Optional["SearchRecencyFilterInput"] = None


class WebSearchFiltersOutput(BaseModel):
    search_domain_filter: Optional[list[str]] = None
    last_updated_after_filter: Optional["DateOutput"] = None
    last_updated_before_filter: Optional["DateOutput"] = None
    search_after_date_filter: Optional["DateOutput"] = None
    search_before_date_filter: Optional["DateOutput"] = None
    search_recency_filter: Optional["SearchRecencyFilterOutput"] = None


class WebSearchOptionsInput(BaseModel):
    image_results_enhanced_relevance: Optional[bool] = None
    search_context_size: Optional[Literal["low", "medium", "high"]] = None
    search_type: Union[Literal["fast", "pro", "auto"], None] = None
    user_location: Union["UserLocationInput", None] = None


class WebSearchOptionsOutput(BaseModel):
    image_results_enhanced_relevance: Optional[bool] = None
    search_context_size: Optional[Literal["low", "medium", "high"]] = None
    search_type: Union[Literal["fast", "pro", "auto"], None] = None
    user_location: Union["UserLocationOutput", None] = None


class WebSearchStepDetailsInput(BaseModel):
    search_keywords: list[str]
    search_results: list["ApiPublicSearchResultInput"]


class WebSearchStepDetailsOutput(BaseModel):
    search_keywords: list[str]
    search_results: list["ApiPublicSearchResultOutput"]


class WebSearchToolInput(BaseModel):
    filters: Optional["WebSearchFiltersInput"] = None
    max_tokens: Optional[int] = None
    max_tokens_per_page: Optional[int] = None
    search_context_size: Optional[Literal["low", "medium", "high"]] = None
    type: Literal["web_search"]
    user_location: Optional["ToolUserLocationInput"] = None


class WebSearchToolOutput(BaseModel):
    filters: Optional["WebSearchFiltersOutput"] = None
    max_tokens: Optional[int] = None
    max_tokens_per_page: Optional[int] = None
    search_context_size: Optional[Literal["low", "medium", "high"]] = None
    type: Literal["web_search"]
    user_location: Optional["ToolUserLocationOutput"] = None


class ResponsesCancelResponseOutput(BaseModel):
    response_id: str
    status: Literal["cancelling"]


AdvisorResultOutputItemInput.model_rebuild(_types_namespace=globals())
AdvisorResultOutputItemOutput.model_rebuild(_types_namespace=globals())
AnnotationInput.model_rebuild(_types_namespace=globals())
AnnotationOutput.model_rebuild(_types_namespace=globals())
ApiChatCompletionsRequestInput.model_rebuild(_types_namespace=globals())
ApiChatCompletionsRequestOutput.model_rebuild(_types_namespace=globals())
ApiPublicSearchResultInput.model_rebuild(_types_namespace=globals())
ApiPublicSearchResultOutput.model_rebuild(_types_namespace=globals())
ApiSearchPageInput.model_rebuild(_types_namespace=globals())
ApiSearchPageOutput.model_rebuild(_types_namespace=globals())
ApiSearchRequestInput.model_rebuild(_types_namespace=globals())
ApiSearchRequestOutput.model_rebuild(_types_namespace=globals())
ApiSearchResponseInput.model_rebuild(_types_namespace=globals())
ApiSearchResponseOutput.model_rebuild(_types_namespace=globals())
AsyncApiChatCompletionsRequestInput.model_rebuild(_types_namespace=globals())
AsyncApiChatCompletionsRequestOutput.model_rebuild(_types_namespace=globals())
AsyncApiChatCompletionsResponseInput.model_rebuild(_types_namespace=globals())
AsyncApiChatCompletionsResponseOutput.model_rebuild(_types_namespace=globals())
AsyncApiChatCompletionsResponseSummaryInput.model_rebuild(_types_namespace=globals())
AsyncApiChatCompletionsResponseSummaryOutput.model_rebuild(_types_namespace=globals())
BrowserSessionResponseInput.model_rebuild(_types_namespace=globals())
BrowserSessionResponseOutput.model_rebuild(_types_namespace=globals())
BuiltinSkillInput.model_rebuild(_types_namespace=globals())
BuiltinSkillOutput.model_rebuild(_types_namespace=globals())
ChatMessageInputInput.model_rebuild(_types_namespace=globals())
ChatMessageInputOutput.model_rebuild(_types_namespace=globals())
ChatMessageOutputInput.model_rebuild(_types_namespace=globals())
ChatMessageOutputOutput.model_rebuild(_types_namespace=globals())
ChatMessageContentFileChunkInput.model_rebuild(_types_namespace=globals())
ChatMessageContentFileChunkOutput.model_rebuild(_types_namespace=globals())
ChatMessageContentImageChunkInput.model_rebuild(_types_namespace=globals())
ChatMessageContentImageChunkOutput.model_rebuild(_types_namespace=globals())
ChatMessageContentPDFChunkInput.model_rebuild(_types_namespace=globals())
ChatMessageContentPDFChunkOutput.model_rebuild(_types_namespace=globals())
ChatMessageContentTextChunkInput.model_rebuild(_types_namespace=globals())
ChatMessageContentTextChunkOutput.model_rebuild(_types_namespace=globals())
ChatMessageContentVideoChunkInput.model_rebuild(_types_namespace=globals())
ChatMessageContentVideoChunkOutput.model_rebuild(_types_namespace=globals())
ChoiceInput.model_rebuild(_types_namespace=globals())
ChoiceOutput.model_rebuild(_types_namespace=globals())
CompletionResponseInput.model_rebuild(_types_namespace=globals())
CompletionResponseOutput.model_rebuild(_types_namespace=globals())
ContentPartInput.model_rebuild(_types_namespace=globals())
ContentPartOutput.model_rebuild(_types_namespace=globals())
ContextualizedEmbeddingObjectInput.model_rebuild(_types_namespace=globals())
ContextualizedEmbeddingObjectOutput.model_rebuild(_types_namespace=globals())
ContextualizedEmbeddingsRequestInput.model_rebuild(_types_namespace=globals())
ContextualizedEmbeddingsRequestOutput.model_rebuild(_types_namespace=globals())
ContextualizedEmbeddingsResponseInput.model_rebuild(_types_namespace=globals())
ContextualizedEmbeddingsResponseOutput.model_rebuild(_types_namespace=globals())
CostInput.model_rebuild(_types_namespace=globals())
CostOutput.model_rebuild(_types_namespace=globals())
CreateBrowserSessionRequestInput.model_rebuild(_types_namespace=globals())
CreateBrowserSessionRequestOutput.model_rebuild(_types_namespace=globals())
DateFiltersInput.model_rebuild(_types_namespace=globals())
DateFiltersOutput.model_rebuild(_types_namespace=globals())
EmbeddingObjectInput.model_rebuild(_types_namespace=globals())
EmbeddingObjectOutput.model_rebuild(_types_namespace=globals())
EmbeddingsRequestInput.model_rebuild(_types_namespace=globals())
EmbeddingsRequestOutput.model_rebuild(_types_namespace=globals())
EmbeddingsResponseInput.model_rebuild(_types_namespace=globals())
EmbeddingsResponseOutput.model_rebuild(_types_namespace=globals())
EmbeddingsUsageInput.model_rebuild(_types_namespace=globals())
EmbeddingsUsageOutput.model_rebuild(_types_namespace=globals())
EmbeddingsUsageCostInput.model_rebuild(_types_namespace=globals())
EmbeddingsUsageCostOutput.model_rebuild(_types_namespace=globals())
ErrorInfoInput.model_rebuild(_types_namespace=globals())
ErrorInfoOutput.model_rebuild(_types_namespace=globals())
ExecutePythonStepDetailsInput.model_rebuild(_types_namespace=globals())
ExecutePythonStepDetailsOutput.model_rebuild(_types_namespace=globals())
FetchUrlContentStepDetailsInput.model_rebuild(_types_namespace=globals())
FetchUrlContentStepDetailsOutput.model_rebuild(_types_namespace=globals())
FetchUrlQueriesEventInput.model_rebuild(_types_namespace=globals())
FetchUrlQueriesEventOutput.model_rebuild(_types_namespace=globals())
FetchUrlResultsEventInput.model_rebuild(_types_namespace=globals())
FetchUrlResultsEventOutput.model_rebuild(_types_namespace=globals())
FetchUrlResultsOutputItemInput.model_rebuild(_types_namespace=globals())
FetchUrlResultsOutputItemOutput.model_rebuild(_types_namespace=globals())
FetchUrlToolInput.model_rebuild(_types_namespace=globals())
FetchUrlToolOutput.model_rebuild(_types_namespace=globals())
FinanceSearchToolInput.model_rebuild(_types_namespace=globals())
FinanceSearchToolOutput.model_rebuild(_types_namespace=globals())
FunctionCallInputInput.model_rebuild(_types_namespace=globals())
FunctionCallInputOutput.model_rebuild(_types_namespace=globals())
FunctionCallOutputInputInput.model_rebuild(_types_namespace=globals())
FunctionCallOutputInputOutput.model_rebuild(_types_namespace=globals())
FunctionCallOutputItemInput.model_rebuild(_types_namespace=globals())
FunctionCallOutputItemOutput.model_rebuild(_types_namespace=globals())
FunctionSpecInput.model_rebuild(_types_namespace=globals())
FunctionSpecOutput.model_rebuild(_types_namespace=globals())
FunctionToolInput.model_rebuild(_types_namespace=globals())
FunctionToolOutput.model_rebuild(_types_namespace=globals())
HTTPValidationErrorInput.model_rebuild(_types_namespace=globals())
HTTPValidationErrorOutput.model_rebuild(_types_namespace=globals())
InlineSkillInput.model_rebuild(_types_namespace=globals())
InlineSkillOutput.model_rebuild(_types_namespace=globals())
InputContentPartInput.model_rebuild(_types_namespace=globals())
InputContentPartOutput.model_rebuild(_types_namespace=globals())
InputMessageInput.model_rebuild(_types_namespace=globals())
InputMessageOutput.model_rebuild(_types_namespace=globals())
JSONSchemaInput.model_rebuild(_types_namespace=globals())
JSONSchemaOutput.model_rebuild(_types_namespace=globals())
JSONSchemaFormatInput.model_rebuild(_types_namespace=globals())
JSONSchemaFormatOutput.model_rebuild(_types_namespace=globals())
ListAsyncApiChatCompletionsResponseInput.model_rebuild(_types_namespace=globals())
ListAsyncApiChatCompletionsResponseOutput.model_rebuild(_types_namespace=globals())
McpCallOutputItemInput.model_rebuild(_types_namespace=globals())
McpCallOutputItemOutput.model_rebuild(_types_namespace=globals())
McpListToolsOutputItemInput.model_rebuild(_types_namespace=globals())
McpListToolsOutputItemOutput.model_rebuild(_types_namespace=globals())
McpToolInput.model_rebuild(_types_namespace=globals())
McpToolOutput.model_rebuild(_types_namespace=globals())
McpToolDefInput.model_rebuild(_types_namespace=globals())
McpToolDefOutput.model_rebuild(_types_namespace=globals())
MessageOutputItemInput.model_rebuild(_types_namespace=globals())
MessageOutputItemOutput.model_rebuild(_types_namespace=globals())
OutputItemAddedEventInput.model_rebuild(_types_namespace=globals())
OutputItemAddedEventOutput.model_rebuild(_types_namespace=globals())
OutputItemDoneEventInput.model_rebuild(_types_namespace=globals())
OutputItemDoneEventOutput.model_rebuild(_types_namespace=globals())
ParameterSpecInput.model_rebuild(_types_namespace=globals())
ParameterSpecOutput.model_rebuild(_types_namespace=globals())
PeopleSearchToolInput.model_rebuild(_types_namespace=globals())
PeopleSearchToolOutput.model_rebuild(_types_namespace=globals())
ReasoningConfigInput.model_rebuild(_types_namespace=globals())
ReasoningConfigOutput.model_rebuild(_types_namespace=globals())
ReasoningStartedEventInput.model_rebuild(_types_namespace=globals())
ReasoningStartedEventOutput.model_rebuild(_types_namespace=globals())
ReasoningStepInputInput.model_rebuild(_types_namespace=globals())
ReasoningStepInputOutput.model_rebuild(_types_namespace=globals())
ReasoningStepOutputInput.model_rebuild(_types_namespace=globals())
ReasoningStepOutputOutput.model_rebuild(_types_namespace=globals())
ReasoningStoppedEventInput.model_rebuild(_types_namespace=globals())
ReasoningStoppedEventOutput.model_rebuild(_types_namespace=globals())
RegexSchemaInput.model_rebuild(_types_namespace=globals())
RegexSchemaOutput.model_rebuild(_types_namespace=globals())
ResponseCompletedEventInput.model_rebuild(_types_namespace=globals())
ResponseCompletedEventOutput.model_rebuild(_types_namespace=globals())
ResponseCreatedEventInput.model_rebuild(_types_namespace=globals())
ResponseCreatedEventOutput.model_rebuild(_types_namespace=globals())
ResponseFailedEventInput.model_rebuild(_types_namespace=globals())
ResponseFailedEventOutput.model_rebuild(_types_namespace=globals())
ResponseFileInput.model_rebuild(_types_namespace=globals())
ResponseFileOutput.model_rebuild(_types_namespace=globals())
ResponseFileListInput.model_rebuild(_types_namespace=globals())
ResponseFileListOutput.model_rebuild(_types_namespace=globals())
ResponseFormatInput.model_rebuild(_types_namespace=globals())
ResponseFormatOutput.model_rebuild(_types_namespace=globals())
ResponseFormatJSONSchemaInput.model_rebuild(_types_namespace=globals())
ResponseFormatJSONSchemaOutput.model_rebuild(_types_namespace=globals())
ResponseFormatRegexInput.model_rebuild(_types_namespace=globals())
ResponseFormatRegexOutput.model_rebuild(_types_namespace=globals())
ResponseFormatTextInput.model_rebuild(_types_namespace=globals())
ResponseFormatTextOutput.model_rebuild(_types_namespace=globals())
ResponseInProgressEventInput.model_rebuild(_types_namespace=globals())
ResponseInProgressEventOutput.model_rebuild(_types_namespace=globals())
ResponseSkillLoadedEventInput.model_rebuild(_types_namespace=globals())
ResponseSkillLoadedEventOutput.model_rebuild(_types_namespace=globals())
ResponsesCostInput.model_rebuild(_types_namespace=globals())
ResponsesCostOutput.model_rebuild(_types_namespace=globals())
ResponsesRequestInput.model_rebuild(_types_namespace=globals())
ResponsesRequestOutput.model_rebuild(_types_namespace=globals())
ResponsesResponseInput.model_rebuild(_types_namespace=globals())
ResponsesResponseOutput.model_rebuild(_types_namespace=globals())
ResponsesUsageInput.model_rebuild(_types_namespace=globals())
ResponsesUsageOutput.model_rebuild(_types_namespace=globals())
ResponsesUsageInputTokensDetailsInput.model_rebuild(_types_namespace=globals())
ResponsesUsageInputTokensDetailsOutput.model_rebuild(_types_namespace=globals())
SandboxApplyPatchOutputItemInput.model_rebuild(_types_namespace=globals())
SandboxApplyPatchOutputItemOutput.model_rebuild(_types_namespace=globals())
SandboxEditFileOutputItemInput.model_rebuild(_types_namespace=globals())
SandboxEditFileOutputItemOutput.model_rebuild(_types_namespace=globals())
SandboxGlobOutputItemInput.model_rebuild(_types_namespace=globals())
SandboxGlobOutputItemOutput.model_rebuild(_types_namespace=globals())
SandboxGrepOutputItemInput.model_rebuild(_types_namespace=globals())
SandboxGrepOutputItemOutput.model_rebuild(_types_namespace=globals())
SandboxReadFileOutputItemInput.model_rebuild(_types_namespace=globals())
SandboxReadFileOutputItemOutput.model_rebuild(_types_namespace=globals())
SandboxResultInput.model_rebuild(_types_namespace=globals())
SandboxResultOutput.model_rebuild(_types_namespace=globals())
SandboxResultsOutputItemInput.model_rebuild(_types_namespace=globals())
SandboxResultsOutputItemOutput.model_rebuild(_types_namespace=globals())
SandboxToolInput.model_rebuild(_types_namespace=globals())
SandboxToolOutput.model_rebuild(_types_namespace=globals())
SandboxWriteFileOutputItemInput.model_rebuild(_types_namespace=globals())
SandboxWriteFileOutputItemOutput.model_rebuild(_types_namespace=globals())
SearchDomainFilterInput.model_rebuild(_types_namespace=globals())
SearchDomainFilterOutput.model_rebuild(_types_namespace=globals())
SearchQueriesEventInput.model_rebuild(_types_namespace=globals())
SearchQueriesEventOutput.model_rebuild(_types_namespace=globals())
SearchResultInput.model_rebuild(_types_namespace=globals())
SearchResultOutput.model_rebuild(_types_namespace=globals())
SearchResultsEventInput.model_rebuild(_types_namespace=globals())
SearchResultsEventOutput.model_rebuild(_types_namespace=globals())
SearchResultsOutputItemInput.model_rebuild(_types_namespace=globals())
SearchResultsOutputItemOutput.model_rebuild(_types_namespace=globals())
ShareFileOutputItemInput.model_rebuild(_types_namespace=globals())
ShareFileOutputItemOutput.model_rebuild(_types_namespace=globals())
SkillLoadedOutputItemInput.model_rebuild(_types_namespace=globals())
SkillLoadedOutputItemOutput.model_rebuild(_types_namespace=globals())
TextDeltaEventInput.model_rebuild(_types_namespace=globals())
TextDeltaEventOutput.model_rebuild(_types_namespace=globals())
TextDoneEventInput.model_rebuild(_types_namespace=globals())
TextDoneEventOutput.model_rebuild(_types_namespace=globals())
ToolCallInput.model_rebuild(_types_namespace=globals())
ToolCallOutput.model_rebuild(_types_namespace=globals())
ToolCallDetailsInput.model_rebuild(_types_namespace=globals())
ToolCallDetailsOutput.model_rebuild(_types_namespace=globals())
ToolCallFunctionInput.model_rebuild(_types_namespace=globals())
ToolCallFunctionOutput.model_rebuild(_types_namespace=globals())
ToolSpecInput.model_rebuild(_types_namespace=globals())
ToolSpecOutput.model_rebuild(_types_namespace=globals())
ToolUserLocationInput.model_rebuild(_types_namespace=globals())
ToolUserLocationOutput.model_rebuild(_types_namespace=globals())
URLInput.model_rebuild(_types_namespace=globals())
URLOutput.model_rebuild(_types_namespace=globals())
UnknownOutputItemInput.model_rebuild(_types_namespace=globals())
UnknownOutputItemOutput.model_rebuild(_types_namespace=globals())
UrlContentInput.model_rebuild(_types_namespace=globals())
UrlContentOutput.model_rebuild(_types_namespace=globals())
UsageInfoInput.model_rebuild(_types_namespace=globals())
UsageInfoOutput.model_rebuild(_types_namespace=globals())
UserLocationInput.model_rebuild(_types_namespace=globals())
UserLocationOutput.model_rebuild(_types_namespace=globals())
ValidationErrorInput.model_rebuild(_types_namespace=globals())
ValidationErrorOutput.model_rebuild(_types_namespace=globals())
VideoURLInput.model_rebuild(_types_namespace=globals())
VideoURLOutput.model_rebuild(_types_namespace=globals())
WebSearchFiltersInput.model_rebuild(_types_namespace=globals())
WebSearchFiltersOutput.model_rebuild(_types_namespace=globals())
WebSearchOptionsInput.model_rebuild(_types_namespace=globals())
WebSearchOptionsOutput.model_rebuild(_types_namespace=globals())
WebSearchStepDetailsInput.model_rebuild(_types_namespace=globals())
WebSearchStepDetailsOutput.model_rebuild(_types_namespace=globals())
WebSearchToolInput.model_rebuild(_types_namespace=globals())
WebSearchToolOutput.model_rebuild(_types_namespace=globals())
ResponsesCancelResponseOutput.model_rebuild(_types_namespace=globals())
APIPublicSearchResult: TypeAlias = ApiPublicSearchResultOutput
Annotation: TypeAlias = AnnotationOutput
BrowserSessionResponse: TypeAlias = BrowserSessionResponseOutput
ChatMessageInput: TypeAlias = ChatMessageInputInput
ChatMessageOutput: TypeAlias = ChatMessageOutputOutput
Choice: TypeAlias = ChoiceOutput
AsyncChatCompletionsCompletionCreateParams: TypeAlias = (
    AsyncApiChatCompletionsRequestInput
)
ChatCompletionsCompletionCreateParams: TypeAlias = ApiChatCompletionsRequestInput


class ChatCompletionsCompletionCreateParamsNonStreaming(BaseModel):
    _debug_pro_search: Optional[bool] = None
    _force_new_agent: Union[bool, None] = None
    _inputs: Union[list[int], None] = None
    _prompt_token_length: Union[int, None] = None
    best_of: Union[int, None] = None
    country: Union[str, None] = None
    cum_logprobs: Union[bool, None] = None
    disable_search: Union[bool, None] = None
    diverse_first_token: Union[bool, None] = None
    enable_search_classifier: Union[bool, None] = None
    file_workspace_id: Union[str, None] = None
    frequency_penalty: Union[float, None] = None
    has_image_url: Optional[bool] = None
    image_domain_filter: Union[list[str], None] = None
    image_format_filter: Union[list[str], None] = None
    language_preference: Union[str, None] = None
    last_updated_after_filter: Union[str, None] = None
    last_updated_before_filter: Union[str, None] = None
    latitude: Union[float, None] = None
    logprobs: Union[bool, None] = None
    longitude: Union[float, None] = None
    max_tokens: Union[int, None] = None
    messages: list["ChatMessageInputInput"]
    model: str
    n: Union[int, None] = None
    num_images: Optional[int] = None
    num_search_results: Optional[int] = None
    parallel_tool_calls: Union[bool, None] = None
    presence_penalty: Union[float, None] = None
    ranking_model: Union[str, None] = None
    reasoning_effort: Union[Literal["minimal", "low", "medium", "high"], None] = None
    response_format: Union[
        "ResponseFormatTextInput",
        "ResponseFormatJSONSchemaInput",
        "ResponseFormatRegexInput",
        None,
    ] = None
    response_formatting_locale: Union[str, None] = None
    response_metadata: Union[dict[str, Any], None] = None
    return_images: Union[bool, None] = None
    return_related_questions: Union[bool, None] = None
    safe_search: Union[bool, None] = None
    search_after_date_filter: Union[str, None] = None
    search_before_date_filter: Union[str, None] = None
    search_domain_filter: Union[list[str], None] = None
    search_internal_properties: Union[dict[str, Any], None] = None
    search_language_filter: Union[list[str], None] = None
    search_mode: Union[Literal["web", "academic", "sec"], None] = None
    search_recency_filter: Union[
        Literal["hour", "day", "week", "month", "year"], None
    ] = None
    search_tenant: Union[str, None] = None
    stop: Union[str, list[str], None] = None
    stream: Optional[Literal[False]] = None
    stream_mode: Optional[Literal["full", "concise"]] = None
    temperature: Union[float, None] = None
    thread_id: Union[str, None] = None
    tool_choice: Union[Literal["none", "auto", "required"], None] = None
    tools: Union[list["ToolSpecInput"], None] = None
    top_k: Union[int, None] = None
    top_logprobs: Union[int, None] = None
    top_p: Union[float, None] = None
    updated_after_timestamp: Union[int, None] = None
    updated_before_timestamp: Union[int, None] = None
    use_threads: Union[bool, None] = None
    user_original_query: Union[str, None] = None
    web_search_options: Optional["WebSearchOptionsInput"] = None


class ChatCompletionsCompletionCreateParamsStreaming(BaseModel):
    _debug_pro_search: Optional[bool] = None
    _force_new_agent: Union[bool, None] = None
    _inputs: Union[list[int], None] = None
    _prompt_token_length: Union[int, None] = None
    best_of: Union[int, None] = None
    country: Union[str, None] = None
    cum_logprobs: Union[bool, None] = None
    disable_search: Union[bool, None] = None
    diverse_first_token: Union[bool, None] = None
    enable_search_classifier: Union[bool, None] = None
    file_workspace_id: Union[str, None] = None
    frequency_penalty: Union[float, None] = None
    has_image_url: Optional[bool] = None
    image_domain_filter: Union[list[str], None] = None
    image_format_filter: Union[list[str], None] = None
    language_preference: Union[str, None] = None
    last_updated_after_filter: Union[str, None] = None
    last_updated_before_filter: Union[str, None] = None
    latitude: Union[float, None] = None
    logprobs: Union[bool, None] = None
    longitude: Union[float, None] = None
    max_tokens: Union[int, None] = None
    messages: list["ChatMessageInputInput"]
    model: str
    n: Union[int, None] = None
    num_images: Optional[int] = None
    num_search_results: Optional[int] = None
    parallel_tool_calls: Union[bool, None] = None
    presence_penalty: Union[float, None] = None
    ranking_model: Union[str, None] = None
    reasoning_effort: Union[Literal["minimal", "low", "medium", "high"], None] = None
    response_format: Union[
        "ResponseFormatTextInput",
        "ResponseFormatJSONSchemaInput",
        "ResponseFormatRegexInput",
        None,
    ] = None
    response_formatting_locale: Union[str, None] = None
    response_metadata: Union[dict[str, Any], None] = None
    return_images: Union[bool, None] = None
    return_related_questions: Union[bool, None] = None
    safe_search: Union[bool, None] = None
    search_after_date_filter: Union[str, None] = None
    search_before_date_filter: Union[str, None] = None
    search_domain_filter: Union[list[str], None] = None
    search_internal_properties: Union[dict[str, Any], None] = None
    search_language_filter: Union[list[str], None] = None
    search_mode: Union[Literal["web", "academic", "sec"], None] = None
    search_recency_filter: Union[
        Literal["hour", "day", "week", "month", "year"], None
    ] = None
    search_tenant: Union[str, None] = None
    stop: Union[str, list[str], None] = None
    stream: Literal[True]
    stream_mode: Optional[Literal["full", "concise"]] = None
    temperature: Union[float, None] = None
    thread_id: Union[str, None] = None
    tool_choice: Union[Literal["none", "auto", "required"], None] = None
    tools: Union[list["ToolSpecInput"], None] = None
    top_k: Union[int, None] = None
    top_logprobs: Union[int, None] = None
    top_p: Union[float, None] = None
    updated_after_timestamp: Union[int, None] = None
    updated_before_timestamp: Union[int, None] = None
    use_threads: Union[bool, None] = None
    user_original_query: Union[str, None] = None
    web_search_options: Optional["WebSearchOptionsInput"] = None


AsyncChatCompletionsCompletionCreateResponse: TypeAlias = (
    AsyncApiChatCompletionsResponseOutput
)


class AsyncChatCompletionsCompletionGetParams(BaseModel):
    x_client_env: Optional[str] = Field(None, alias="x-client-env")
    x_client_name: Optional[str] = Field(None, alias="x-client-name")
    x_created_at_epoch_seconds: Optional[str] = Field(
        None, alias="x-created-at-epoch-seconds"
    )
    x_request_time: Optional[str] = Field(None, alias="x-request-time")
    x_usage_tier: Optional[str] = Field(None, alias="x-usage-tier")
    x_user_id: Optional[str] = Field(None, alias="x-user-id")
    api_request: str
    local_mode: Optional[bool] = None


AsyncChatCompletionsCompletionGetResponse: TypeAlias = (
    AsyncApiChatCompletionsResponseOutput
)
AsyncChatCompletionsCompletionListResponse: TypeAlias = (
    ListAsyncApiChatCompletionsResponseOutput
)
ContentPart: TypeAlias = ContentPartOutput
ContextualizedEmbeddingCreateParams: TypeAlias = ContextualizedEmbeddingsRequestInput
ContextualizedEmbeddingCreateResponse: TypeAlias = (
    ContextualizedEmbeddingsResponseOutput
)
ContextualizedEmbeddingObject: TypeAlias = ContextualizedEmbeddingObjectOutput
EmbeddingCreateParams: TypeAlias = EmbeddingsRequestInput
EmbeddingCreateResponse: TypeAlias = EmbeddingsResponseOutput
EmbeddingObject: TypeAlias = EmbeddingObjectOutput
EmbeddingsUsage: TypeAlias = EmbeddingsUsageOutput
ErrorInfo: TypeAlias = ErrorInfoOutput


class ResponsesFilesFileContentParams(BaseModel):
    file_id: str
    response_id: str


FunctionCallOutputItem: TypeAlias = FunctionCallOutputItemOutput
FunctionTool: TypeAlias = FunctionToolInput
InputItem: TypeAlias = InputItemInput
JsonSchemaFormat: TypeAlias = JSONSchemaFormatInput
OutputItem: TypeAlias = OutputItemOutput
ResponseCancelResponse: TypeAlias = ResponsesCancelResponseOutput
ResponseCreateParams: TypeAlias = ResponsesRequestInput


class ResponsesResponseCreateParamsNonStreaming(BaseModel):
    background: Union[bool, None] = None
    input: "InputInput"
    instructions: Optional[str] = None
    language_preference: Optional[str] = None
    max_output_tokens: Optional[int] = None
    max_steps: Optional[int] = None
    model: Optional[str] = None
    models: Optional[list[str]] = None
    preset: Optional[str] = None
    previous_response_id: Optional[str] = None
    reasoning: Optional["ReasoningConfigInput"] = None
    response_format: Optional["ResponseFormatInput"] = None
    skills: Optional[list["SkillInput"]] = None
    store: Optional[bool] = None
    stream: Literal[False] = False
    temperature: Optional[float] = None
    tools: Optional[list["ToolInput"]] = None
    top_p: Optional[float] = None


class ResponsesResponseCreateParamsStreaming(BaseModel):
    background: Union[bool, None] = None
    input: "InputInput"
    instructions: Optional[str] = None
    language_preference: Optional[str] = None
    max_output_tokens: Optional[int] = None
    max_steps: Optional[int] = None
    model: Optional[str] = None
    models: Optional[list[str]] = None
    preset: Optional[str] = None
    previous_response_id: Optional[str] = None
    reasoning: Optional["ReasoningConfigInput"] = None
    response_format: Optional["ResponseFormatInput"] = None
    skills: Optional[list["SkillInput"]] = None
    store: Optional[bool] = None
    stream: Literal[True]
    temperature: Optional[float] = None
    tools: Optional[list["ToolInput"]] = None
    top_p: Optional[float] = None


ResponseCreateResponse: TypeAlias = ResponsesResponseOutput
ResponseFile: TypeAlias = ResponseFileOutput
ResponseFileList: TypeAlias = ResponseFileListOutput
ResponseFormat: TypeAlias = ResponseFormatInput
ResponseRetrieveResponse: TypeAlias = ResponsesResponseOutput
ResponseStreamChunk: TypeAlias = ResponseStreamEventOutput
ResponsesCreateParams: TypeAlias = ResponsesRequestInput
ResponsesUsage: TypeAlias = ResponsesUsageOutput
SearchCreateParams: TypeAlias = ApiSearchRequestInput
SearchCreateResponse: TypeAlias = ApiSearchResponseOutput
SearchResult: TypeAlias = SearchResultOutput
BrowserSessionsSessionCreateParams: TypeAlias = CreateBrowserSessionRequestInput
StreamChunk: TypeAlias = CompletionResponseOutput
UsageInfo: TypeAlias = UsageInfoOutput
UserLocation: TypeAlias = UserLocationInput
WebSearchOptions: TypeAlias = WebSearchOptionsInput
ChatCompletionsCompletionCreateParamsNonStreaming.model_rebuild(
    _types_namespace=globals()
)
ChatCompletionsCompletionCreateParamsStreaming.model_rebuild(_types_namespace=globals())
AsyncChatCompletionsCompletionGetParams.model_rebuild(_types_namespace=globals())
ResponsesFilesFileContentParams.model_rebuild(_types_namespace=globals())
ResponsesResponseCreateParamsNonStreaming.model_rebuild(_types_namespace=globals())
ResponsesResponseCreateParamsStreaming.model_rebuild(_types_namespace=globals())


class AsyncChatCompletionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatCompletionsResourceWithRawResponse:
        return AsyncChatCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(
        self,
    ) -> AsyncChatCompletionsResourceWithStreamingResponse:
        return AsyncChatCompletionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        request: Union["ApiChatCompletionsRequestInput", Mapping[str, object]],
        idempotency_key: Union[Union[str, None], Omit] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> "AsyncApiChatCompletionsResponseOutput":
        _body = AsyncApiChatCompletionsRequestInput.model_validate(
            _without_omitted({"idempotency_key": idempotency_key, "request": request})
        )
        _body_data = _body.model_dump(mode="json", by_alias=True, exclude_unset=True)
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            "AsyncApiChatCompletionsResponseOutput",
            self._post(
                "/async/chat/completions",
                cast_to=AsyncApiChatCompletionsResponseOutput,
                body=_body_data,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result

    def get(
        self,
        api_request: str,
        *,
        local_mode: Union[bool, Omit] = omit,
        x_client_env: Union[str, Omit] = omit,
        x_client_name: Union[str, Omit] = omit,
        x_created_at_epoch_seconds: Union[str, Omit] = omit,
        x_request_time: Union[str, Omit] = omit,
        x_usage_tier: Union[str, Omit] = omit,
        x_user_id: Union[str, Omit] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> "AsyncApiChatCompletionsResponseOutput":
        if not api_request:
            raise ValueError(
                "Expected a non-empty value for `api_request` but received "
                + repr(api_request)
            )
        _query_parameters = _without_omitted({"local_mode": local_mode})
        _header_parameters = _without_omitted_headers(
            {
                "x-client-env": x_client_env,
                "x-client-name": x_client_name,
                "x-created-at-epoch-seconds": x_created_at_epoch_seconds,
                "x-request-time": x_request_time,
                "x-usage-tier": x_usage_tier,
                "x-user-id": x_user_id,
            }
        )
        _result = cast(
            "AsyncApiChatCompletionsResponseOutput",
            self._get(
                "/async/chat/completions/{api_request}".format(api_request=api_request),
                cast_to=AsyncApiChatCompletionsResponseOutput,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result

    def list(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> "ListAsyncApiChatCompletionsResponseOutput":
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            "ListAsyncApiChatCompletionsResponseOutput",
            self._get(
                "/async/chat/completions",
                cast_to=ListAsyncApiChatCompletionsResponseOutput,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result


class AsyncChatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        return AsyncChatResourceWithStreamingResponse(self)

    @cached_property
    def completions(self) -> AsyncChatCompletionsResource:
        return AsyncChatCompletionsResource(self._client)


class BrowserSessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrowserSessionsResourceWithRawResponse:
        return BrowserSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrowserSessionsResourceWithStreamingResponse:
        return BrowserSessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> "BrowserSessionResponseOutput":
        _body = CreateBrowserSessionRequestInput.model_validate(_without_omitted({}))
        _body_data = _body.model_dump(mode="json", by_alias=True, exclude_unset=True)
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            "BrowserSessionResponseOutput",
            self._post(
                "/v1/browser/sessions",
                cast_to=BrowserSessionResponseOutput,
                body=_body_data,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result

    def delete(
        self,
        session_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> None:
        if not session_id:
            raise ValueError(
                "Expected a non-empty value for `session_id` but received "
                + repr(session_id)
            )
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            None,
            self._delete(
                "/v1/browser/sessions/{session_id}".format(session_id=session_id),
                cast_to=NoneType,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result


class ChatCompletionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatCompletionsResourceWithRawResponse:
        return ChatCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatCompletionsResourceWithStreamingResponse:
        return ChatCompletionsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        messages: Sequence[Union["ChatMessageInputInput", Mapping[str, object]]],
        model: str,
        _debug_pro_search: Union[bool, Omit] = omit,
        _force_new_agent: Union[Union[bool, None], Omit] = omit,
        _inputs: Union[Union[Sequence[int], None], Omit] = omit,
        _prompt_token_length: Union[Union[int, None], Omit] = omit,
        best_of: Union[Union[int, None], Omit] = omit,
        country: Union[Union[str, None], Omit] = omit,
        cum_logprobs: Union[Union[bool, None], Omit] = omit,
        disable_search: Union[Union[bool, None], Omit] = omit,
        diverse_first_token: Union[Union[bool, None], Omit] = omit,
        enable_search_classifier: Union[Union[bool, None], Omit] = omit,
        file_workspace_id: Union[Union[str, None], Omit] = omit,
        frequency_penalty: Union[Union[float, None], Omit] = omit,
        has_image_url: Union[bool, Omit] = omit,
        image_domain_filter: Union[Union[Sequence[str], None], Omit] = omit,
        image_format_filter: Union[Union[Sequence[str], None], Omit] = omit,
        language_preference: Union[Union[str, None], Omit] = omit,
        last_updated_after_filter: Union[Union[str, None], Omit] = omit,
        last_updated_before_filter: Union[Union[str, None], Omit] = omit,
        latitude: Union[Union[float, None], Omit] = omit,
        logprobs: Union[Union[bool, None], Omit] = omit,
        longitude: Union[Union[float, None], Omit] = omit,
        max_tokens: Union[Union[int, None], Omit] = omit,
        n: Union[Union[int, None], Omit] = omit,
        num_images: Union[int, Omit] = omit,
        num_search_results: Union[int, Omit] = omit,
        parallel_tool_calls: Union[Union[bool, None], Omit] = omit,
        presence_penalty: Union[Union[float, None], Omit] = omit,
        ranking_model: Union[Union[str, None], Omit] = omit,
        reasoning_effort: Union[
            Union[Literal["minimal", "low", "medium", "high"], None], Omit
        ] = omit,
        response_format: Union[
            Union[
                Union["ResponseFormatTextInput", Mapping[str, object]],
                Union["ResponseFormatJSONSchemaInput", Mapping[str, object]],
                Union["ResponseFormatRegexInput", Mapping[str, object]],
                None,
            ],
            Omit,
        ] = omit,
        response_formatting_locale: Union[Union[str, None], Omit] = omit,
        response_metadata: Union[Union[dict[str, Any], None], Omit] = omit,
        return_images: Union[Union[bool, None], Omit] = omit,
        return_related_questions: Union[Union[bool, None], Omit] = omit,
        safe_search: Union[Union[bool, None], Omit] = omit,
        search_after_date_filter: Union[Union[str, None], Omit] = omit,
        search_before_date_filter: Union[Union[str, None], Omit] = omit,
        search_domain_filter: Union[Union[Sequence[str], None], Omit] = omit,
        search_internal_properties: Union[Union[dict[str, Any], None], Omit] = omit,
        search_language_filter: Union[Union[Sequence[str], None], Omit] = omit,
        search_mode: Union[Union[Literal["web", "academic", "sec"], None], Omit] = omit,
        search_recency_filter: Union[
            Union[Literal["hour", "day", "week", "month", "year"], None], Omit
        ] = omit,
        search_tenant: Union[Union[str, None], Omit] = omit,
        stop: Union[Union[str, Sequence[str], None], Omit] = omit,
        stream: Union[Literal[False], Omit] = omit,
        stream_mode: Union[Literal["full", "concise"], Omit] = omit,
        temperature: Union[Union[float, None], Omit] = omit,
        thread_id: Union[Union[str, None], Omit] = omit,
        tool_choice: Union[
            Union[Literal["none", "auto", "required"], None], Omit
        ] = omit,
        tools: Union[
            Union[Sequence[Union["ToolSpecInput", Mapping[str, object]]], None], Omit
        ] = omit,
        top_k: Union[Union[int, None], Omit] = omit,
        top_logprobs: Union[Union[int, None], Omit] = omit,
        top_p: Union[Union[float, None], Omit] = omit,
        updated_after_timestamp: Union[Union[int, None], Omit] = omit,
        updated_before_timestamp: Union[Union[int, None], Omit] = omit,
        use_threads: Union[Union[bool, None], Omit] = omit,
        user_original_query: Union[Union[str, None], Omit] = omit,
        web_search_options: Union[
            Union["WebSearchOptionsInput", Mapping[str, object]], Omit
        ] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> CompletionResponseOutput: ...
    @overload
    def create(
        self,
        *,
        messages: Sequence[Union["ChatMessageInputInput", Mapping[str, object]]],
        model: str,
        _debug_pro_search: Union[bool, Omit] = omit,
        _force_new_agent: Union[Union[bool, None], Omit] = omit,
        _inputs: Union[Union[Sequence[int], None], Omit] = omit,
        _prompt_token_length: Union[Union[int, None], Omit] = omit,
        best_of: Union[Union[int, None], Omit] = omit,
        country: Union[Union[str, None], Omit] = omit,
        cum_logprobs: Union[Union[bool, None], Omit] = omit,
        disable_search: Union[Union[bool, None], Omit] = omit,
        diverse_first_token: Union[Union[bool, None], Omit] = omit,
        enable_search_classifier: Union[Union[bool, None], Omit] = omit,
        file_workspace_id: Union[Union[str, None], Omit] = omit,
        frequency_penalty: Union[Union[float, None], Omit] = omit,
        has_image_url: Union[bool, Omit] = omit,
        image_domain_filter: Union[Union[Sequence[str], None], Omit] = omit,
        image_format_filter: Union[Union[Sequence[str], None], Omit] = omit,
        language_preference: Union[Union[str, None], Omit] = omit,
        last_updated_after_filter: Union[Union[str, None], Omit] = omit,
        last_updated_before_filter: Union[Union[str, None], Omit] = omit,
        latitude: Union[Union[float, None], Omit] = omit,
        logprobs: Union[Union[bool, None], Omit] = omit,
        longitude: Union[Union[float, None], Omit] = omit,
        max_tokens: Union[Union[int, None], Omit] = omit,
        n: Union[Union[int, None], Omit] = omit,
        num_images: Union[int, Omit] = omit,
        num_search_results: Union[int, Omit] = omit,
        parallel_tool_calls: Union[Union[bool, None], Omit] = omit,
        presence_penalty: Union[Union[float, None], Omit] = omit,
        ranking_model: Union[Union[str, None], Omit] = omit,
        reasoning_effort: Union[
            Union[Literal["minimal", "low", "medium", "high"], None], Omit
        ] = omit,
        response_format: Union[
            Union[
                Union["ResponseFormatTextInput", Mapping[str, object]],
                Union["ResponseFormatJSONSchemaInput", Mapping[str, object]],
                Union["ResponseFormatRegexInput", Mapping[str, object]],
                None,
            ],
            Omit,
        ] = omit,
        response_formatting_locale: Union[Union[str, None], Omit] = omit,
        response_metadata: Union[Union[dict[str, Any], None], Omit] = omit,
        return_images: Union[Union[bool, None], Omit] = omit,
        return_related_questions: Union[Union[bool, None], Omit] = omit,
        safe_search: Union[Union[bool, None], Omit] = omit,
        search_after_date_filter: Union[Union[str, None], Omit] = omit,
        search_before_date_filter: Union[Union[str, None], Omit] = omit,
        search_domain_filter: Union[Union[Sequence[str], None], Omit] = omit,
        search_internal_properties: Union[Union[dict[str, Any], None], Omit] = omit,
        search_language_filter: Union[Union[Sequence[str], None], Omit] = omit,
        search_mode: Union[Union[Literal["web", "academic", "sec"], None], Omit] = omit,
        search_recency_filter: Union[
            Union[Literal["hour", "day", "week", "month", "year"], None], Omit
        ] = omit,
        search_tenant: Union[Union[str, None], Omit] = omit,
        stop: Union[Union[str, Sequence[str], None], Omit] = omit,
        stream: Literal[True],
        stream_mode: Union[Literal["full", "concise"], Omit] = omit,
        temperature: Union[Union[float, None], Omit] = omit,
        thread_id: Union[Union[str, None], Omit] = omit,
        tool_choice: Union[
            Union[Literal["none", "auto", "required"], None], Omit
        ] = omit,
        tools: Union[
            Union[Sequence[Union["ToolSpecInput", Mapping[str, object]]], None], Omit
        ] = omit,
        top_k: Union[Union[int, None], Omit] = omit,
        top_logprobs: Union[Union[int, None], Omit] = omit,
        top_p: Union[Union[float, None], Omit] = omit,
        updated_after_timestamp: Union[Union[int, None], Omit] = omit,
        updated_before_timestamp: Union[Union[int, None], Omit] = omit,
        use_threads: Union[Union[bool, None], Omit] = omit,
        user_original_query: Union[Union[str, None], Omit] = omit,
        web_search_options: Union[
            Union["WebSearchOptionsInput", Mapping[str, object]], Omit
        ] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> Stream["CompletionResponseOutput"]: ...
    def create(
        self,
        *,
        messages: Sequence[Union["ChatMessageInputInput", Mapping[str, object]]],
        model: str,
        _debug_pro_search: Union[bool, Omit] = omit,
        _force_new_agent: Union[Union[bool, None], Omit] = omit,
        _inputs: Union[Union[Sequence[int], None], Omit] = omit,
        _prompt_token_length: Union[Union[int, None], Omit] = omit,
        best_of: Union[Union[int, None], Omit] = omit,
        country: Union[Union[str, None], Omit] = omit,
        cum_logprobs: Union[Union[bool, None], Omit] = omit,
        disable_search: Union[Union[bool, None], Omit] = omit,
        diverse_first_token: Union[Union[bool, None], Omit] = omit,
        enable_search_classifier: Union[Union[bool, None], Omit] = omit,
        file_workspace_id: Union[Union[str, None], Omit] = omit,
        frequency_penalty: Union[Union[float, None], Omit] = omit,
        has_image_url: Union[bool, Omit] = omit,
        image_domain_filter: Union[Union[Sequence[str], None], Omit] = omit,
        image_format_filter: Union[Union[Sequence[str], None], Omit] = omit,
        language_preference: Union[Union[str, None], Omit] = omit,
        last_updated_after_filter: Union[Union[str, None], Omit] = omit,
        last_updated_before_filter: Union[Union[str, None], Omit] = omit,
        latitude: Union[Union[float, None], Omit] = omit,
        logprobs: Union[Union[bool, None], Omit] = omit,
        longitude: Union[Union[float, None], Omit] = omit,
        max_tokens: Union[Union[int, None], Omit] = omit,
        n: Union[Union[int, None], Omit] = omit,
        num_images: Union[int, Omit] = omit,
        num_search_results: Union[int, Omit] = omit,
        parallel_tool_calls: Union[Union[bool, None], Omit] = omit,
        presence_penalty: Union[Union[float, None], Omit] = omit,
        ranking_model: Union[Union[str, None], Omit] = omit,
        reasoning_effort: Union[
            Union[Literal["minimal", "low", "medium", "high"], None], Omit
        ] = omit,
        response_format: Union[
            Union[
                Union["ResponseFormatTextInput", Mapping[str, object]],
                Union["ResponseFormatJSONSchemaInput", Mapping[str, object]],
                Union["ResponseFormatRegexInput", Mapping[str, object]],
                None,
            ],
            Omit,
        ] = omit,
        response_formatting_locale: Union[Union[str, None], Omit] = omit,
        response_metadata: Union[Union[dict[str, Any], None], Omit] = omit,
        return_images: Union[Union[bool, None], Omit] = omit,
        return_related_questions: Union[Union[bool, None], Omit] = omit,
        safe_search: Union[Union[bool, None], Omit] = omit,
        search_after_date_filter: Union[Union[str, None], Omit] = omit,
        search_before_date_filter: Union[Union[str, None], Omit] = omit,
        search_domain_filter: Union[Union[Sequence[str], None], Omit] = omit,
        search_internal_properties: Union[Union[dict[str, Any], None], Omit] = omit,
        search_language_filter: Union[Union[Sequence[str], None], Omit] = omit,
        search_mode: Union[Union[Literal["web", "academic", "sec"], None], Omit] = omit,
        search_recency_filter: Union[
            Union[Literal["hour", "day", "week", "month", "year"], None], Omit
        ] = omit,
        search_tenant: Union[Union[str, None], Omit] = omit,
        stop: Union[Union[str, Sequence[str], None], Omit] = omit,
        stream: Union[Union[bool, None], Omit] = omit,
        stream_mode: Union[Literal["full", "concise"], Omit] = omit,
        temperature: Union[Union[float, None], Omit] = omit,
        thread_id: Union[Union[str, None], Omit] = omit,
        tool_choice: Union[
            Union[Literal["none", "auto", "required"], None], Omit
        ] = omit,
        tools: Union[
            Union[Sequence[Union["ToolSpecInput", Mapping[str, object]]], None], Omit
        ] = omit,
        top_k: Union[Union[int, None], Omit] = omit,
        top_logprobs: Union[Union[int, None], Omit] = omit,
        top_p: Union[Union[float, None], Omit] = omit,
        updated_after_timestamp: Union[Union[int, None], Omit] = omit,
        updated_before_timestamp: Union[Union[int, None], Omit] = omit,
        use_threads: Union[Union[bool, None], Omit] = omit,
        user_original_query: Union[Union[str, None], Omit] = omit,
        web_search_options: Union[
            Union["WebSearchOptionsInput", Mapping[str, object]], Omit
        ] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> Union["CompletionResponseOutput", Stream["CompletionResponseOutput"]]:
        _body = ApiChatCompletionsRequestInput.model_validate(
            _without_omitted(
                {
                    "_debug_pro_search": _debug_pro_search,
                    "_force_new_agent": _force_new_agent,
                    "_inputs": _inputs,
                    "_prompt_token_length": _prompt_token_length,
                    "best_of": best_of,
                    "country": country,
                    "cum_logprobs": cum_logprobs,
                    "disable_search": disable_search,
                    "diverse_first_token": diverse_first_token,
                    "enable_search_classifier": enable_search_classifier,
                    "file_workspace_id": file_workspace_id,
                    "frequency_penalty": frequency_penalty,
                    "has_image_url": has_image_url,
                    "image_domain_filter": image_domain_filter,
                    "image_format_filter": image_format_filter,
                    "language_preference": language_preference,
                    "last_updated_after_filter": last_updated_after_filter,
                    "last_updated_before_filter": last_updated_before_filter,
                    "latitude": latitude,
                    "logprobs": logprobs,
                    "longitude": longitude,
                    "max_tokens": max_tokens,
                    "messages": messages,
                    "model": model,
                    "n": n,
                    "num_images": num_images,
                    "num_search_results": num_search_results,
                    "parallel_tool_calls": parallel_tool_calls,
                    "presence_penalty": presence_penalty,
                    "ranking_model": ranking_model,
                    "reasoning_effort": reasoning_effort,
                    "response_format": response_format,
                    "response_formatting_locale": response_formatting_locale,
                    "response_metadata": response_metadata,
                    "return_images": return_images,
                    "return_related_questions": return_related_questions,
                    "safe_search": safe_search,
                    "search_after_date_filter": search_after_date_filter,
                    "search_before_date_filter": search_before_date_filter,
                    "search_domain_filter": search_domain_filter,
                    "search_internal_properties": search_internal_properties,
                    "search_language_filter": search_language_filter,
                    "search_mode": search_mode,
                    "search_recency_filter": search_recency_filter,
                    "search_tenant": search_tenant,
                    "stop": stop,
                    "stream": stream,
                    "stream_mode": stream_mode,
                    "temperature": temperature,
                    "thread_id": thread_id,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "updated_after_timestamp": updated_after_timestamp,
                    "updated_before_timestamp": updated_before_timestamp,
                    "use_threads": use_threads,
                    "user_original_query": user_original_query,
                    "web_search_options": web_search_options,
                }
            )
        )
        _body_data = _body.model_dump(mode="json", by_alias=True, exclude_unset=True)
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            Union["CompletionResponseOutput", Stream["CompletionResponseOutput"]],
            self._post(
                "/chat/completions",
                cast_to=CompletionResponseOutput,
                body=_body_data,
                stream=stream is True,
                stream_cls=Stream["CompletionResponseOutput"],
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result


class ResponsesFilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResponsesFilesResourceWithRawResponse:
        return ResponsesFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponsesFilesResourceWithStreamingResponse:
        return ResponsesFilesResourceWithStreamingResponse(self)

    def content(
        self,
        file_id: str,
        *,
        response_id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        if not file_id:
            raise ValueError(
                "Expected a non-empty value for `file_id` but received " + repr(file_id)
            )
        if not response_id:
            raise ValueError(
                "Expected a non-empty value for `response_id` but received "
                + repr(response_id)
            )
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers(
            {"Accept": "application/octet-stream"}
        )
        _result = cast(
            BinaryAPIResponse,
            self._get(
                "/v1/responses/{response_id}/files/{file_id}/content".format(
                    file_id=file_id, response_id=response_id
                ),
                cast_to=BinaryAPIResponse,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result

    def list(
        self,
        response_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> "ResponseFileListOutput":
        if not response_id:
            raise ValueError(
                "Expected a non-empty value for `response_id` but received "
                + repr(response_id)
            )
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            "ResponseFileListOutput",
            self._get(
                "/v1/responses/{response_id}/files".format(response_id=response_id),
                cast_to=ResponseFileListOutput,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result


class AsyncResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResourceWithRawResponse:
        return AsyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourceWithStreamingResponse:
        return AsyncResourceWithStreamingResponse(self)

    @cached_property
    def chat(self) -> AsyncChatResource:
        return AsyncChatResource(self._client)


class BrowserResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrowserResourceWithRawResponse:
        return BrowserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrowserResourceWithStreamingResponse:
        return BrowserResourceWithStreamingResponse(self)

    @cached_property
    def sessions(self) -> BrowserSessionsResource:
        return BrowserSessionsResource(self._client)


class ChatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        return ChatResourceWithStreamingResponse(self)

    @cached_property
    def completions(self) -> ChatCompletionsResource:
        return ChatCompletionsResource(self._client)


class ContextualizedEmbeddingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContextualizedEmbeddingsResourceWithRawResponse:
        return ContextualizedEmbeddingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(
        self,
    ) -> ContextualizedEmbeddingsResourceWithStreamingResponse:
        return ContextualizedEmbeddingsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        input: Sequence[Sequence[str]],
        model: Literal["pplx-embed-context-v1-0.6b", "pplx-embed-context-v1-4b"],
        dimensions: Union[int, Omit] = omit,
        encoding_format: Union[Literal["base64_int8", "base64_binary"], Omit] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> "ContextualizedEmbeddingsResponseOutput":
        _body = ContextualizedEmbeddingsRequestInput.model_validate(
            _without_omitted(
                {
                    "dimensions": dimensions,
                    "encoding_format": encoding_format,
                    "input": input,
                    "model": model,
                }
            )
        )
        _body_data = _body.model_dump(mode="json", by_alias=True, exclude_unset=True)
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            "ContextualizedEmbeddingsResponseOutput",
            self._post(
                "/v1/contextualizedembeddings",
                cast_to=ContextualizedEmbeddingsResponseOutput,
                body=_body_data,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result


class EmbeddingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmbeddingsResourceWithRawResponse:
        return EmbeddingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmbeddingsResourceWithStreamingResponse:
        return EmbeddingsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        input: Union[str, Sequence[str]],
        model: Literal["pplx-embed-v1-0.6b", "pplx-embed-v1-4b"],
        dimensions: Union[int, Omit] = omit,
        encoding_format: Union[Literal["base64_int8", "base64_binary"], Omit] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> "EmbeddingsResponseOutput":
        _body = EmbeddingsRequestInput.model_validate(
            _without_omitted(
                {
                    "dimensions": dimensions,
                    "encoding_format": encoding_format,
                    "input": input,
                    "model": model,
                }
            )
        )
        _body_data = _body.model_dump(mode="json", by_alias=True, exclude_unset=True)
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            "EmbeddingsResponseOutput",
            self._post(
                "/v1/embeddings",
                cast_to=EmbeddingsResponseOutput,
                body=_body_data,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result


class ResponsesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResponsesResourceWithRawResponse:
        return ResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponsesResourceWithStreamingResponse:
        return ResponsesResourceWithStreamingResponse(self)

    def cancel(
        self,
        response_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> "ResponsesCancelResponseOutput":
        if not response_id:
            raise ValueError(
                "Expected a non-empty value for `response_id` but received "
                + repr(response_id)
            )
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            "ResponsesCancelResponseOutput",
            self._post(
                "/v1/responses/{response_id}/cancel".format(response_id=response_id),
                cast_to=ResponsesCancelResponseOutput,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result

    @overload
    def create(
        self,
        *,
        input: "InputInput",
        background: Union[Union[bool, None], Omit] = omit,
        instructions: Union[str, Omit] = omit,
        language_preference: Union[str, Omit] = omit,
        max_output_tokens: Union[int, Omit] = omit,
        max_steps: Union[int, Omit] = omit,
        model: Union[str, Omit] = omit,
        models: Union[Sequence[str], Omit] = omit,
        preset: Union[str, Omit] = omit,
        previous_response_id: Union[str, Omit] = omit,
        reasoning: Union[
            Union["ReasoningConfigInput", Mapping[str, object]], Omit
        ] = omit,
        response_format: Union[
            Union["ResponseFormatInput", Mapping[str, object]], Omit
        ] = omit,
        skills: Union[Sequence[Union["SkillInput", Mapping[str, object]]], Omit] = omit,
        store: Union[bool, Omit] = omit,
        stream: Union[Literal[False], Omit] = omit,
        temperature: Union[float, Omit] = omit,
        tools: Union[Sequence[Union["ToolInput", Mapping[str, object]]], Omit] = omit,
        top_p: Union[float, Omit] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> ResponsesResponseOutput: ...
    @overload
    def create(
        self,
        *,
        input: "InputInput",
        background: Union[Union[bool, None], Omit] = omit,
        instructions: Union[str, Omit] = omit,
        language_preference: Union[str, Omit] = omit,
        max_output_tokens: Union[int, Omit] = omit,
        max_steps: Union[int, Omit] = omit,
        model: Union[str, Omit] = omit,
        models: Union[Sequence[str], Omit] = omit,
        preset: Union[str, Omit] = omit,
        previous_response_id: Union[str, Omit] = omit,
        reasoning: Union[
            Union["ReasoningConfigInput", Mapping[str, object]], Omit
        ] = omit,
        response_format: Union[
            Union["ResponseFormatInput", Mapping[str, object]], Omit
        ] = omit,
        skills: Union[Sequence[Union["SkillInput", Mapping[str, object]]], Omit] = omit,
        store: Union[bool, Omit] = omit,
        stream: Literal[True],
        temperature: Union[float, Omit] = omit,
        tools: Union[Sequence[Union["ToolInput", Mapping[str, object]]], Omit] = omit,
        top_p: Union[float, Omit] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> Stream["ResponseStreamEventOutput"]: ...
    def create(
        self,
        *,
        input: "InputInput",
        background: Union[Union[bool, None], Omit] = omit,
        instructions: Union[str, Omit] = omit,
        language_preference: Union[str, Omit] = omit,
        max_output_tokens: Union[int, Omit] = omit,
        max_steps: Union[int, Omit] = omit,
        model: Union[str, Omit] = omit,
        models: Union[Sequence[str], Omit] = omit,
        preset: Union[str, Omit] = omit,
        previous_response_id: Union[str, Omit] = omit,
        reasoning: Union[
            Union["ReasoningConfigInput", Mapping[str, object]], Omit
        ] = omit,
        response_format: Union[
            Union["ResponseFormatInput", Mapping[str, object]], Omit
        ] = omit,
        skills: Union[Sequence[Union["SkillInput", Mapping[str, object]]], Omit] = omit,
        store: Union[bool, Omit] = omit,
        stream: Union[bool, Omit] = omit,
        temperature: Union[float, Omit] = omit,
        tools: Union[Sequence[Union["ToolInput", Mapping[str, object]]], Omit] = omit,
        top_p: Union[float, Omit] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> Union["ResponsesResponseOutput", Stream["ResponseStreamEventOutput"]]:
        _body = ResponsesRequestInput.model_validate(
            _without_omitted(
                {
                    "background": background,
                    "input": input,
                    "instructions": instructions,
                    "language_preference": language_preference,
                    "max_output_tokens": max_output_tokens,
                    "max_steps": max_steps,
                    "model": model,
                    "models": models,
                    "preset": preset,
                    "previous_response_id": previous_response_id,
                    "reasoning": reasoning,
                    "response_format": response_format,
                    "skills": skills,
                    "store": store,
                    "stream": stream,
                    "temperature": temperature,
                    "tools": tools,
                    "top_p": top_p,
                }
            )
        )
        _body_data = _body.model_dump(mode="json", by_alias=True, exclude_unset=True)
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            Union["ResponsesResponseOutput", Stream["ResponseStreamEventOutput"]],
            self._post(
                "/v1/responses",
                cast_to=ResponsesResponseOutput,
                body=_body_data,
                stream=stream is True,
                stream_cls=Stream["ResponseStreamEventOutput"],
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result

    def retrieve(
        self,
        response_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> "ResponsesResponseOutput":
        if not response_id:
            raise ValueError(
                "Expected a non-empty value for `response_id` but received "
                + repr(response_id)
            )
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            "ResponsesResponseOutput",
            self._get(
                "/v1/responses/{response_id}".format(response_id=response_id),
                cast_to=ResponsesResponseOutput,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result

    @cached_property
    def files(self) -> ResponsesFilesResource:
        return ResponsesFilesResource(self._client)


class SearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        return SearchResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        query: Union[str, Sequence[str]],
        country: Union[Union[str, None], Omit] = omit,
        display_server_time: Union[bool, Omit] = omit,
        last_updated_after_filter: Union[Union[str, None], Omit] = omit,
        last_updated_before_filter: Union[Union[str, None], Omit] = omit,
        max_results: Union[int, Omit] = omit,
        max_tokens: Union[int, Omit] = omit,
        max_tokens_per_page: Union[int, Omit] = omit,
        search_after_date_filter: Union[Union[str, None], Omit] = omit,
        search_before_date_filter: Union[Union[str, None], Omit] = omit,
        search_context_size: Union[Literal["low", "medium", "high"], Omit] = omit,
        search_domain_filter: Union[Union[Sequence[str], None], Omit] = omit,
        search_language_filter: Union[Union[Sequence[str], None], Omit] = omit,
        search_mode: Union[Union[Literal["web", "academic", "sec"], None], Omit] = omit,
        search_recency_filter: Union[
            Union[Literal["hour", "day", "week", "month", "year"], None], Omit
        ] = omit,
        search_type: Union[Union[Literal["web", "people"], None], Omit] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> "ApiSearchResponseOutput":
        _body = ApiSearchRequestInput.model_validate(
            _without_omitted(
                {
                    "country": country,
                    "display_server_time": display_server_time,
                    "last_updated_after_filter": last_updated_after_filter,
                    "last_updated_before_filter": last_updated_before_filter,
                    "max_results": max_results,
                    "max_tokens": max_tokens,
                    "max_tokens_per_page": max_tokens_per_page,
                    "query": query,
                    "search_after_date_filter": search_after_date_filter,
                    "search_before_date_filter": search_before_date_filter,
                    "search_context_size": search_context_size,
                    "search_domain_filter": search_domain_filter,
                    "search_language_filter": search_language_filter,
                    "search_mode": search_mode,
                    "search_recency_filter": search_recency_filter,
                    "search_type": search_type,
                }
            )
        )
        _body_data = _body.model_dump(mode="json", by_alias=True, exclude_unset=True)
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            "ApiSearchResponseOutput",
            self._post(
                "/search",
                cast_to=ApiSearchResponseOutput,
                body=_body_data,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result


class AsyncChatCompletionsResourceWithRawResponse:
    def __init__(self, resource: AsyncChatCompletionsResource) -> None:
        self._resource = resource
        self.create = to_raw_response_wrapper(resource, "create")
        self.get = to_raw_response_wrapper(resource, "get")
        self.list = to_raw_response_wrapper(resource, "list")


class AsyncChatCompletionsResourceWithStreamingResponse:
    def __init__(self, resource: AsyncChatCompletionsResource) -> None:
        self._resource = resource
        self.create = to_streamed_response_wrapper(resource, "create")
        self.get = to_streamed_response_wrapper(resource, "get")
        self.list = to_streamed_response_wrapper(resource, "list")


class AsyncChatResourceWithRawResponse:
    def __init__(self, resource: AsyncChatResource) -> None:
        self._resource = resource

    @cached_property
    def completions(self) -> AsyncChatCompletionsResourceWithRawResponse:
        return AsyncChatCompletionsResourceWithRawResponse(self._resource.completions)


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, resource: AsyncChatResource) -> None:
        self._resource = resource

    @cached_property
    def completions(self) -> AsyncChatCompletionsResourceWithStreamingResponse:
        return AsyncChatCompletionsResourceWithStreamingResponse(
            self._resource.completions
        )


class BrowserSessionsResourceWithRawResponse:
    def __init__(self, resource: BrowserSessionsResource) -> None:
        self._resource = resource
        self.create = to_raw_response_wrapper(resource, "create")
        self.delete = to_raw_response_wrapper(resource, "delete")


class BrowserSessionsResourceWithStreamingResponse:
    def __init__(self, resource: BrowserSessionsResource) -> None:
        self._resource = resource
        self.create = to_streamed_response_wrapper(resource, "create")
        self.delete = to_streamed_response_wrapper(resource, "delete")


class ChatCompletionsResourceWithRawResponse:
    def __init__(self, resource: ChatCompletionsResource) -> None:
        self._resource = resource
        self.create = to_raw_response_wrapper(resource, "create")


class ChatCompletionsResourceWithStreamingResponse:
    def __init__(self, resource: ChatCompletionsResource) -> None:
        self._resource = resource
        self.create = to_streamed_response_wrapper(resource, "create")


class ResponsesFilesResourceWithRawResponse:
    def __init__(self, resource: ResponsesFilesResource) -> None:
        self._resource = resource
        self.content = to_raw_response_wrapper(resource, "content")
        self.list = to_raw_response_wrapper(resource, "list")


class ResponsesFilesResourceWithStreamingResponse:
    def __init__(self, resource: ResponsesFilesResource) -> None:
        self._resource = resource
        self.content = to_streamed_response_wrapper(resource, "content")
        self.list = to_streamed_response_wrapper(resource, "list")


class AsyncResourceWithRawResponse:
    def __init__(self, resource: AsyncResource) -> None:
        self._resource = resource

    @cached_property
    def chat(self) -> AsyncChatResourceWithRawResponse:
        return AsyncChatResourceWithRawResponse(self._resource.chat)


class AsyncResourceWithStreamingResponse:
    def __init__(self, resource: AsyncResource) -> None:
        self._resource = resource

    @cached_property
    def chat(self) -> AsyncChatResourceWithStreamingResponse:
        return AsyncChatResourceWithStreamingResponse(self._resource.chat)


class BrowserResourceWithRawResponse:
    def __init__(self, resource: BrowserResource) -> None:
        self._resource = resource

    @cached_property
    def sessions(self) -> BrowserSessionsResourceWithRawResponse:
        return BrowserSessionsResourceWithRawResponse(self._resource.sessions)


class BrowserResourceWithStreamingResponse:
    def __init__(self, resource: BrowserResource) -> None:
        self._resource = resource

    @cached_property
    def sessions(self) -> BrowserSessionsResourceWithStreamingResponse:
        return BrowserSessionsResourceWithStreamingResponse(self._resource.sessions)


class ChatResourceWithRawResponse:
    def __init__(self, resource: ChatResource) -> None:
        self._resource = resource

    @cached_property
    def completions(self) -> ChatCompletionsResourceWithRawResponse:
        return ChatCompletionsResourceWithRawResponse(self._resource.completions)


class ChatResourceWithStreamingResponse:
    def __init__(self, resource: ChatResource) -> None:
        self._resource = resource

    @cached_property
    def completions(self) -> ChatCompletionsResourceWithStreamingResponse:
        return ChatCompletionsResourceWithStreamingResponse(self._resource.completions)


class ContextualizedEmbeddingsResourceWithRawResponse:
    def __init__(self, resource: ContextualizedEmbeddingsResource) -> None:
        self._resource = resource
        self.create = to_raw_response_wrapper(resource, "create")


class ContextualizedEmbeddingsResourceWithStreamingResponse:
    def __init__(self, resource: ContextualizedEmbeddingsResource) -> None:
        self._resource = resource
        self.create = to_streamed_response_wrapper(resource, "create")


class EmbeddingsResourceWithRawResponse:
    def __init__(self, resource: EmbeddingsResource) -> None:
        self._resource = resource
        self.create = to_raw_response_wrapper(resource, "create")


class EmbeddingsResourceWithStreamingResponse:
    def __init__(self, resource: EmbeddingsResource) -> None:
        self._resource = resource
        self.create = to_streamed_response_wrapper(resource, "create")


class ResponsesResourceWithRawResponse:
    def __init__(self, resource: ResponsesResource) -> None:
        self._resource = resource
        self.cancel = to_raw_response_wrapper(resource, "cancel")
        self.create = to_raw_response_wrapper(resource, "create")
        self.retrieve = to_raw_response_wrapper(resource, "retrieve")

    @cached_property
    def files(self) -> ResponsesFilesResourceWithRawResponse:
        return ResponsesFilesResourceWithRawResponse(self._resource.files)


class ResponsesResourceWithStreamingResponse:
    def __init__(self, resource: ResponsesResource) -> None:
        self._resource = resource
        self.cancel = to_streamed_response_wrapper(resource, "cancel")
        self.create = to_streamed_response_wrapper(resource, "create")
        self.retrieve = to_streamed_response_wrapper(resource, "retrieve")

    @cached_property
    def files(self) -> ResponsesFilesResourceWithStreamingResponse:
        return ResponsesFilesResourceWithStreamingResponse(self._resource.files)


class SearchResourceWithRawResponse:
    def __init__(self, resource: SearchResource) -> None:
        self._resource = resource
        self.create = to_raw_response_wrapper(resource, "create")


class SearchResourceWithStreamingResponse:
    def __init__(self, resource: SearchResource) -> None:
        self._resource = resource
        self.create = to_streamed_response_wrapper(resource, "create")


class PerplexitySdk(SyncAPIResource):
    @cached_property
    def async_(self) -> AsyncResource:
        return AsyncResource(self._client)

    @cached_property
    def browser(self) -> BrowserResource:
        return BrowserResource(self._client)

    @cached_property
    def chat(self) -> ChatResource:
        return ChatResource(self._client)

    @cached_property
    def contextualized_embeddings(self) -> ContextualizedEmbeddingsResource:
        return ContextualizedEmbeddingsResource(self._client)

    @cached_property
    def embeddings(self) -> EmbeddingsResource:
        return EmbeddingsResource(self._client)

    @cached_property
    def responses(self) -> ResponsesResource:
        return ResponsesResource(self._client)

    @cached_property
    def search(self) -> SearchResource:
        return SearchResource(self._client)


class AsyncClientAsyncChatCompletionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(
        self,
    ) -> AsyncClientAsyncChatCompletionsResourceWithRawResponse:
        return AsyncClientAsyncChatCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(
        self,
    ) -> AsyncClientAsyncChatCompletionsResourceWithStreamingResponse:
        return AsyncClientAsyncChatCompletionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        request: Union["ApiChatCompletionsRequestInput", Mapping[str, object]],
        idempotency_key: Union[Union[str, None], Omit] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> "AsyncApiChatCompletionsResponseOutput":
        _body = AsyncApiChatCompletionsRequestInput.model_validate(
            _without_omitted({"idempotency_key": idempotency_key, "request": request})
        )
        _body_data = _body.model_dump(mode="json", by_alias=True, exclude_unset=True)
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            "AsyncApiChatCompletionsResponseOutput",
            await self._post(
                "/async/chat/completions",
                cast_to=AsyncApiChatCompletionsResponseOutput,
                body=_body_data,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result

    async def get(
        self,
        api_request: str,
        *,
        local_mode: Union[bool, Omit] = omit,
        x_client_env: Union[str, Omit] = omit,
        x_client_name: Union[str, Omit] = omit,
        x_created_at_epoch_seconds: Union[str, Omit] = omit,
        x_request_time: Union[str, Omit] = omit,
        x_usage_tier: Union[str, Omit] = omit,
        x_user_id: Union[str, Omit] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> "AsyncApiChatCompletionsResponseOutput":
        if not api_request:
            raise ValueError(
                "Expected a non-empty value for `api_request` but received "
                + repr(api_request)
            )
        _query_parameters = _without_omitted({"local_mode": local_mode})
        _header_parameters = _without_omitted_headers(
            {
                "x-client-env": x_client_env,
                "x-client-name": x_client_name,
                "x-created-at-epoch-seconds": x_created_at_epoch_seconds,
                "x-request-time": x_request_time,
                "x-usage-tier": x_usage_tier,
                "x-user-id": x_user_id,
            }
        )
        _result = cast(
            "AsyncApiChatCompletionsResponseOutput",
            await self._get(
                "/async/chat/completions/{api_request}".format(api_request=api_request),
                cast_to=AsyncApiChatCompletionsResponseOutput,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result

    async def list(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> "ListAsyncApiChatCompletionsResponseOutput":
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            "ListAsyncApiChatCompletionsResponseOutput",
            await self._get(
                "/async/chat/completions",
                cast_to=ListAsyncApiChatCompletionsResponseOutput,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result


class AsyncClientAsyncChatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientAsyncChatResourceWithRawResponse:
        return AsyncClientAsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(
        self,
    ) -> AsyncClientAsyncChatResourceWithStreamingResponse:
        return AsyncClientAsyncChatResourceWithStreamingResponse(self)

    @cached_property
    def completions(self) -> AsyncClientAsyncChatCompletionsResource:
        return AsyncClientAsyncChatCompletionsResource(self._client)


class AsyncClientBrowserSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientBrowserSessionsResourceWithRawResponse:
        return AsyncClientBrowserSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(
        self,
    ) -> AsyncClientBrowserSessionsResourceWithStreamingResponse:
        return AsyncClientBrowserSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> "BrowserSessionResponseOutput":
        _body = CreateBrowserSessionRequestInput.model_validate(_without_omitted({}))
        _body_data = _body.model_dump(mode="json", by_alias=True, exclude_unset=True)
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            "BrowserSessionResponseOutput",
            await self._post(
                "/v1/browser/sessions",
                cast_to=BrowserSessionResponseOutput,
                body=_body_data,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result

    async def delete(
        self,
        session_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> None:
        if not session_id:
            raise ValueError(
                "Expected a non-empty value for `session_id` but received "
                + repr(session_id)
            )
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            None,
            await self._delete(
                "/v1/browser/sessions/{session_id}".format(session_id=session_id),
                cast_to=NoneType,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result


class AsyncClientChatCompletionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientChatCompletionsResourceWithRawResponse:
        return AsyncClientChatCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(
        self,
    ) -> AsyncClientChatCompletionsResourceWithStreamingResponse:
        return AsyncClientChatCompletionsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        messages: Sequence[Union["ChatMessageInputInput", Mapping[str, object]]],
        model: str,
        _debug_pro_search: Union[bool, Omit] = omit,
        _force_new_agent: Union[Union[bool, None], Omit] = omit,
        _inputs: Union[Union[Sequence[int], None], Omit] = omit,
        _prompt_token_length: Union[Union[int, None], Omit] = omit,
        best_of: Union[Union[int, None], Omit] = omit,
        country: Union[Union[str, None], Omit] = omit,
        cum_logprobs: Union[Union[bool, None], Omit] = omit,
        disable_search: Union[Union[bool, None], Omit] = omit,
        diverse_first_token: Union[Union[bool, None], Omit] = omit,
        enable_search_classifier: Union[Union[bool, None], Omit] = omit,
        file_workspace_id: Union[Union[str, None], Omit] = omit,
        frequency_penalty: Union[Union[float, None], Omit] = omit,
        has_image_url: Union[bool, Omit] = omit,
        image_domain_filter: Union[Union[Sequence[str], None], Omit] = omit,
        image_format_filter: Union[Union[Sequence[str], None], Omit] = omit,
        language_preference: Union[Union[str, None], Omit] = omit,
        last_updated_after_filter: Union[Union[str, None], Omit] = omit,
        last_updated_before_filter: Union[Union[str, None], Omit] = omit,
        latitude: Union[Union[float, None], Omit] = omit,
        logprobs: Union[Union[bool, None], Omit] = omit,
        longitude: Union[Union[float, None], Omit] = omit,
        max_tokens: Union[Union[int, None], Omit] = omit,
        n: Union[Union[int, None], Omit] = omit,
        num_images: Union[int, Omit] = omit,
        num_search_results: Union[int, Omit] = omit,
        parallel_tool_calls: Union[Union[bool, None], Omit] = omit,
        presence_penalty: Union[Union[float, None], Omit] = omit,
        ranking_model: Union[Union[str, None], Omit] = omit,
        reasoning_effort: Union[
            Union[Literal["minimal", "low", "medium", "high"], None], Omit
        ] = omit,
        response_format: Union[
            Union[
                Union["ResponseFormatTextInput", Mapping[str, object]],
                Union["ResponseFormatJSONSchemaInput", Mapping[str, object]],
                Union["ResponseFormatRegexInput", Mapping[str, object]],
                None,
            ],
            Omit,
        ] = omit,
        response_formatting_locale: Union[Union[str, None], Omit] = omit,
        response_metadata: Union[Union[dict[str, Any], None], Omit] = omit,
        return_images: Union[Union[bool, None], Omit] = omit,
        return_related_questions: Union[Union[bool, None], Omit] = omit,
        safe_search: Union[Union[bool, None], Omit] = omit,
        search_after_date_filter: Union[Union[str, None], Omit] = omit,
        search_before_date_filter: Union[Union[str, None], Omit] = omit,
        search_domain_filter: Union[Union[Sequence[str], None], Omit] = omit,
        search_internal_properties: Union[Union[dict[str, Any], None], Omit] = omit,
        search_language_filter: Union[Union[Sequence[str], None], Omit] = omit,
        search_mode: Union[Union[Literal["web", "academic", "sec"], None], Omit] = omit,
        search_recency_filter: Union[
            Union[Literal["hour", "day", "week", "month", "year"], None], Omit
        ] = omit,
        search_tenant: Union[Union[str, None], Omit] = omit,
        stop: Union[Union[str, Sequence[str], None], Omit] = omit,
        stream: Union[Literal[False], Omit] = omit,
        stream_mode: Union[Literal["full", "concise"], Omit] = omit,
        temperature: Union[Union[float, None], Omit] = omit,
        thread_id: Union[Union[str, None], Omit] = omit,
        tool_choice: Union[
            Union[Literal["none", "auto", "required"], None], Omit
        ] = omit,
        tools: Union[
            Union[Sequence[Union["ToolSpecInput", Mapping[str, object]]], None], Omit
        ] = omit,
        top_k: Union[Union[int, None], Omit] = omit,
        top_logprobs: Union[Union[int, None], Omit] = omit,
        top_p: Union[Union[float, None], Omit] = omit,
        updated_after_timestamp: Union[Union[int, None], Omit] = omit,
        updated_before_timestamp: Union[Union[int, None], Omit] = omit,
        use_threads: Union[Union[bool, None], Omit] = omit,
        user_original_query: Union[Union[str, None], Omit] = omit,
        web_search_options: Union[
            Union["WebSearchOptionsInput", Mapping[str, object]], Omit
        ] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> CompletionResponseOutput: ...
    @overload
    async def create(
        self,
        *,
        messages: Sequence[Union["ChatMessageInputInput", Mapping[str, object]]],
        model: str,
        _debug_pro_search: Union[bool, Omit] = omit,
        _force_new_agent: Union[Union[bool, None], Omit] = omit,
        _inputs: Union[Union[Sequence[int], None], Omit] = omit,
        _prompt_token_length: Union[Union[int, None], Omit] = omit,
        best_of: Union[Union[int, None], Omit] = omit,
        country: Union[Union[str, None], Omit] = omit,
        cum_logprobs: Union[Union[bool, None], Omit] = omit,
        disable_search: Union[Union[bool, None], Omit] = omit,
        diverse_first_token: Union[Union[bool, None], Omit] = omit,
        enable_search_classifier: Union[Union[bool, None], Omit] = omit,
        file_workspace_id: Union[Union[str, None], Omit] = omit,
        frequency_penalty: Union[Union[float, None], Omit] = omit,
        has_image_url: Union[bool, Omit] = omit,
        image_domain_filter: Union[Union[Sequence[str], None], Omit] = omit,
        image_format_filter: Union[Union[Sequence[str], None], Omit] = omit,
        language_preference: Union[Union[str, None], Omit] = omit,
        last_updated_after_filter: Union[Union[str, None], Omit] = omit,
        last_updated_before_filter: Union[Union[str, None], Omit] = omit,
        latitude: Union[Union[float, None], Omit] = omit,
        logprobs: Union[Union[bool, None], Omit] = omit,
        longitude: Union[Union[float, None], Omit] = omit,
        max_tokens: Union[Union[int, None], Omit] = omit,
        n: Union[Union[int, None], Omit] = omit,
        num_images: Union[int, Omit] = omit,
        num_search_results: Union[int, Omit] = omit,
        parallel_tool_calls: Union[Union[bool, None], Omit] = omit,
        presence_penalty: Union[Union[float, None], Omit] = omit,
        ranking_model: Union[Union[str, None], Omit] = omit,
        reasoning_effort: Union[
            Union[Literal["minimal", "low", "medium", "high"], None], Omit
        ] = omit,
        response_format: Union[
            Union[
                Union["ResponseFormatTextInput", Mapping[str, object]],
                Union["ResponseFormatJSONSchemaInput", Mapping[str, object]],
                Union["ResponseFormatRegexInput", Mapping[str, object]],
                None,
            ],
            Omit,
        ] = omit,
        response_formatting_locale: Union[Union[str, None], Omit] = omit,
        response_metadata: Union[Union[dict[str, Any], None], Omit] = omit,
        return_images: Union[Union[bool, None], Omit] = omit,
        return_related_questions: Union[Union[bool, None], Omit] = omit,
        safe_search: Union[Union[bool, None], Omit] = omit,
        search_after_date_filter: Union[Union[str, None], Omit] = omit,
        search_before_date_filter: Union[Union[str, None], Omit] = omit,
        search_domain_filter: Union[Union[Sequence[str], None], Omit] = omit,
        search_internal_properties: Union[Union[dict[str, Any], None], Omit] = omit,
        search_language_filter: Union[Union[Sequence[str], None], Omit] = omit,
        search_mode: Union[Union[Literal["web", "academic", "sec"], None], Omit] = omit,
        search_recency_filter: Union[
            Union[Literal["hour", "day", "week", "month", "year"], None], Omit
        ] = omit,
        search_tenant: Union[Union[str, None], Omit] = omit,
        stop: Union[Union[str, Sequence[str], None], Omit] = omit,
        stream: Literal[True],
        stream_mode: Union[Literal["full", "concise"], Omit] = omit,
        temperature: Union[Union[float, None], Omit] = omit,
        thread_id: Union[Union[str, None], Omit] = omit,
        tool_choice: Union[
            Union[Literal["none", "auto", "required"], None], Omit
        ] = omit,
        tools: Union[
            Union[Sequence[Union["ToolSpecInput", Mapping[str, object]]], None], Omit
        ] = omit,
        top_k: Union[Union[int, None], Omit] = omit,
        top_logprobs: Union[Union[int, None], Omit] = omit,
        top_p: Union[Union[float, None], Omit] = omit,
        updated_after_timestamp: Union[Union[int, None], Omit] = omit,
        updated_before_timestamp: Union[Union[int, None], Omit] = omit,
        use_threads: Union[Union[bool, None], Omit] = omit,
        user_original_query: Union[Union[str, None], Omit] = omit,
        web_search_options: Union[
            Union["WebSearchOptionsInput", Mapping[str, object]], Omit
        ] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> AsyncStream["CompletionResponseOutput"]: ...
    async def create(
        self,
        *,
        messages: Sequence[Union["ChatMessageInputInput", Mapping[str, object]]],
        model: str,
        _debug_pro_search: Union[bool, Omit] = omit,
        _force_new_agent: Union[Union[bool, None], Omit] = omit,
        _inputs: Union[Union[Sequence[int], None], Omit] = omit,
        _prompt_token_length: Union[Union[int, None], Omit] = omit,
        best_of: Union[Union[int, None], Omit] = omit,
        country: Union[Union[str, None], Omit] = omit,
        cum_logprobs: Union[Union[bool, None], Omit] = omit,
        disable_search: Union[Union[bool, None], Omit] = omit,
        diverse_first_token: Union[Union[bool, None], Omit] = omit,
        enable_search_classifier: Union[Union[bool, None], Omit] = omit,
        file_workspace_id: Union[Union[str, None], Omit] = omit,
        frequency_penalty: Union[Union[float, None], Omit] = omit,
        has_image_url: Union[bool, Omit] = omit,
        image_domain_filter: Union[Union[Sequence[str], None], Omit] = omit,
        image_format_filter: Union[Union[Sequence[str], None], Omit] = omit,
        language_preference: Union[Union[str, None], Omit] = omit,
        last_updated_after_filter: Union[Union[str, None], Omit] = omit,
        last_updated_before_filter: Union[Union[str, None], Omit] = omit,
        latitude: Union[Union[float, None], Omit] = omit,
        logprobs: Union[Union[bool, None], Omit] = omit,
        longitude: Union[Union[float, None], Omit] = omit,
        max_tokens: Union[Union[int, None], Omit] = omit,
        n: Union[Union[int, None], Omit] = omit,
        num_images: Union[int, Omit] = omit,
        num_search_results: Union[int, Omit] = omit,
        parallel_tool_calls: Union[Union[bool, None], Omit] = omit,
        presence_penalty: Union[Union[float, None], Omit] = omit,
        ranking_model: Union[Union[str, None], Omit] = omit,
        reasoning_effort: Union[
            Union[Literal["minimal", "low", "medium", "high"], None], Omit
        ] = omit,
        response_format: Union[
            Union[
                Union["ResponseFormatTextInput", Mapping[str, object]],
                Union["ResponseFormatJSONSchemaInput", Mapping[str, object]],
                Union["ResponseFormatRegexInput", Mapping[str, object]],
                None,
            ],
            Omit,
        ] = omit,
        response_formatting_locale: Union[Union[str, None], Omit] = omit,
        response_metadata: Union[Union[dict[str, Any], None], Omit] = omit,
        return_images: Union[Union[bool, None], Omit] = omit,
        return_related_questions: Union[Union[bool, None], Omit] = omit,
        safe_search: Union[Union[bool, None], Omit] = omit,
        search_after_date_filter: Union[Union[str, None], Omit] = omit,
        search_before_date_filter: Union[Union[str, None], Omit] = omit,
        search_domain_filter: Union[Union[Sequence[str], None], Omit] = omit,
        search_internal_properties: Union[Union[dict[str, Any], None], Omit] = omit,
        search_language_filter: Union[Union[Sequence[str], None], Omit] = omit,
        search_mode: Union[Union[Literal["web", "academic", "sec"], None], Omit] = omit,
        search_recency_filter: Union[
            Union[Literal["hour", "day", "week", "month", "year"], None], Omit
        ] = omit,
        search_tenant: Union[Union[str, None], Omit] = omit,
        stop: Union[Union[str, Sequence[str], None], Omit] = omit,
        stream: Union[Union[bool, None], Omit] = omit,
        stream_mode: Union[Literal["full", "concise"], Omit] = omit,
        temperature: Union[Union[float, None], Omit] = omit,
        thread_id: Union[Union[str, None], Omit] = omit,
        tool_choice: Union[
            Union[Literal["none", "auto", "required"], None], Omit
        ] = omit,
        tools: Union[
            Union[Sequence[Union["ToolSpecInput", Mapping[str, object]]], None], Omit
        ] = omit,
        top_k: Union[Union[int, None], Omit] = omit,
        top_logprobs: Union[Union[int, None], Omit] = omit,
        top_p: Union[Union[float, None], Omit] = omit,
        updated_after_timestamp: Union[Union[int, None], Omit] = omit,
        updated_before_timestamp: Union[Union[int, None], Omit] = omit,
        use_threads: Union[Union[bool, None], Omit] = omit,
        user_original_query: Union[Union[str, None], Omit] = omit,
        web_search_options: Union[
            Union["WebSearchOptionsInput", Mapping[str, object]], Omit
        ] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> Union["CompletionResponseOutput", AsyncStream["CompletionResponseOutput"]]:
        _body = ApiChatCompletionsRequestInput.model_validate(
            _without_omitted(
                {
                    "_debug_pro_search": _debug_pro_search,
                    "_force_new_agent": _force_new_agent,
                    "_inputs": _inputs,
                    "_prompt_token_length": _prompt_token_length,
                    "best_of": best_of,
                    "country": country,
                    "cum_logprobs": cum_logprobs,
                    "disable_search": disable_search,
                    "diverse_first_token": diverse_first_token,
                    "enable_search_classifier": enable_search_classifier,
                    "file_workspace_id": file_workspace_id,
                    "frequency_penalty": frequency_penalty,
                    "has_image_url": has_image_url,
                    "image_domain_filter": image_domain_filter,
                    "image_format_filter": image_format_filter,
                    "language_preference": language_preference,
                    "last_updated_after_filter": last_updated_after_filter,
                    "last_updated_before_filter": last_updated_before_filter,
                    "latitude": latitude,
                    "logprobs": logprobs,
                    "longitude": longitude,
                    "max_tokens": max_tokens,
                    "messages": messages,
                    "model": model,
                    "n": n,
                    "num_images": num_images,
                    "num_search_results": num_search_results,
                    "parallel_tool_calls": parallel_tool_calls,
                    "presence_penalty": presence_penalty,
                    "ranking_model": ranking_model,
                    "reasoning_effort": reasoning_effort,
                    "response_format": response_format,
                    "response_formatting_locale": response_formatting_locale,
                    "response_metadata": response_metadata,
                    "return_images": return_images,
                    "return_related_questions": return_related_questions,
                    "safe_search": safe_search,
                    "search_after_date_filter": search_after_date_filter,
                    "search_before_date_filter": search_before_date_filter,
                    "search_domain_filter": search_domain_filter,
                    "search_internal_properties": search_internal_properties,
                    "search_language_filter": search_language_filter,
                    "search_mode": search_mode,
                    "search_recency_filter": search_recency_filter,
                    "search_tenant": search_tenant,
                    "stop": stop,
                    "stream": stream,
                    "stream_mode": stream_mode,
                    "temperature": temperature,
                    "thread_id": thread_id,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "updated_after_timestamp": updated_after_timestamp,
                    "updated_before_timestamp": updated_before_timestamp,
                    "use_threads": use_threads,
                    "user_original_query": user_original_query,
                    "web_search_options": web_search_options,
                }
            )
        )
        _body_data = _body.model_dump(mode="json", by_alias=True, exclude_unset=True)
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            Union["CompletionResponseOutput", AsyncStream["CompletionResponseOutput"]],
            await self._post(
                "/chat/completions",
                cast_to=CompletionResponseOutput,
                body=_body_data,
                stream=stream is True,
                stream_cls=AsyncStream["CompletionResponseOutput"],
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result


class AsyncClientResponsesFilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientResponsesFilesResourceWithRawResponse:
        return AsyncClientResponsesFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(
        self,
    ) -> AsyncClientResponsesFilesResourceWithStreamingResponse:
        return AsyncClientResponsesFilesResourceWithStreamingResponse(self)

    async def content(
        self,
        file_id: str,
        *,
        response_id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        if not file_id:
            raise ValueError(
                "Expected a non-empty value for `file_id` but received " + repr(file_id)
            )
        if not response_id:
            raise ValueError(
                "Expected a non-empty value for `response_id` but received "
                + repr(response_id)
            )
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers(
            {"Accept": "application/octet-stream"}
        )
        _result = cast(
            AsyncBinaryAPIResponse,
            await self._get(
                "/v1/responses/{response_id}/files/{file_id}/content".format(
                    file_id=file_id, response_id=response_id
                ),
                cast_to=AsyncBinaryAPIResponse,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result

    async def list(
        self,
        response_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> "ResponseFileListOutput":
        if not response_id:
            raise ValueError(
                "Expected a non-empty value for `response_id` but received "
                + repr(response_id)
            )
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            "ResponseFileListOutput",
            await self._get(
                "/v1/responses/{response_id}/files".format(response_id=response_id),
                cast_to=ResponseFileListOutput,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result


class AsyncClientAsyncResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientAsyncResourceWithRawResponse:
        return AsyncClientAsyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientAsyncResourceWithStreamingResponse:
        return AsyncClientAsyncResourceWithStreamingResponse(self)

    @cached_property
    def chat(self) -> AsyncClientAsyncChatResource:
        return AsyncClientAsyncChatResource(self._client)


class AsyncClientBrowserResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientBrowserResourceWithRawResponse:
        return AsyncClientBrowserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(
        self,
    ) -> AsyncClientBrowserResourceWithStreamingResponse:
        return AsyncClientBrowserResourceWithStreamingResponse(self)

    @cached_property
    def sessions(self) -> AsyncClientBrowserSessionsResource:
        return AsyncClientBrowserSessionsResource(self._client)


class AsyncClientChatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientChatResourceWithRawResponse:
        return AsyncClientChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientChatResourceWithStreamingResponse:
        return AsyncClientChatResourceWithStreamingResponse(self)

    @cached_property
    def completions(self) -> AsyncClientChatCompletionsResource:
        return AsyncClientChatCompletionsResource(self._client)


class AsyncClientContextualizedEmbeddingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(
        self,
    ) -> AsyncClientContextualizedEmbeddingsResourceWithRawResponse:
        return AsyncClientContextualizedEmbeddingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(
        self,
    ) -> AsyncClientContextualizedEmbeddingsResourceWithStreamingResponse:
        return AsyncClientContextualizedEmbeddingsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        input: Sequence[Sequence[str]],
        model: Literal["pplx-embed-context-v1-0.6b", "pplx-embed-context-v1-4b"],
        dimensions: Union[int, Omit] = omit,
        encoding_format: Union[Literal["base64_int8", "base64_binary"], Omit] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> "ContextualizedEmbeddingsResponseOutput":
        _body = ContextualizedEmbeddingsRequestInput.model_validate(
            _without_omitted(
                {
                    "dimensions": dimensions,
                    "encoding_format": encoding_format,
                    "input": input,
                    "model": model,
                }
            )
        )
        _body_data = _body.model_dump(mode="json", by_alias=True, exclude_unset=True)
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            "ContextualizedEmbeddingsResponseOutput",
            await self._post(
                "/v1/contextualizedembeddings",
                cast_to=ContextualizedEmbeddingsResponseOutput,
                body=_body_data,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result


class AsyncClientEmbeddingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientEmbeddingsResourceWithRawResponse:
        return AsyncClientEmbeddingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(
        self,
    ) -> AsyncClientEmbeddingsResourceWithStreamingResponse:
        return AsyncClientEmbeddingsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        input: Union[str, Sequence[str]],
        model: Literal["pplx-embed-v1-0.6b", "pplx-embed-v1-4b"],
        dimensions: Union[int, Omit] = omit,
        encoding_format: Union[Literal["base64_int8", "base64_binary"], Omit] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> "EmbeddingsResponseOutput":
        _body = EmbeddingsRequestInput.model_validate(
            _without_omitted(
                {
                    "dimensions": dimensions,
                    "encoding_format": encoding_format,
                    "input": input,
                    "model": model,
                }
            )
        )
        _body_data = _body.model_dump(mode="json", by_alias=True, exclude_unset=True)
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            "EmbeddingsResponseOutput",
            await self._post(
                "/v1/embeddings",
                cast_to=EmbeddingsResponseOutput,
                body=_body_data,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result


class AsyncClientResponsesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientResponsesResourceWithRawResponse:
        return AsyncClientResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(
        self,
    ) -> AsyncClientResponsesResourceWithStreamingResponse:
        return AsyncClientResponsesResourceWithStreamingResponse(self)

    async def cancel(
        self,
        response_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> "ResponsesCancelResponseOutput":
        if not response_id:
            raise ValueError(
                "Expected a non-empty value for `response_id` but received "
                + repr(response_id)
            )
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            "ResponsesCancelResponseOutput",
            await self._post(
                "/v1/responses/{response_id}/cancel".format(response_id=response_id),
                cast_to=ResponsesCancelResponseOutput,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result

    @overload
    async def create(
        self,
        *,
        input: "InputInput",
        background: Union[Union[bool, None], Omit] = omit,
        instructions: Union[str, Omit] = omit,
        language_preference: Union[str, Omit] = omit,
        max_output_tokens: Union[int, Omit] = omit,
        max_steps: Union[int, Omit] = omit,
        model: Union[str, Omit] = omit,
        models: Union[Sequence[str], Omit] = omit,
        preset: Union[str, Omit] = omit,
        previous_response_id: Union[str, Omit] = omit,
        reasoning: Union[
            Union["ReasoningConfigInput", Mapping[str, object]], Omit
        ] = omit,
        response_format: Union[
            Union["ResponseFormatInput", Mapping[str, object]], Omit
        ] = omit,
        skills: Union[Sequence[Union["SkillInput", Mapping[str, object]]], Omit] = omit,
        store: Union[bool, Omit] = omit,
        stream: Union[Literal[False], Omit] = omit,
        temperature: Union[float, Omit] = omit,
        tools: Union[Sequence[Union["ToolInput", Mapping[str, object]]], Omit] = omit,
        top_p: Union[float, Omit] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> ResponsesResponseOutput: ...
    @overload
    async def create(
        self,
        *,
        input: "InputInput",
        background: Union[Union[bool, None], Omit] = omit,
        instructions: Union[str, Omit] = omit,
        language_preference: Union[str, Omit] = omit,
        max_output_tokens: Union[int, Omit] = omit,
        max_steps: Union[int, Omit] = omit,
        model: Union[str, Omit] = omit,
        models: Union[Sequence[str], Omit] = omit,
        preset: Union[str, Omit] = omit,
        previous_response_id: Union[str, Omit] = omit,
        reasoning: Union[
            Union["ReasoningConfigInput", Mapping[str, object]], Omit
        ] = omit,
        response_format: Union[
            Union["ResponseFormatInput", Mapping[str, object]], Omit
        ] = omit,
        skills: Union[Sequence[Union["SkillInput", Mapping[str, object]]], Omit] = omit,
        store: Union[bool, Omit] = omit,
        stream: Literal[True],
        temperature: Union[float, Omit] = omit,
        tools: Union[Sequence[Union["ToolInput", Mapping[str, object]]], Omit] = omit,
        top_p: Union[float, Omit] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> AsyncStream["ResponseStreamEventOutput"]: ...
    async def create(
        self,
        *,
        input: "InputInput",
        background: Union[Union[bool, None], Omit] = omit,
        instructions: Union[str, Omit] = omit,
        language_preference: Union[str, Omit] = omit,
        max_output_tokens: Union[int, Omit] = omit,
        max_steps: Union[int, Omit] = omit,
        model: Union[str, Omit] = omit,
        models: Union[Sequence[str], Omit] = omit,
        preset: Union[str, Omit] = omit,
        previous_response_id: Union[str, Omit] = omit,
        reasoning: Union[
            Union["ReasoningConfigInput", Mapping[str, object]], Omit
        ] = omit,
        response_format: Union[
            Union["ResponseFormatInput", Mapping[str, object]], Omit
        ] = omit,
        skills: Union[Sequence[Union["SkillInput", Mapping[str, object]]], Omit] = omit,
        store: Union[bool, Omit] = omit,
        stream: Union[bool, Omit] = omit,
        temperature: Union[float, Omit] = omit,
        tools: Union[Sequence[Union["ToolInput", Mapping[str, object]]], Omit] = omit,
        top_p: Union[float, Omit] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> Union["ResponsesResponseOutput", AsyncStream["ResponseStreamEventOutput"]]:
        _body = ResponsesRequestInput.model_validate(
            _without_omitted(
                {
                    "background": background,
                    "input": input,
                    "instructions": instructions,
                    "language_preference": language_preference,
                    "max_output_tokens": max_output_tokens,
                    "max_steps": max_steps,
                    "model": model,
                    "models": models,
                    "preset": preset,
                    "previous_response_id": previous_response_id,
                    "reasoning": reasoning,
                    "response_format": response_format,
                    "skills": skills,
                    "store": store,
                    "stream": stream,
                    "temperature": temperature,
                    "tools": tools,
                    "top_p": top_p,
                }
            )
        )
        _body_data = _body.model_dump(mode="json", by_alias=True, exclude_unset=True)
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            Union["ResponsesResponseOutput", AsyncStream["ResponseStreamEventOutput"]],
            await self._post(
                "/v1/responses",
                cast_to=ResponsesResponseOutput,
                body=_body_data,
                stream=stream is True,
                stream_cls=AsyncStream["ResponseStreamEventOutput"],
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result

    async def retrieve(
        self,
        response_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> "ResponsesResponseOutput":
        if not response_id:
            raise ValueError(
                "Expected a non-empty value for `response_id` but received "
                + repr(response_id)
            )
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            "ResponsesResponseOutput",
            await self._get(
                "/v1/responses/{response_id}".format(response_id=response_id),
                cast_to=ResponsesResponseOutput,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result

    @cached_property
    def files(self) -> AsyncClientResponsesFilesResource:
        return AsyncClientResponsesFilesResource(self._client)


class AsyncClientSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientSearchResourceWithRawResponse:
        return AsyncClientSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientSearchResourceWithStreamingResponse:
        return AsyncClientSearchResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        query: Union[str, Sequence[str]],
        country: Union[Union[str, None], Omit] = omit,
        display_server_time: Union[bool, Omit] = omit,
        last_updated_after_filter: Union[Union[str, None], Omit] = omit,
        last_updated_before_filter: Union[Union[str, None], Omit] = omit,
        max_results: Union[int, Omit] = omit,
        max_tokens: Union[int, Omit] = omit,
        max_tokens_per_page: Union[int, Omit] = omit,
        search_after_date_filter: Union[Union[str, None], Omit] = omit,
        search_before_date_filter: Union[Union[str, None], Omit] = omit,
        search_context_size: Union[Literal["low", "medium", "high"], Omit] = omit,
        search_domain_filter: Union[Union[Sequence[str], None], Omit] = omit,
        search_language_filter: Union[Union[Sequence[str], None], Omit] = omit,
        search_mode: Union[Union[Literal["web", "academic", "sec"], None], Omit] = omit,
        search_recency_filter: Union[
            Union[Literal["hour", "day", "week", "month", "year"], None], Omit
        ] = omit,
        search_type: Union[Union[Literal["web", "people"], None], Omit] = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> "ApiSearchResponseOutput":
        _body = ApiSearchRequestInput.model_validate(
            _without_omitted(
                {
                    "country": country,
                    "display_server_time": display_server_time,
                    "last_updated_after_filter": last_updated_after_filter,
                    "last_updated_before_filter": last_updated_before_filter,
                    "max_results": max_results,
                    "max_tokens": max_tokens,
                    "max_tokens_per_page": max_tokens_per_page,
                    "query": query,
                    "search_after_date_filter": search_after_date_filter,
                    "search_before_date_filter": search_before_date_filter,
                    "search_context_size": search_context_size,
                    "search_domain_filter": search_domain_filter,
                    "search_language_filter": search_language_filter,
                    "search_mode": search_mode,
                    "search_recency_filter": search_recency_filter,
                    "search_type": search_type,
                }
            )
        )
        _body_data = _body.model_dump(mode="json", by_alias=True, exclude_unset=True)
        _query_parameters = _without_omitted({})
        _header_parameters = _without_omitted_headers({})
        _result = cast(
            "ApiSearchResponseOutput",
            await self._post(
                "/search",
                cast_to=ApiSearchResponseOutput,
                body=_body_data,
                options=make_request_options(
                    extra_headers={**_header_parameters, **(extra_headers or {})},
                    extra_query={**_query_parameters, **(extra_query or {})},
                    extra_body=extra_body,
                    timeout=timeout,
                ),
            ),
        )
        return _result


class AsyncClientAsyncChatCompletionsResourceWithRawResponse:
    def __init__(self, resource: AsyncClientAsyncChatCompletionsResource) -> None:
        self._resource = resource
        self.create = async_to_raw_response_wrapper(resource, "create")
        self.get = async_to_raw_response_wrapper(resource, "get")
        self.list = async_to_raw_response_wrapper(resource, "list")


class AsyncClientAsyncChatCompletionsResourceWithStreamingResponse:
    def __init__(self, resource: AsyncClientAsyncChatCompletionsResource) -> None:
        self._resource = resource
        self.create = async_to_streamed_response_wrapper(resource, "create")
        self.get = async_to_streamed_response_wrapper(resource, "get")
        self.list = async_to_streamed_response_wrapper(resource, "list")


class AsyncClientAsyncChatResourceWithRawResponse:
    def __init__(self, resource: AsyncClientAsyncChatResource) -> None:
        self._resource = resource

    @cached_property
    def completions(self) -> AsyncClientAsyncChatCompletionsResourceWithRawResponse:
        return AsyncClientAsyncChatCompletionsResourceWithRawResponse(
            self._resource.completions
        )


class AsyncClientAsyncChatResourceWithStreamingResponse:
    def __init__(self, resource: AsyncClientAsyncChatResource) -> None:
        self._resource = resource

    @cached_property
    def completions(
        self,
    ) -> AsyncClientAsyncChatCompletionsResourceWithStreamingResponse:
        return AsyncClientAsyncChatCompletionsResourceWithStreamingResponse(
            self._resource.completions
        )


class AsyncClientBrowserSessionsResourceWithRawResponse:
    def __init__(self, resource: AsyncClientBrowserSessionsResource) -> None:
        self._resource = resource
        self.create = async_to_raw_response_wrapper(resource, "create")
        self.delete = async_to_raw_response_wrapper(resource, "delete")


class AsyncClientBrowserSessionsResourceWithStreamingResponse:
    def __init__(self, resource: AsyncClientBrowserSessionsResource) -> None:
        self._resource = resource
        self.create = async_to_streamed_response_wrapper(resource, "create")
        self.delete = async_to_streamed_response_wrapper(resource, "delete")


class AsyncClientChatCompletionsResourceWithRawResponse:
    def __init__(self, resource: AsyncClientChatCompletionsResource) -> None:
        self._resource = resource
        self.create = async_to_raw_response_wrapper(resource, "create")


class AsyncClientChatCompletionsResourceWithStreamingResponse:
    def __init__(self, resource: AsyncClientChatCompletionsResource) -> None:
        self._resource = resource
        self.create = async_to_streamed_response_wrapper(resource, "create")


class AsyncClientResponsesFilesResourceWithRawResponse:
    def __init__(self, resource: AsyncClientResponsesFilesResource) -> None:
        self._resource = resource
        self.content = async_to_raw_response_wrapper(resource, "content")
        self.list = async_to_raw_response_wrapper(resource, "list")


class AsyncClientResponsesFilesResourceWithStreamingResponse:
    def __init__(self, resource: AsyncClientResponsesFilesResource) -> None:
        self._resource = resource
        self.content = async_to_streamed_response_wrapper(resource, "content")
        self.list = async_to_streamed_response_wrapper(resource, "list")


class AsyncClientAsyncResourceWithRawResponse:
    def __init__(self, resource: AsyncClientAsyncResource) -> None:
        self._resource = resource

    @cached_property
    def chat(self) -> AsyncClientAsyncChatResourceWithRawResponse:
        return AsyncClientAsyncChatResourceWithRawResponse(self._resource.chat)


class AsyncClientAsyncResourceWithStreamingResponse:
    def __init__(self, resource: AsyncClientAsyncResource) -> None:
        self._resource = resource

    @cached_property
    def chat(self) -> AsyncClientAsyncChatResourceWithStreamingResponse:
        return AsyncClientAsyncChatResourceWithStreamingResponse(self._resource.chat)


class AsyncClientBrowserResourceWithRawResponse:
    def __init__(self, resource: AsyncClientBrowserResource) -> None:
        self._resource = resource

    @cached_property
    def sessions(self) -> AsyncClientBrowserSessionsResourceWithRawResponse:
        return AsyncClientBrowserSessionsResourceWithRawResponse(
            self._resource.sessions
        )


class AsyncClientBrowserResourceWithStreamingResponse:
    def __init__(self, resource: AsyncClientBrowserResource) -> None:
        self._resource = resource

    @cached_property
    def sessions(self) -> AsyncClientBrowserSessionsResourceWithStreamingResponse:
        return AsyncClientBrowserSessionsResourceWithStreamingResponse(
            self._resource.sessions
        )


class AsyncClientChatResourceWithRawResponse:
    def __init__(self, resource: AsyncClientChatResource) -> None:
        self._resource = resource

    @cached_property
    def completions(self) -> AsyncClientChatCompletionsResourceWithRawResponse:
        return AsyncClientChatCompletionsResourceWithRawResponse(
            self._resource.completions
        )


class AsyncClientChatResourceWithStreamingResponse:
    def __init__(self, resource: AsyncClientChatResource) -> None:
        self._resource = resource

    @cached_property
    def completions(self) -> AsyncClientChatCompletionsResourceWithStreamingResponse:
        return AsyncClientChatCompletionsResourceWithStreamingResponse(
            self._resource.completions
        )


class AsyncClientContextualizedEmbeddingsResourceWithRawResponse:
    def __init__(self, resource: AsyncClientContextualizedEmbeddingsResource) -> None:
        self._resource = resource
        self.create = async_to_raw_response_wrapper(resource, "create")


class AsyncClientContextualizedEmbeddingsResourceWithStreamingResponse:
    def __init__(self, resource: AsyncClientContextualizedEmbeddingsResource) -> None:
        self._resource = resource
        self.create = async_to_streamed_response_wrapper(resource, "create")


class AsyncClientEmbeddingsResourceWithRawResponse:
    def __init__(self, resource: AsyncClientEmbeddingsResource) -> None:
        self._resource = resource
        self.create = async_to_raw_response_wrapper(resource, "create")


class AsyncClientEmbeddingsResourceWithStreamingResponse:
    def __init__(self, resource: AsyncClientEmbeddingsResource) -> None:
        self._resource = resource
        self.create = async_to_streamed_response_wrapper(resource, "create")


class AsyncClientResponsesResourceWithRawResponse:
    def __init__(self, resource: AsyncClientResponsesResource) -> None:
        self._resource = resource
        self.cancel = async_to_raw_response_wrapper(resource, "cancel")
        self.create = async_to_raw_response_wrapper(resource, "create")
        self.retrieve = async_to_raw_response_wrapper(resource, "retrieve")

    @cached_property
    def files(self) -> AsyncClientResponsesFilesResourceWithRawResponse:
        return AsyncClientResponsesFilesResourceWithRawResponse(self._resource.files)


class AsyncClientResponsesResourceWithStreamingResponse:
    def __init__(self, resource: AsyncClientResponsesResource) -> None:
        self._resource = resource
        self.cancel = async_to_streamed_response_wrapper(resource, "cancel")
        self.create = async_to_streamed_response_wrapper(resource, "create")
        self.retrieve = async_to_streamed_response_wrapper(resource, "retrieve")

    @cached_property
    def files(self) -> AsyncClientResponsesFilesResourceWithStreamingResponse:
        return AsyncClientResponsesFilesResourceWithStreamingResponse(
            self._resource.files
        )


class AsyncClientSearchResourceWithRawResponse:
    def __init__(self, resource: AsyncClientSearchResource) -> None:
        self._resource = resource
        self.create = async_to_raw_response_wrapper(resource, "create")


class AsyncClientSearchResourceWithStreamingResponse:
    def __init__(self, resource: AsyncClientSearchResource) -> None:
        self._resource = resource
        self.create = async_to_streamed_response_wrapper(resource, "create")


class AsyncPerplexitySdk(AsyncAPIResource):
    @cached_property
    def async_(self) -> AsyncClientAsyncResource:
        return AsyncClientAsyncResource(self._client)

    @cached_property
    def browser(self) -> AsyncClientBrowserResource:
        return AsyncClientBrowserResource(self._client)

    @cached_property
    def chat(self) -> AsyncClientChatResource:
        return AsyncClientChatResource(self._client)

    @cached_property
    def contextualized_embeddings(self) -> AsyncClientContextualizedEmbeddingsResource:
        return AsyncClientContextualizedEmbeddingsResource(self._client)

    @cached_property
    def embeddings(self) -> AsyncClientEmbeddingsResource:
        return AsyncClientEmbeddingsResource(self._client)

    @cached_property
    def responses(self) -> AsyncClientResponsesResource:
        return AsyncClientResponsesResource(self._client)

    @cached_property
    def search(self) -> AsyncClientSearchResource:
        return AsyncClientSearchResource(self._client)
