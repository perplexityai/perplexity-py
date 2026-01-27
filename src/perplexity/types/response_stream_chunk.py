# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .error_info import ErrorInfo
from .output_item import OutputItem
from .responses_usage import ResponsesUsage
from .shared.search_result import SearchResult

__all__ = [
    "ResponseStreamChunk",
    "ResponseCreatedEvent",
    "ResponseCreatedEventResponse",
    "ResponseInProgressEvent",
    "ResponseInProgressEventResponse",
    "ResponseCompletedEvent",
    "ResponseCompletedEventResponse",
    "ResponseFailedEvent",
    "OutputItemAddedEvent",
    "OutputItemDoneEvent",
    "TextDeltaEvent",
    "TextDoneEvent",
    "ReasoningStartedEvent",
    "SearchQueriesEvent",
    "SearchResultsEvent",
    "FetchURLQueriesEvent",
    "FetchURLResultsEvent",
    "FetchURLResultsEventContent",
    "ReasoningStoppedEvent",
]


class ResponseCreatedEventResponse(BaseModel):
    """Non-streaming response returned when stream is false"""

    id: str

    created_at: int

    model: str

    object: Literal["response"]
    """Object type in API responses"""

    output: List[OutputItem]

    status: Literal["completed", "failed", "in_progress", "requires_action"]
    """Status of a response or output item"""

    error: Optional[ErrorInfo] = None

    usage: Optional[ResponsesUsage] = None


