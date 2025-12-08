# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from .api_public_search_result import APIPublicSearchResult

__all__ = [
    "ChatMessageInput",
    "ContentStructuredContent",
    "ContentStructuredContentChatMessageContentTextChunk",
    "ContentStructuredContentChatMessageContentImageChunk",
    "ContentStructuredContentChatMessageContentImageChunkImageURL",
    "ContentStructuredContentChatMessageContentImageChunkImageURLURL",
    "ContentStructuredContentChatMessageContentFileChunk",
    "ContentStructuredContentChatMessageContentFileChunkFileURL",
    "ContentStructuredContentChatMessageContentFileChunkFileURLURL",
    "ContentStructuredContentChatMessageContentPdfChunk",
    "ContentStructuredContentChatMessageContentPdfChunkPdfURL",
    "ContentStructuredContentChatMessageContentPdfChunkPdfURLURL",
    "ContentStructuredContentChatMessageContentVideoChunk",
    "ContentStructuredContentChatMessageContentVideoChunkVideoURL",
    "ContentStructuredContentChatMessageContentVideoChunkVideoURLVideoURL",
    "ReasoningStep",
    "ReasoningStepExecutePython",
    "ReasoningStepFetchURLContent",
    "ReasoningStepWebSearch",
    "ToolCall",
    "ToolCallFunction",
]


class ContentStructuredContentChatMessageContentTextChunk(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class ContentStructuredContentChatMessageContentImageChunkImageURLURL(TypedDict, total=False):
    url: Required[str]


ContentStructuredContentChatMessageContentImageChunkImageURL: TypeAlias = Union[
    ContentStructuredContentChatMessageContentImageChunkImageURLURL, str
]


class ContentStructuredContentChatMessageContentImageChunk(TypedDict, total=False):
    image_url: Required[ContentStructuredContentChatMessageContentImageChunkImageURL]

    type: Required[Literal["image_url"]]


class ContentStructuredContentChatMessageContentFileChunkFileURLURL(TypedDict, total=False):
    url: Required[str]


ContentStructuredContentChatMessageContentFileChunkFileURL: TypeAlias = Union[
    ContentStructuredContentChatMessageContentFileChunkFileURLURL, str
]


class ContentStructuredContentChatMessageContentFileChunk(TypedDict, total=False):
    file_url: Required[ContentStructuredContentChatMessageContentFileChunkFileURL]

    type: Required[Literal["file_url"]]

    file_name: Optional[str]


class ContentStructuredContentChatMessageContentPdfChunkPdfURLURL(TypedDict, total=False):
    url: Required[str]


ContentStructuredContentChatMessageContentPdfChunkPdfURL: TypeAlias = Union[
    ContentStructuredContentChatMessageContentPdfChunkPdfURLURL, str
]


class ContentStructuredContentChatMessageContentPdfChunk(TypedDict, total=False):
    pdf_url: Required[ContentStructuredContentChatMessageContentPdfChunkPdfURL]

    type: Required[Literal["pdf_url"]]


class ContentStructuredContentChatMessageContentVideoChunkVideoURLVideoURL(TypedDict, total=False):
    url: Required[str]

    frame_interval: Union[str, int]


ContentStructuredContentChatMessageContentVideoChunkVideoURL: TypeAlias = Union[
    ContentStructuredContentChatMessageContentVideoChunkVideoURLVideoURL, str
]


class ContentStructuredContentChatMessageContentVideoChunk(TypedDict, total=False):
    type: Required[Literal["video_url"]]

    video_url: Required[ContentStructuredContentChatMessageContentVideoChunkVideoURL]


ContentStructuredContent: TypeAlias = Union[
    ContentStructuredContentChatMessageContentTextChunk,
    ContentStructuredContentChatMessageContentImageChunk,
    ContentStructuredContentChatMessageContentFileChunk,
    ContentStructuredContentChatMessageContentPdfChunk,
    ContentStructuredContentChatMessageContentVideoChunk,
]


class ReasoningStepExecutePython(TypedDict, total=False):
    """Code generation step details wrapper class"""

    code: Required[str]

    result: Required[str]


class ReasoningStepFetchURLContent(TypedDict, total=False):
    """Fetch url content step details wrapper class"""

    contents: Required[Iterable[APIPublicSearchResult]]


class ReasoningStepWebSearch(TypedDict, total=False):
    """Web search step details wrapper class"""

    search_keywords: Required[SequenceNotStr[str]]

    search_results: Required[Iterable[APIPublicSearchResult]]


class ReasoningStep(TypedDict, total=False):
    """Reasoning step wrapper class"""

    thought: Required[str]

    execute_python: Optional[ReasoningStepExecutePython]
    """Code generation step details wrapper class"""

    fetch_url_content: Optional[ReasoningStepFetchURLContent]
    """Fetch url content step details wrapper class"""

    type: Optional[str]

    web_search: Optional[ReasoningStepWebSearch]
    """Web search step details wrapper class"""


class ToolCallFunction(TypedDict, total=False):
    arguments: Optional[str]

    name: Optional[str]


class ToolCall(TypedDict, total=False):
    id: Optional[str]

    function: Optional[ToolCallFunction]

    type: Optional[Literal["function"]]


class ChatMessageInput(TypedDict, total=False):
    content: Required[Union[str, Iterable[ContentStructuredContent], None]]

    role: Required[Literal["system", "user", "assistant", "tool"]]
    """Chat roles enum"""

    reasoning_steps: Optional[Iterable[ReasoningStep]]

    tool_call_id: Optional[str]

    tool_calls: Optional[Iterable[ToolCall]]
