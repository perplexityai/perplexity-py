# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
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
    "ReasoningStepAgentProgress",
    "ReasoningStepBrowserAgent",
    "ReasoningStepBrowserToolExecution",
    "ReasoningStepExecutePython",
    "ReasoningStepFetchURLContent",
    "ReasoningStepFileAttachmentSearch",
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


class ReasoningStepAgentProgress(TypedDict, total=False):
    action: Required[Optional[str]]

    screenshot: Required[Optional[str]]

    url: Required[Optional[str]]


class ReasoningStepBrowserAgent(TypedDict, total=False):
    result: Required[str]

    url: Required[str]


class ReasoningStepBrowserToolExecution(TypedDict, total=False):
    tool: Required[Dict[str, object]]


class ReasoningStepExecutePython(TypedDict, total=False):
    code: Required[str]

    result: Required[str]


class ReasoningStepFetchURLContent(TypedDict, total=False):
    contents: Required[Iterable[APIPublicSearchResult]]


class ReasoningStepFileAttachmentSearch(TypedDict, total=False):
    attachment_urls: Required[SequenceNotStr[str]]


class ReasoningStepWebSearch(TypedDict, total=False):
    search_keywords: Required[SequenceNotStr[str]]

    search_results: Required[Iterable[APIPublicSearchResult]]


class ReasoningStep(TypedDict, total=False):
    thought: Required[str]

    type: Required[
        Literal[
            "web_search",
            "fetch_url_content",
            "execute_python",
            "agent_progress",
            "browser_agent",
            "browser_tool_execution",
            "file_attachment_search",
        ]
    ]

    agent_progress: Optional[ReasoningStepAgentProgress]
    """Agent progress class for live-browsing updates"""

    browser_agent: Optional[ReasoningStepBrowserAgent]
    """Browser agent step summary class"""

    browser_tool_execution: Optional[ReasoningStepBrowserToolExecution]
    """Tool input for kicking off browser tool automation"""

    execute_python: Optional[ReasoningStepExecutePython]
    """Code generation step details wrapper class"""

    fetch_url_content: Optional[ReasoningStepFetchURLContent]
    """Fetch url content step details wrapper class"""

    file_attachment_search: Optional[ReasoningStepFileAttachmentSearch]
    """File attachment search step details wrapper class"""

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
    content: Required[Union[str, Iterable[ContentStructuredContent]]]

    role: Required[Literal["system", "user", "assistant", "tool"]]
    """Chat roles enum"""

    reasoning_steps: Optional[Iterable[ReasoningStep]]

    tool_calls: Optional[Iterable[ToolCall]]
