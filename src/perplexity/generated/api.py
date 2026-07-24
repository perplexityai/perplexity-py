from __future__ import annotations
from typing import Any, AsyncIterable, Optional, Union
from typing_extensions import (
    Literal,
    Never,
    NotRequired,
    Protocol,
    Required,
    TypeAlias,
    TypedDict,
)

AnnotationInput = TypedDict(
    "AnnotationInput",
    {
        "end_index": NotRequired[int],
        "start_index": NotRequired[int],
        "title": NotRequired[str],
        "type": NotRequired[str],
        "url": NotRequired[str],
    },
    total=False,
)
AnnotationOutput = TypedDict(
    "AnnotationOutput",
    {
        "end_index": NotRequired[int],
        "start_index": NotRequired[int],
        "title": NotRequired[str],
        "type": NotRequired[str],
        "url": NotRequired[str],
    },
    total=False,
)
ApiErrorInput = TypedDict(
    "ApiErrorInput", {"error": NotRequired[dict[str, Any]]}, total=False
)
ApiErrorOutput = TypedDict(
    "ApiErrorOutput", {"error": NotRequired[dict[str, Any]]}, total=False
)
ChatChoiceInput = TypedDict(
    "ChatChoiceInput",
    {
        "finish_reason": Required[str],
        "index": Required[int],
        "message": Required["ChatMessageInput"],
    },
    total=False,
)
ChatChoiceOutput = TypedDict(
    "ChatChoiceOutput",
    {
        "finish_reason": Required[str],
        "index": Required[int],
        "message": Required["ChatMessageOutput"],
    },
    total=False,
)
ChatMessageInput = TypedDict(
    "ChatMessageInput",
    {
        "content": Required["MessageContentInput"],
        "role": Required[Literal["system", "user", "assistant"]],
    },
    total=False,
)
ChatMessageOutput = TypedDict(
    "ChatMessageOutput",
    {
        "content": Required["MessageContentOutput"],
        "role": Required[Literal["system", "user", "assistant"]],
    },
    total=False,
)
CompletionDoneChunkInput = TypedDict(
    "CompletionDoneChunkInput",
    {
        "choices": Required[list["ChatChoiceInput"]],
        "created": Required[int],
        "id": Required[str],
        "images": NotRequired[list["ImageResultInput"]],
        "model": Required[str],
        "object": Required["ObjectTypeInput"],
        "search_results": NotRequired[list["SearchResultInput"]],
        "usage": NotRequired["UsageInput"],
    },
    total=False,
)
CompletionDoneChunkOutput = TypedDict(
    "CompletionDoneChunkOutput",
    {
        "choices": Required[list["ChatChoiceOutput"]],
        "created": Required[int],
        "id": Required[str],
        "images": NotRequired[list["ImageResultOutput"]],
        "model": Required[str],
        "object": Required["ObjectTypeOutput"],
        "search_results": NotRequired[list["SearchResultOutput"]],
        "usage": NotRequired["UsageOutput"],
    },
    total=False,
)
CompletionTokensDetailsInput = TypedDict(
    "CompletionTokensDetailsInput", {"reasoning_tokens": Required[int]}, total=False
)
CompletionTokensDetailsOutput = TypedDict(
    "CompletionTokensDetailsOutput", {"reasoning_tokens": Required[int]}, total=False
)
ContentBlockInput = TypedDict(
    "ContentBlockInput",
    {
        "image_url": NotRequired["ImageURLInput"],
        "text": NotRequired[str],
        "type": Required[Literal["text", "image_url"]],
    },
    total=False,
)
ContentBlockOutput = TypedDict(
    "ContentBlockOutput",
    {
        "image_url": NotRequired["ImageURLOutput"],
        "text": NotRequired[str],
        "type": Required[Literal["text", "image_url"]],
    },
    total=False,
)
ContentPartInput = TypedDict(
    "ContentPartInput",
    {
        "annotations": NotRequired[list["AnnotationInput"]],
        "text": Required[str],
        "type": Required["ContentPartTypeInput"],
    },
    total=False,
)
ContentPartOutput = TypedDict(
    "ContentPartOutput",
    {
        "annotations": NotRequired[list["AnnotationOutput"]],
        "text": Required[str],
        "type": Required["ContentPartTypeOutput"],
    },
    total=False,
)
ContentPartTypeInput: TypeAlias = Literal["output_text"]
ContentPartTypeOutput: TypeAlias = Literal["output_text"]
CostInput = TypedDict(
    "CostInput",
    {
        "currency": Required["CurrencyInput"],
        "input_tokens_cost": Required[float],
        "output_tokens_cost": Required[float],
        "request_cost": NotRequired[float],
        "total_cost": Required[float],
    },
    total=False,
)
CostOutput = TypedDict(
    "CostOutput",
    {
        "currency": Required["CurrencyOutput"],
        "input_tokens_cost": Required[float],
        "output_tokens_cost": Required[float],
        "request_cost": NotRequired[float],
        "total_cost": Required[float],
    },
    total=False,
)
CurrencyInput: TypeAlias = Literal["USD"]
CurrencyOutput: TypeAlias = Literal["USD"]
DateInput: TypeAlias = str
DateOutput: TypeAlias = str
DateFiltersInput = TypedDict(
    "DateFiltersInput",
    {
        "last_updated_after_filter": NotRequired["DateInput"],
        "last_updated_before_filter": NotRequired["DateInput"],
        "search_after_date_filter": NotRequired["DateInput"],
        "search_before_date_filter": NotRequired["DateInput"],
        "search_recency_filter": NotRequired["SearchRecencyFilterInput"],
    },
    total=False,
)
DateFiltersOutput = TypedDict(
    "DateFiltersOutput",
    {
        "last_updated_after_filter": NotRequired["DateOutput"],
        "last_updated_before_filter": NotRequired["DateOutput"],
        "search_after_date_filter": NotRequired["DateOutput"],
        "search_before_date_filter": NotRequired["DateOutput"],
        "search_recency_filter": NotRequired["SearchRecencyFilterOutput"],
    },
    total=False,
)
ErrorInfoInput = TypedDict(
    "ErrorInfoInput",
    {"code": NotRequired[str], "message": Required[str], "type": NotRequired[str]},
    total=False,
)
ErrorInfoOutput = TypedDict(
    "ErrorInfoOutput",
    {"code": NotRequired[str], "message": Required[str], "type": NotRequired[str]},
    total=False,
)
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
]
FetchUrlContentDataInput = TypedDict(
    "FetchUrlContentDataInput",
    {"contents": NotRequired[list["UrlContentInput"]], "urls": NotRequired[list[str]]},
    total=False,
)
FetchUrlContentDataOutput = TypedDict(
    "FetchUrlContentDataOutput",
    {"contents": NotRequired[list["UrlContentOutput"]], "urls": NotRequired[list[str]]},
    total=False,
)
FetchUrlQueriesEventInput = TypedDict(
    "FetchUrlQueriesEventInput",
    {
        "sequence_number": Required[int],
        "thought": NotRequired[str],
        "type": Required["EventTypeInput"],
        "urls": Required[list[str]],
    },
    total=False,
)
FetchUrlQueriesEventOutput = TypedDict(
    "FetchUrlQueriesEventOutput",
    {
        "sequence_number": Required[int],
        "thought": NotRequired[str],
        "type": Required["EventTypeOutput"],
        "urls": Required[list[str]],
    },
    total=False,
)
FetchUrlResultsEventInput = TypedDict(
    "FetchUrlResultsEventInput",
    {
        "contents": Required[list["UrlContentInput"]],
        "sequence_number": Required[int],
        "thought": NotRequired[str],
        "type": Required["EventTypeInput"],
    },
    total=False,
)
FetchUrlResultsEventOutput = TypedDict(
    "FetchUrlResultsEventOutput",
    {
        "contents": Required[list["UrlContentOutput"]],
        "sequence_number": Required[int],
        "thought": NotRequired[str],
        "type": Required["EventTypeOutput"],
    },
    total=False,
)
FetchUrlResultsOutputItemInput = TypedDict(
    "FetchUrlResultsOutputItemInput",
    {
        "contents": Required[list["UrlContentInput"]],
        "type": Required[Literal["fetch_url_results"]],
    },
    total=False,
)
FetchUrlResultsOutputItemOutput = TypedDict(
    "FetchUrlResultsOutputItemOutput",
    {
        "contents": Required[list["UrlContentOutput"]],
        "type": Required[Literal["fetch_url_results"]],
    },
    total=False,
)
FetchUrlToolInput = TypedDict(
    "FetchUrlToolInput",
    {
        "max_urls": NotRequired[int],
        "total_budget_tokens": NotRequired[int],
        "type": Required[Literal["fetch_url"]],
    },
    total=False,
)
FetchUrlToolOutput = TypedDict(
    "FetchUrlToolOutput",
    {
        "max_urls": NotRequired[int],
        "total_budget_tokens": NotRequired[int],
        "type": Required[Literal["fetch_url"]],
    },
    total=False,
)
FlexIntInput: TypeAlias = int
FlexIntOutput: TypeAlias = int
ImageResultInput = TypedDict(
    "ImageResultInput",
    {
        "height": Required[int],
        "image_url": Required[str],
        "origin_url": Required[str],
        "title": NotRequired[str],
        "width": Required[int],
    },
    total=False,
)
ImageResultOutput = TypedDict(
    "ImageResultOutput",
    {
        "height": Required[int],
        "image_url": Required[str],
        "origin_url": Required[str],
        "title": NotRequired[str],
        "width": Required[int],
    },
    total=False,
)
ImageURLInput = TypedDict("ImageURLInput", {"url": Required[str]}, total=False)
ImageURLOutput = TypedDict("ImageURLOutput", {"url": Required[str]}, total=False)
ImagesSearchDataInput = TypedDict(
    "ImagesSearchDataInput",
    {
        "images": NotRequired[list["ImageResultInput"]],
        "search_keywords": NotRequired[list[str]],
    },
    total=False,
)
ImagesSearchDataOutput = TypedDict(
    "ImagesSearchDataOutput",
    {
        "images": NotRequired[list["ImageResultOutput"]],
        "search_keywords": NotRequired[list[str]],
    },
    total=False,
)
InputInput: TypeAlias = Union[str, list["InputMessageInput"]]
InputOutput: TypeAlias = Union[str, list["InputMessageOutput"]]
InputContentInput: TypeAlias = Union[str, list["InputContentPartInput"]]
InputContentOutput: TypeAlias = Union[str, list["InputContentPartOutput"]]
InputContentPartInput = TypedDict(
    "InputContentPartInput",
    {
        "image_url": NotRequired[str],
        "text": NotRequired[str],
        "type": Required[Literal["input_text", "input_image"]],
    },
    total=False,
)
InputContentPartOutput = TypedDict(
    "InputContentPartOutput",
    {
        "image_url": NotRequired[str],
        "text": NotRequired[str],
        "type": Required[Literal["input_text", "input_image"]],
    },
    total=False,
)
InputMessageInput = TypedDict(
    "InputMessageInput",
    {
        "content": Required["InputContentInput"],
        "role": Required[Literal["user", "assistant", "system", "developer"]],
        "type": NotRequired[Literal["message"]],
    },
    total=False,
)
InputMessageOutput = TypedDict(
    "InputMessageOutput",
    {
        "content": Required["InputContentOutput"],
        "role": Required[Literal["user", "assistant", "system", "developer"]],
        "type": NotRequired[Literal["message"]],
    },
    total=False,
)
JSONSchemaFormatInput = TypedDict(
    "JSONSchemaFormatInput",
    {
        "description": NotRequired[str],
        "name": Required[str],
        "schema": Required[dict[str, Any]],
        "strict": NotRequired[bool],
    },
    total=False,
)
JSONSchemaFormatOutput = TypedDict(
    "JSONSchemaFormatOutput",
    {
        "description": NotRequired[str],
        "name": Required[str],
        "schema": Required[dict[str, Any]],
        "strict": NotRequired[bool],
    },
    total=False,
)
McpCallOutputItemInput = TypedDict(
    "McpCallOutputItemInput",
    {
        "arguments": Required[str],
        "error": NotRequired[Optional[str]],
        "id": Required[str],
        "name": Required[str],
        "output": NotRequired[str],
        "server_label": Required[str],
        "type": Required[Literal["mcp_call"]],
    },
    total=False,
)
McpCallOutputItemOutput = TypedDict(
    "McpCallOutputItemOutput",
    {
        "arguments": Required[str],
        "error": NotRequired[Optional[str]],
        "id": Required[str],
        "name": Required[str],
        "output": NotRequired[str],
        "server_label": Required[str],
        "type": Required[Literal["mcp_call"]],
    },
    total=False,
)
McpListToolsOutputItemInput = TypedDict(
    "McpListToolsOutputItemInput",
    {
        "error": NotRequired[str],
        "id": Required[str],
        "server_label": Required[str],
        "tools": Required[list["McpToolDefInput"]],
        "type": Required[Literal["mcp_list_tools"]],
    },
    total=False,
)
McpListToolsOutputItemOutput = TypedDict(
    "McpListToolsOutputItemOutput",
    {
        "error": NotRequired[str],
        "id": Required[str],
        "server_label": Required[str],
        "tools": Required[list["McpToolDefOutput"]],
        "type": Required[Literal["mcp_list_tools"]],
    },
    total=False,
)
McpToolInput = TypedDict(
    "McpToolInput",
    {
        "allowed_tools": NotRequired[list[str]],
        "authorization": NotRequired[str],
        "headers": NotRequired[dict[str, Any]],
        "server_label": Required[str],
        "server_url": Required[str],
        "type": Required[Literal["mcp"]],
    },
    total=False,
)
McpToolOutput = TypedDict(
    "McpToolOutput",
    {
        "allowed_tools": NotRequired[list[str]],
        "authorization": NotRequired[str],
        "headers": NotRequired[dict[str, Any]],
        "server_label": Required[str],
        "server_url": Required[str],
        "type": Required[Literal["mcp"]],
    },
    total=False,
)
McpToolDefInput = TypedDict(
    "McpToolDefInput",
    {
        "description": NotRequired[str],
        "input_schema": Required[dict[str, Any]],
        "name": Required[str],
    },
    total=False,
)
McpToolDefOutput = TypedDict(
    "McpToolDefOutput",
    {
        "description": NotRequired[str],
        "input_schema": Required[dict[str, Any]],
        "name": Required[str],
    },
    total=False,
)
MessageContentInput: TypeAlias = Union[str, list["ContentBlockInput"]]
MessageContentOutput: TypeAlias = Union[str, list["ContentBlockOutput"]]
MessageOutputItemInput = TypedDict(
    "MessageOutputItemInput",
    {
        "content": Required[list["ContentPartInput"]],
        "id": Required[str],
        "role": Required["RoleTypeInput"],
        "status": Required["StatusInput"],
        "type": Required[Literal["message"]],
    },
    total=False,
)
MessageOutputItemOutput = TypedDict(
    "MessageOutputItemOutput",
    {
        "content": Required[list["ContentPartOutput"]],
        "id": Required[str],
        "role": Required["RoleTypeOutput"],
        "status": Required["StatusOutput"],
        "type": Required[Literal["message"]],
    },
    total=False,
)
ObjectTypeInput: TypeAlias = Literal[
    "chat.completion.chunk",
    "chat.completion.done",
    "chat.reasoning",
    "chat.reasoning.done",
]
ObjectTypeOutput: TypeAlias = Literal[
    "chat.completion.chunk",
    "chat.completion.done",
    "chat.reasoning",
    "chat.reasoning.done",
]
OutputItemInput: TypeAlias = Union[
    "MessageOutputItemInput",
    "SearchResultsOutputItemInput",
    "FetchUrlResultsOutputItemInput",
    "McpListToolsOutputItemInput",
    "McpCallOutputItemInput",
]
OutputItemOutput: TypeAlias = Union[
    "MessageOutputItemOutput",
    "SearchResultsOutputItemOutput",
    "FetchUrlResultsOutputItemOutput",
    "McpListToolsOutputItemOutput",
    "McpCallOutputItemOutput",
]
OutputItemAddedEventInput = TypedDict(
    "OutputItemAddedEventInput",
    {
        "item": Required["OutputItemInput"],
        "output_index": Required[int],
        "sequence_number": Required[int],
        "type": Required["EventTypeInput"],
    },
    total=False,
)
OutputItemAddedEventOutput = TypedDict(
    "OutputItemAddedEventOutput",
    {
        "item": Required["OutputItemOutput"],
        "output_index": Required[int],
        "sequence_number": Required[int],
        "type": Required["EventTypeOutput"],
    },
    total=False,
)
OutputItemDoneEventInput = TypedDict(
    "OutputItemDoneEventInput",
    {
        "item": Required["OutputItemInput"],
        "output_index": Required[int],
        "sequence_number": Required[int],
        "type": Required["EventTypeInput"],
    },
    total=False,
)
OutputItemDoneEventOutput = TypedDict(
    "OutputItemDoneEventOutput",
    {
        "item": Required["OutputItemOutput"],
        "output_index": Required[int],
        "sequence_number": Required[int],
        "type": Required["EventTypeOutput"],
    },
    total=False,
)
QueryFieldInput: TypeAlias = str
QueryFieldOutput: TypeAlias = str
ReasoningChoiceInput = TypedDict(
    "ReasoningChoiceInput",
    {
        "delta": Required["ReasoningDeltaInput"],
        "finish_reason": Required[Optional[str]],
        "index": Required[int],
    },
    total=False,
)
ReasoningChoiceOutput = TypedDict(
    "ReasoningChoiceOutput",
    {
        "delta": Required["ReasoningDeltaOutput"],
        "finish_reason": Required[Optional[str]],
        "index": Required[int],
    },
    total=False,
)
ReasoningChunkInput = TypedDict(
    "ReasoningChunkInput",
    {
        "choices": Required[list["ReasoningChoiceInput"]],
        "created": Required[int],
        "id": Required[str],
        "model": Required[str],
        "object": Required["ObjectTypeInput"],
    },
    total=False,
)
ReasoningChunkOutput = TypedDict(
    "ReasoningChunkOutput",
    {
        "choices": Required[list["ReasoningChoiceOutput"]],
        "created": Required[int],
        "id": Required[str],
        "model": Required[str],
        "object": Required["ObjectTypeOutput"],
    },
    total=False,
)
ReasoningConfigInput = TypedDict(
    "ReasoningConfigInput",
    {"effort": NotRequired[Literal["low", "medium", "high", "xhigh"]]},
    total=False,
)
ReasoningConfigOutput = TypedDict(
    "ReasoningConfigOutput",
    {"effort": NotRequired[Literal["low", "medium", "high", "xhigh"]]},
    total=False,
)
ReasoningDeltaInput = TypedDict(
    "ReasoningDeltaInput",
    {
        "content": NotRequired[str],
        "reasoning_steps": NotRequired[list["ReasoningStepInput"]],
        "role": NotRequired[str],
    },
    total=False,
)
ReasoningDeltaOutput = TypedDict(
    "ReasoningDeltaOutput",
    {
        "content": NotRequired[str],
        "reasoning_steps": NotRequired[list["ReasoningStepOutput"]],
        "role": NotRequired[str],
    },
    total=False,
)
ReasoningDoneChunkInput = TypedDict(
    "ReasoningDoneChunkInput",
    {
        "choices": Required[list["ReasoningChoiceInput"]],
        "created": Required[int],
        "id": Required[str],
        "images": NotRequired[list["ImageResultInput"]],
        "model": Required[str],
        "object": Required["ObjectTypeInput"],
        "search_results": NotRequired[list["SearchResultInput"]],
    },
    total=False,
)
ReasoningDoneChunkOutput = TypedDict(
    "ReasoningDoneChunkOutput",
    {
        "choices": Required[list["ReasoningChoiceOutput"]],
        "created": Required[int],
        "id": Required[str],
        "images": NotRequired[list["ImageResultOutput"]],
        "model": Required[str],
        "object": Required["ObjectTypeOutput"],
        "search_results": NotRequired[list["SearchResultOutput"]],
    },
    total=False,
)
ReasoningStartedEventInput = TypedDict(
    "ReasoningStartedEventInput",
    {
        "sequence_number": Required[int],
        "thought": NotRequired[str],
        "type": Required["EventTypeInput"],
    },
    total=False,
)
ReasoningStartedEventOutput = TypedDict(
    "ReasoningStartedEventOutput",
    {
        "sequence_number": Required[int],
        "thought": NotRequired[str],
        "type": Required["EventTypeOutput"],
    },
    total=False,
)
ReasoningStepInput = TypedDict(
    "ReasoningStepInput",
    {
        "fetch_url_content": NotRequired["FetchUrlContentDataInput"],
        "images_search": NotRequired["ImagesSearchDataInput"],
        "thought": Required[str],
        "type": NotRequired[str],
        "web_search": NotRequired["WebSearchDataInput"],
    },
    total=False,
)
ReasoningStepOutput = TypedDict(
    "ReasoningStepOutput",
    {
        "fetch_url_content": NotRequired["FetchUrlContentDataOutput"],
        "images_search": NotRequired["ImagesSearchDataOutput"],
        "thought": Required[str],
        "type": NotRequired[str],
        "web_search": NotRequired["WebSearchDataOutput"],
    },
    total=False,
)
ReasoningStoppedEventInput = TypedDict(
    "ReasoningStoppedEventInput",
    {
        "sequence_number": Required[int],
        "thought": NotRequired[str],
        "type": Required["EventTypeInput"],
    },
    total=False,
)
ReasoningStoppedEventOutput = TypedDict(
    "ReasoningStoppedEventOutput",
    {
        "sequence_number": Required[int],
        "thought": NotRequired[str],
        "type": Required["EventTypeOutput"],
    },
    total=False,
)
RequestInput = TypedDict(
    "RequestInput",
    {
        "language_preference": NotRequired[str],
        "max_tokens": NotRequired[int],
        "messages": Required[list["ChatMessageInput"]],
        "model": Required[str],
        "reasoning_effort": NotRequired[Literal["low", "medium", "high"]],
        "response_format": NotRequired["ResponseFormatInput"],
        "response_formatting_locale": NotRequired[str],
        "return_images": NotRequired[bool],
        "safe_mode": NotRequired[Literal["enabled", "disabled"]],
        "stream": NotRequired[bool],
        "temperature": NotRequired[float],
        "top_p": NotRequired[float],
        "web_search_options": NotRequired["WebSearchOptionsInput"],
    },
    total=False,
)
RequestOutput = TypedDict(
    "RequestOutput",
    {
        "language_preference": NotRequired[str],
        "max_tokens": NotRequired[int],
        "messages": Required[list["ChatMessageOutput"]],
        "model": Required[str],
        "reasoning_effort": NotRequired[Literal["low", "medium", "high"]],
        "response_format": NotRequired["ResponseFormatOutput"],
        "response_formatting_locale": NotRequired[str],
        "return_images": NotRequired[bool],
        "safe_mode": NotRequired[Literal["enabled", "disabled"]],
        "stream": NotRequired[bool],
        "temperature": NotRequired[float],
        "top_p": NotRequired[float],
        "web_search_options": NotRequired["WebSearchOptionsOutput"],
    },
    total=False,
)
ResponseInput = TypedDict(
    "ResponseInput",
    {
        "choices": Required[list["ChatChoiceInput"]],
        "created": Required[int],
        "id": Required[str],
        "images": NotRequired[list["ImageResultInput"]],
        "model": Required[str],
        "object": Required["ObjectTypeInput"],
        "search_results": NotRequired[list["SearchResultInput"]],
        "usage": NotRequired["UsageInput"],
    },
    total=False,
)
ResponseOutput = TypedDict(
    "ResponseOutput",
    {
        "choices": Required[list["ChatChoiceOutput"]],
        "created": Required[int],
        "id": Required[str],
        "images": NotRequired[list["ImageResultOutput"]],
        "model": Required[str],
        "object": Required["ObjectTypeOutput"],
        "search_results": NotRequired[list["SearchResultOutput"]],
        "usage": NotRequired["UsageOutput"],
    },
    total=False,
)
ResponseCompletedEventInput = TypedDict(
    "ResponseCompletedEventInput",
    {
        "response": NotRequired["ResponsesResponseInput"],
        "sequence_number": Required[int],
        "type": Required["EventTypeInput"],
    },
    total=False,
)
ResponseCompletedEventOutput = TypedDict(
    "ResponseCompletedEventOutput",
    {
        "response": NotRequired["ResponsesResponseOutput"],
        "sequence_number": Required[int],
        "type": Required["EventTypeOutput"],
    },
    total=False,
)
ResponseCreatedEventInput = TypedDict(
    "ResponseCreatedEventInput",
    {
        "response": NotRequired["ResponsesResponseInput"],
        "sequence_number": Required[int],
        "type": Required["EventTypeInput"],
    },
    total=False,
)
ResponseCreatedEventOutput = TypedDict(
    "ResponseCreatedEventOutput",
    {
        "response": NotRequired["ResponsesResponseOutput"],
        "sequence_number": Required[int],
        "type": Required["EventTypeOutput"],
    },
    total=False,
)
ResponseFailedEventInput = TypedDict(
    "ResponseFailedEventInput",
    {
        "error": Required["ErrorInfoInput"],
        "sequence_number": Required[int],
        "type": Required["EventTypeInput"],
    },
    total=False,
)
ResponseFailedEventOutput = TypedDict(
    "ResponseFailedEventOutput",
    {
        "error": Required["ErrorInfoOutput"],
        "sequence_number": Required[int],
        "type": Required["EventTypeOutput"],
    },
    total=False,
)
ResponseFormatInput = TypedDict(
    "ResponseFormatInput",
    {
        "json_schema": NotRequired["JSONSchemaFormatInput"],
        "type": Required[Literal["json_schema"]],
    },
    total=False,
)
ResponseFormatOutput = TypedDict(
    "ResponseFormatOutput",
    {
        "json_schema": NotRequired["JSONSchemaFormatOutput"],
        "type": Required[Literal["json_schema"]],
    },
    total=False,
)
ResponseInProgressEventInput = TypedDict(
    "ResponseInProgressEventInput",
    {
        "response": NotRequired["ResponsesResponseInput"],
        "sequence_number": Required[int],
        "type": Required["EventTypeInput"],
    },
    total=False,
)
ResponseInProgressEventOutput = TypedDict(
    "ResponseInProgressEventOutput",
    {
        "response": NotRequired["ResponsesResponseOutput"],
        "sequence_number": Required[int],
        "type": Required["EventTypeOutput"],
    },
    total=False,
)
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
]
ResponsesCostInput = TypedDict(
    "ResponsesCostInput",
    {
        "cache_creation_cost": NotRequired[float],
        "cache_read_cost": NotRequired[float],
        "currency": Required["CurrencyInput"],
        "input_cost": Required[float],
        "output_cost": Required[float],
        "tool_calls_cost": NotRequired[float],
        "tool_calls_cost_details": NotRequired[dict[str, Any]],
        "total_cost": Required[float],
    },
    total=False,
)
ResponsesCostOutput = TypedDict(
    "ResponsesCostOutput",
    {
        "cache_creation_cost": NotRequired[float],
        "cache_read_cost": NotRequired[float],
        "currency": Required["CurrencyOutput"],
        "input_cost": Required[float],
        "output_cost": Required[float],
        "tool_calls_cost": NotRequired[float],
        "tool_calls_cost_details": NotRequired[dict[str, Any]],
        "total_cost": Required[float],
    },
    total=False,
)
ResponsesObjectTypeInput: TypeAlias = Literal["response"]
ResponsesObjectTypeOutput: TypeAlias = Literal["response"]
ResponsesRequestInput = TypedDict(
    "ResponsesRequestInput",
    {
        "input": Required["InputInput"],
        "instructions": NotRequired[str],
        "language_preference": NotRequired[str],
        "max_output_tokens": NotRequired[int],
        "max_steps": NotRequired[int],
        "model": NotRequired[str],
        "preset": NotRequired[str],
        "previous_response_id": NotRequired[str],
        "reasoning": NotRequired["ReasoningConfigInput"],
        "response_format": NotRequired["ResponseFormatInput"],
        "store": NotRequired[bool],
        "stream": NotRequired[bool],
        "tools": NotRequired[list["ToolInput"]],
    },
    total=False,
)
ResponsesRequestOutput = TypedDict(
    "ResponsesRequestOutput",
    {
        "input": Required["InputOutput"],
        "instructions": NotRequired[str],
        "language_preference": NotRequired[str],
        "max_output_tokens": NotRequired[int],
        "max_steps": NotRequired[int],
        "model": NotRequired[str],
        "preset": NotRequired[str],
        "previous_response_id": NotRequired[str],
        "reasoning": NotRequired["ReasoningConfigOutput"],
        "response_format": NotRequired["ResponseFormatOutput"],
        "store": NotRequired[bool],
        "stream": NotRequired[bool],
        "tools": NotRequired[list["ToolOutput"]],
    },
    total=False,
)
ResponsesResponseInput = TypedDict(
    "ResponsesResponseInput",
    {
        "created_at": Required[int],
        "error": NotRequired["ErrorInfoInput"],
        "id": Required[str],
        "model": Required[str],
        "object": Required["ResponsesObjectTypeInput"],
        "output": Required[list["OutputItemInput"]],
        "status": Required["StatusInput"],
        "usage": NotRequired["ResponsesUsageInput"],
    },
    total=False,
)
ResponsesResponseOutput = TypedDict(
    "ResponsesResponseOutput",
    {
        "created_at": Required[int],
        "error": NotRequired["ErrorInfoOutput"],
        "id": Required[str],
        "model": Required[str],
        "object": Required["ResponsesObjectTypeOutput"],
        "output": Required[list["OutputItemOutput"]],
        "status": Required["StatusOutput"],
        "usage": NotRequired["ResponsesUsageOutput"],
    },
    total=False,
)
ResponsesUsageInput = TypedDict(
    "ResponsesUsageInput",
    {
        "cost": NotRequired["ResponsesCostInput"],
        "input_tokens": Required[int],
        "input_tokens_details": NotRequired[dict[str, Any]],
        "output_tokens": Required[int],
        "tool_calls_details": NotRequired[dict[str, Any]],
        "total_tokens": Required[int],
    },
    total=False,
)
ResponsesUsageOutput = TypedDict(
    "ResponsesUsageOutput",
    {
        "cost": NotRequired["ResponsesCostOutput"],
        "input_tokens": Required[int],
        "input_tokens_details": NotRequired[dict[str, Any]],
        "output_tokens": Required[int],
        "tool_calls_details": NotRequired[dict[str, Any]],
        "total_tokens": Required[int],
    },
    total=False,
)
RoleTypeInput: TypeAlias = Literal["assistant"]
RoleTypeOutput: TypeAlias = Literal["assistant"]
SearchContextSizeInput: TypeAlias = Literal["low", "medium", "high"]
SearchContextSizeOutput: TypeAlias = Literal["low", "medium", "high"]
SearchDomainFilterInput = TypedDict(
    "SearchDomainFilterInput",
    {"search_domain_filter": NotRequired[list[str]]},
    total=False,
)
SearchDomainFilterOutput = TypedDict(
    "SearchDomainFilterOutput",
    {"search_domain_filter": NotRequired[list[str]]},
    total=False,
)
SearchPageInput = TypedDict(
    "SearchPageInput",
    {
        "date": NotRequired["DateInput"],
        "last_updated": NotRequired["DateInput"],
        "snippet": Required[str],
        "title": Required[str],
        "url": Required[str],
    },
    total=False,
)
SearchPageOutput = TypedDict(
    "SearchPageOutput",
    {
        "date": NotRequired["DateOutput"],
        "last_updated": NotRequired["DateOutput"],
        "snippet": Required[str],
        "title": Required[str],
        "url": Required[str],
    },
    total=False,
)
SearchQueriesEventInput = TypedDict(
    "SearchQueriesEventInput",
    {
        "queries": Required[list[str]],
        "sequence_number": Required[int],
        "thought": NotRequired[str],
        "type": Required["EventTypeInput"],
    },
    total=False,
)
SearchQueriesEventOutput = TypedDict(
    "SearchQueriesEventOutput",
    {
        "queries": Required[list[str]],
        "sequence_number": Required[int],
        "thought": NotRequired[str],
        "type": Required["EventTypeOutput"],
    },
    total=False,
)
SearchRecencyFilterInput: TypeAlias = Literal["hour", "day", "week", "month", "year"]
SearchRecencyFilterOutput: TypeAlias = Literal["hour", "day", "week", "month", "year"]
SearchRequestInput = TypedDict(
    "SearchRequestInput",
    {
        "country": NotRequired[str],
        "display_server_time": NotRequired[bool],
        "last_updated_after_filter": NotRequired["DateInput"],
        "last_updated_before_filter": NotRequired["DateInput"],
        "max_results": NotRequired["FlexIntInput"],
        "max_tokens": NotRequired["FlexIntInput"],
        "max_tokens_per_page": NotRequired["FlexIntInput"],
        "query": Required["QueryFieldInput"],
        "search_after_date_filter": NotRequired["DateInput"],
        "search_before_date_filter": NotRequired["DateInput"],
        "search_domain_filter": NotRequired[list[str]],
        "search_language_filter": NotRequired[list[str]],
        "search_mode": NotRequired[str],
        "search_recency_filter": NotRequired["SearchRecencyFilterInput"],
        "search_type": NotRequired[Literal["web", "people"]],
    },
    total=False,
)
SearchRequestOutput = TypedDict(
    "SearchRequestOutput",
    {
        "country": NotRequired[str],
        "display_server_time": NotRequired[bool],
        "last_updated_after_filter": NotRequired["DateOutput"],
        "last_updated_before_filter": NotRequired["DateOutput"],
        "max_results": NotRequired["FlexIntOutput"],
        "max_tokens": NotRequired["FlexIntOutput"],
        "max_tokens_per_page": NotRequired["FlexIntOutput"],
        "query": Required["QueryFieldOutput"],
        "search_after_date_filter": NotRequired["DateOutput"],
        "search_before_date_filter": NotRequired["DateOutput"],
        "search_domain_filter": NotRequired[list[str]],
        "search_language_filter": NotRequired[list[str]],
        "search_mode": NotRequired[str],
        "search_recency_filter": NotRequired["SearchRecencyFilterOutput"],
        "search_type": NotRequired[Literal["web", "people"]],
    },
    total=False,
)
SearchResponseInput = TypedDict(
    "SearchResponseInput",
    {
        "id": Required[str],
        "results": Required[list["SearchPageInput"]],
        "server_time": NotRequired[str],
    },
    total=False,
)
SearchResponseOutput = TypedDict(
    "SearchResponseOutput",
    {
        "id": Required[str],
        "results": Required[list["SearchPageOutput"]],
        "server_time": NotRequired[str],
    },
    total=False,
)
SearchResultInput = TypedDict(
    "SearchResultInput",
    {
        "date": NotRequired[str],
        "id": Required[int],
        "last_updated": NotRequired[str],
        "snippet": Required[str],
        "source": NotRequired["SearchSourceInput"],
        "title": Required[str],
        "url": Required[str],
    },
    total=False,
)
SearchResultOutput = TypedDict(
    "SearchResultOutput",
    {
        "date": NotRequired[str],
        "id": Required[int],
        "last_updated": NotRequired[str],
        "snippet": Required[str],
        "source": NotRequired["SearchSourceOutput"],
        "title": Required[str],
        "url": Required[str],
    },
    total=False,
)
SearchResultsEventInput = TypedDict(
    "SearchResultsEventInput",
    {
        "results": Required[list["SearchResultInput"]],
        "sequence_number": Required[int],
        "thought": NotRequired[str],
        "type": Required["EventTypeInput"],
        "usage": NotRequired["ResponsesUsageInput"],
    },
    total=False,
)
SearchResultsEventOutput = TypedDict(
    "SearchResultsEventOutput",
    {
        "results": Required[list["SearchResultOutput"]],
        "sequence_number": Required[int],
        "thought": NotRequired[str],
        "type": Required["EventTypeOutput"],
        "usage": NotRequired["ResponsesUsageOutput"],
    },
    total=False,
)
SearchResultsOutputItemInput = TypedDict(
    "SearchResultsOutputItemInput",
    {
        "queries": NotRequired[list[str]],
        "results": Required[list["SearchResultInput"]],
        "type": Required[Literal["search_results"]],
    },
    total=False,
)
SearchResultsOutputItemOutput = TypedDict(
    "SearchResultsOutputItemOutput",
    {
        "queries": NotRequired[list[str]],
        "results": Required[list["SearchResultOutput"]],
        "type": Required[Literal["search_results"]],
    },
    total=False,
)
SearchSourceInput: TypeAlias = Literal["web"]
SearchSourceOutput: TypeAlias = Literal["web"]
StatusInput: TypeAlias = Literal["completed", "failed", "in_progress"]
StatusOutput: TypeAlias = Literal["completed", "failed", "in_progress"]
StreamEventInput: TypeAlias = Union[
    "TextDeltaChunkInput",
    "CompletionDoneChunkInput",
    "ReasoningChunkInput",
    "ReasoningDoneChunkInput",
]
StreamEventOutput: TypeAlias = Union[
    "TextDeltaChunkOutput",
    "CompletionDoneChunkOutput",
    "ReasoningChunkOutput",
    "ReasoningDoneChunkOutput",
]
TextDeltaInput = TypedDict(
    "TextDeltaInput",
    {"content": NotRequired[str], "role": NotRequired[str]},
    total=False,
)
TextDeltaOutput = TypedDict(
    "TextDeltaOutput",
    {"content": NotRequired[str], "role": NotRequired[str]},
    total=False,
)
TextDeltaChoiceInput = TypedDict(
    "TextDeltaChoiceInput",
    {
        "delta": Required["TextDeltaInput"],
        "finish_reason": Required[Optional[str]],
        "index": Required[int],
        "logprobs": Required[Optional[Any]],
    },
    total=False,
)
TextDeltaChoiceOutput = TypedDict(
    "TextDeltaChoiceOutput",
    {
        "delta": Required["TextDeltaOutput"],
        "finish_reason": Required[Optional[str]],
        "index": Required[int],
        "logprobs": Required[Optional[Any]],
    },
    total=False,
)
TextDeltaChunkInput = TypedDict(
    "TextDeltaChunkInput",
    {
        "choices": Required[list["TextDeltaChoiceInput"]],
        "created": Required[int],
        "id": Required[str],
        "images": NotRequired[list["ImageResultInput"]],
        "model": Required[str],
        "object": Required["ObjectTypeInput"],
        "search_results": NotRequired[list["SearchResultInput"]],
        "usage": NotRequired["UsageInput"],
    },
    total=False,
)
TextDeltaChunkOutput = TypedDict(
    "TextDeltaChunkOutput",
    {
        "choices": Required[list["TextDeltaChoiceOutput"]],
        "created": Required[int],
        "id": Required[str],
        "images": NotRequired[list["ImageResultOutput"]],
        "model": Required[str],
        "object": Required["ObjectTypeOutput"],
        "search_results": NotRequired[list["SearchResultOutput"]],
        "usage": NotRequired["UsageOutput"],
    },
    total=False,
)
TextDeltaEventInput = TypedDict(
    "TextDeltaEventInput",
    {
        "content_index": Required[int],
        "delta": Required[str],
        "item_id": Required[str],
        "output_index": Required[int],
        "sequence_number": Required[int],
        "type": Required["EventTypeInput"],
    },
    total=False,
)
TextDeltaEventOutput = TypedDict(
    "TextDeltaEventOutput",
    {
        "content_index": Required[int],
        "delta": Required[str],
        "item_id": Required[str],
        "output_index": Required[int],
        "sequence_number": Required[int],
        "type": Required["EventTypeOutput"],
    },
    total=False,
)
TextDoneEventInput = TypedDict(
    "TextDoneEventInput",
    {
        "content_index": Required[int],
        "item_id": Required[str],
        "output_index": Required[int],
        "sequence_number": Required[int],
        "text": Required[str],
        "type": Required["EventTypeInput"],
    },
    total=False,
)
TextDoneEventOutput = TypedDict(
    "TextDoneEventOutput",
    {
        "content_index": Required[int],
        "item_id": Required[str],
        "output_index": Required[int],
        "sequence_number": Required[int],
        "text": Required[str],
        "type": Required["EventTypeOutput"],
    },
    total=False,
)
ToolInput: TypeAlias = Union["WebSearchToolInput", "FetchUrlToolInput", "McpToolInput"]
ToolOutput: TypeAlias = Union[
    "WebSearchToolOutput", "FetchUrlToolOutput", "McpToolOutput"
]
ToolCallDetailsInput = TypedDict(
    "ToolCallDetailsInput",
    {
        "cost_usd": NotRequired[float],
        "duration_ms": NotRequired[int],
        "invocation": NotRequired[int],
        "token_usage": NotRequired[list["ToolCallTokenUsageInput"]],
    },
    total=False,
)
ToolCallDetailsOutput = TypedDict(
    "ToolCallDetailsOutput",
    {
        "cost_usd": NotRequired[float],
        "duration_ms": NotRequired[int],
        "invocation": NotRequired[int],
        "token_usage": NotRequired[list["ToolCallTokenUsageOutput"]],
    },
    total=False,
)
ToolCallTokenUsageInput = TypedDict(
    "ToolCallTokenUsageInput",
    {
        "input_tokens": Required[int],
        "input_tokens_details": Required[dict[str, Any]],
        "model": NotRequired[str],
        "output_tokens": Required[int],
        "output_tokens_details": Required[dict[str, Any]],
    },
    total=False,
)
ToolCallTokenUsageOutput = TypedDict(
    "ToolCallTokenUsageOutput",
    {
        "input_tokens": Required[int],
        "input_tokens_details": Required[dict[str, Any]],
        "model": NotRequired[str],
        "output_tokens": Required[int],
        "output_tokens_details": Required[dict[str, Any]],
    },
    total=False,
)
UrlContentInput = TypedDict(
    "UrlContentInput",
    {"snippet": Required[str], "title": Required[str], "url": Required[str]},
    total=False,
)
UrlContentOutput = TypedDict(
    "UrlContentOutput",
    {"snippet": Required[str], "title": Required[str], "url": Required[str]},
    total=False,
)
UsageInput = TypedDict(
    "UsageInput",
    {
        "completion_tokens": Required[int],
        "completion_tokens_details": NotRequired["CompletionTokensDetailsInput"],
        "cost": NotRequired["CostInput"],
        "prompt_tokens": Required[int],
        "search_context_size": NotRequired["SearchContextSizeInput"],
        "total_tokens": Required[int],
    },
    total=False,
)
UsageOutput = TypedDict(
    "UsageOutput",
    {
        "completion_tokens": Required[int],
        "completion_tokens_details": NotRequired["CompletionTokensDetailsOutput"],
        "cost": NotRequired["CostOutput"],
        "prompt_tokens": Required[int],
        "search_context_size": NotRequired["SearchContextSizeOutput"],
        "total_tokens": Required[int],
    },
    total=False,
)
UserLocationInput = TypedDict(
    "UserLocationInput",
    {
        "city": NotRequired[str],
        "country": NotRequired[str],
        "latitude": NotRequired[float],
        "longitude": NotRequired[float],
        "region": NotRequired[str],
    },
    total=False,
)
UserLocationOutput = TypedDict(
    "UserLocationOutput",
    {
        "city": NotRequired[str],
        "country": NotRequired[str],
        "latitude": NotRequired[float],
        "longitude": NotRequired[float],
        "region": NotRequired[str],
    },
    total=False,
)
WebSearchDataInput = TypedDict(
    "WebSearchDataInput",
    {
        "search_keywords": NotRequired[list[str]],
        "search_results": NotRequired[list["SearchResultInput"]],
    },
    total=False,
)
WebSearchDataOutput = TypedDict(
    "WebSearchDataOutput",
    {
        "search_keywords": NotRequired[list[str]],
        "search_results": NotRequired[list["SearchResultOutput"]],
    },
    total=False,
)
WebSearchFiltersInput = TypedDict(
    "WebSearchFiltersInput",
    {
        "last_updated_after_filter": NotRequired["DateInput"],
        "last_updated_before_filter": NotRequired["DateInput"],
        "search_after_date_filter": NotRequired["DateInput"],
        "search_before_date_filter": NotRequired["DateInput"],
        "search_domain_filter": NotRequired[list[str]],
        "search_recency_filter": NotRequired["SearchRecencyFilterInput"],
    },
    total=False,
)
WebSearchFiltersOutput = TypedDict(
    "WebSearchFiltersOutput",
    {
        "last_updated_after_filter": NotRequired["DateOutput"],
        "last_updated_before_filter": NotRequired["DateOutput"],
        "search_after_date_filter": NotRequired["DateOutput"],
        "search_before_date_filter": NotRequired["DateOutput"],
        "search_domain_filter": NotRequired[list[str]],
        "search_recency_filter": NotRequired["SearchRecencyFilterOutput"],
    },
    total=False,
)
WebSearchOptionsInput = TypedDict(
    "WebSearchOptionsInput",
    {
        "last_updated_after_filter": NotRequired["DateInput"],
        "last_updated_before_filter": NotRequired["DateInput"],
        "search_after_date_filter": NotRequired["DateInput"],
        "search_before_date_filter": NotRequired["DateInput"],
        "search_context_size": NotRequired["SearchContextSizeInput"],
        "search_domain_filter": NotRequired[list[str]],
        "search_recency_filter": NotRequired["SearchRecencyFilterInput"],
        "search_type": NotRequired[Literal["fast", "pro", "auto"]],
        "user_location": NotRequired["UserLocationInput"],
    },
    total=False,
)
WebSearchOptionsOutput = TypedDict(
    "WebSearchOptionsOutput",
    {
        "last_updated_after_filter": NotRequired["DateOutput"],
        "last_updated_before_filter": NotRequired["DateOutput"],
        "search_after_date_filter": NotRequired["DateOutput"],
        "search_before_date_filter": NotRequired["DateOutput"],
        "search_context_size": NotRequired["SearchContextSizeOutput"],
        "search_domain_filter": NotRequired[list[str]],
        "search_recency_filter": NotRequired["SearchRecencyFilterOutput"],
        "search_type": NotRequired[Literal["fast", "pro", "auto"]],
        "user_location": NotRequired["UserLocationOutput"],
    },
    total=False,
)
WebSearchToolInput = TypedDict(
    "WebSearchToolInput",
    {
        "filters": NotRequired["WebSearchFiltersInput"],
        "max_tokens": NotRequired[int],
        "max_tokens_per_page": NotRequired[int],
        "type": Required[Literal["web_search"]],
        "user_location": NotRequired["UserLocationInput"],
    },
    total=False,
)
WebSearchToolOutput = TypedDict(
    "WebSearchToolOutput",
    {
        "filters": NotRequired["WebSearchFiltersOutput"],
        "max_tokens": NotRequired[int],
        "max_tokens_per_page": NotRequired[int],
        "type": Required[Literal["web_search"]],
        "user_location": NotRequired["UserLocationOutput"],
    },
    total=False,
)


class PerplexitySdk(Protocol):
    def cancel_response(self, id: str) -> dict[str, Any]: ...
    def chat_completions(
        self, body: "RequestInput"
    ) -> Union["ResponseOutput", AsyncIterable["StreamEventOutput"]]: ...
    def create_response(
        self, body: "ResponsesRequestInput"
    ) -> Union[
        "ResponsesResponseOutput", AsyncIterable["ResponseStreamEventOutput"]
    ]: ...
    def search(self, body: "SearchRequestInput") -> "SearchResponseOutput": ...
class AsyncPerplexitySdk(Protocol):
    async def cancel_response(self, id: str) -> dict[str, Any]: ...
    async def chat_completions(
        self, body: "RequestInput"
    ) -> Union["ResponseOutput", AsyncIterable["StreamEventOutput"]]: ...
    async def create_response(
        self, body: "ResponsesRequestInput"
    ) -> Union[
        "ResponsesResponseOutput", AsyncIterable["ResponseStreamEventOutput"]
    ]: ...
    async def search(self, body: "SearchRequestInput") -> "SearchResponseOutput": ...