class ResponseCreatedEvent(BaseModel):
    """
    Response created event (type: "response.created").
    Contains the initial response object.
    """

    sequence_number: int
    """Monotonically increasing sequence number for event ordering"""

    type: Literal[
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
    """SSE event type discriminator"""

    response: Optional[ResponseCreatedEventResponse] = None
    """Non-streaming response returned when stream is false"""


class ResponseInProgressEventResponse(BaseModel):
    """Non-streaming response returned when stream is false"""

    id: str

    created_at: int

    model: str

    object: Literal["response"]
    """Object type in API responses"""

    output: List[OutputItem]

    status: Literal["completed", "failed", "in_progress", "requires_action"]
    """Status of a response or output item"""

    error: Optional[ErrorInfo] = None

    usage: Optional[ResponsesUsage] = None


class ResponseInProgressEvent(BaseModel):
    """
    Response in progress event (type: "response.in_progress").
    Emitted when response processing has started.
    """

    sequence_number: int
    """Monotonically increasing sequence number for event ordering"""

    type: Literal[
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
    """SSE event type discriminator"""

    response: Optional[ResponseInProgressEventResponse] = None
    """Non-streaming response returned when stream is false"""


class ResponseCompletedEventResponse(BaseModel):
    """Non-streaming response returned when stream is false"""

    id: str

    created_at: int

    model: str

    object: Literal["response"]
    """Object type in API responses"""

    output: List[OutputItem]

    status: Literal["completed", "failed", "in_progress", "requires_action"]
    """Status of a response or output item"""

    error: Optional[ErrorInfo] = None

    usage: Optional[ResponsesUsage] = None


class ResponseCompletedEvent(BaseModel):
    """
    Response event
    Contains the full or partial response object.
    """

    sequence_number: int
    """Monotonically increasing sequence number for event ordering"""

    type: Literal[
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
    """SSE event type discriminator"""

    response: Optional[ResponseCompletedEventResponse] = None
    """Non-streaming response returned when stream is false"""


class ResponseFailedEvent(BaseModel):
    """
    Response failed event (type: "response.failed").
    Contains error details when streaming fails.
    """

    error: ErrorInfo

    sequence_number: int
    """Monotonically increasing sequence number for event ordering"""

    type: Literal[
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
    """SSE event type discriminator"""


class OutputItemAddedEvent(BaseModel):
    """
    Output item added event (type: "response.output_item.added").
    Emitted when a new output item (message or tool call) starts.
    """

    item: OutputItem

    output_index: int

    sequence_number: int
    """Monotonically increasing sequence number for event ordering"""

    type: Literal[
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
    """SSE event type discriminator"""


class OutputItemDoneEvent(BaseModel):
    """
    Output item done event (type: "response.output_item.done").
    Emitted when an output item (message or tool call) completes.
    """

    item: OutputItem

    output_index: int

    sequence_number: int
    """Monotonically increasing sequence number for event ordering"""

    type: Literal[
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
    """SSE event type discriminator"""


class TextDeltaEvent(BaseModel):
    """
    Text delta event (type: "response.output_text.delta").
    Contains incremental text content.
    """

    content_index: int

    delta: str

    item_id: str

    output_index: int

    sequence_number: int
    """Monotonically increasing sequence number for event ordering"""

    type: Literal[
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
    """SSE event type discriminator"""


class TextDoneEvent(BaseModel):
    """
    Text done event (type: "response.output_text.done").
    Contains the final text content.
    """

    content_index: int

    item_id: str

    output_index: int

    sequence_number: int
    """Monotonically increasing sequence number for event ordering"""

    text: str

    type: Literal[
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
    """SSE event type discriminator"""


class ReasoningStartedEvent(BaseModel):
    """
    Reasoning started event (type: "response.reasoning.started").
    Signals the model has started reasoning/searching.
    """

    sequence_number: int
    """Monotonically increasing sequence number for event ordering"""

    type: Literal[
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
    """SSE event type discriminator"""

    thought: Optional[str] = None


class SearchQueriesEvent(BaseModel):
    """
    Search queries event (type: "response.reasoning.search_queries").
    Contains search queries being executed.
    """

    queries: List[str]

    sequence_number: int
    """Monotonically increasing sequence number for event ordering"""

    type: Literal[
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
    """SSE event type discriminator"""

    thought: Optional[str] = None


class SearchResultsEvent(BaseModel):
    """
    Search results event (type: "response.reasoning.search_results").
    Contains search results returned.
    """

    results: List[SearchResult]

    sequence_number: int
    """Monotonically increasing sequence number for event ordering"""

    type: Literal[
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
    """SSE event type discriminator"""

    thought: Optional[str] = None

    usage: Optional[ResponsesUsage] = None


class FetchURLQueriesEvent(BaseModel):
    """
    URL fetch queries event (type: "response.reasoning.fetch_url_queries").
    Contains URLs being fetched.
    """

    sequence_number: int
    """Monotonically increasing sequence number for event ordering"""

    type: Literal[
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
    """SSE event type discriminator"""

    urls: List[str]

    thought: Optional[str] = None


class FetchURLResultsEventContent(BaseModel):
    """Content fetched from a URL"""

    snippet: str
    """The fetched content snippet"""

    title: str
    """The title of the page"""

    url: str
    """The URL from which content was fetched"""


class FetchURLResultsEvent(BaseModel):
    """
    URL fetch results event (type: "response.reasoning.fetch_url_results").
    Contains fetched URL contents.
    """

    contents: List[FetchURLResultsEventContent]

    sequence_number: int
    """Monotonically increasing sequence number for event ordering"""

    type: Literal[
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
    """SSE event type discriminator"""

    thought: Optional[str] = None


class ReasoningStoppedEvent(BaseModel):
    """
    Reasoning stopped event (type: "response.reasoning.stopped").
    Signals the model has finished reasoning/searching.
    """

    sequence_number: int
    """Monotonically increasing sequence number for event ordering"""

    type: Literal[
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
    """SSE event type discriminator"""

    thought: Optional[str] = None


ResponseStreamChunk: TypeAlias = Union[
    ResponseCreatedEvent,
    ResponseInProgressEvent,
    ResponseCompletedEvent,
    ResponseFailedEvent,
    OutputItemAddedEvent,
    OutputItemDoneEvent,
    TextDeltaEvent,
    TextDoneEvent,
    ReasoningStartedEvent,
    SearchQueriesEvent,
    SearchResultsEvent,
    FetchURLQueriesEvent,
    FetchURLResultsEvent,
    ReasoningStoppedEvent,
]
