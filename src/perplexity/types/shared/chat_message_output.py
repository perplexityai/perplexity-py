# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .api_public_search_result import APIPublicSearchResult

__all__ = [
    "ChatMessageOutput",
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


class ContentStructuredContentChatMessageContentTextChunk(BaseModel):
    text: str

    type: Literal["text"]


class ContentStructuredContentChatMessageContentImageChunkImageURLURL(BaseModel):
    url: str


ContentStructuredContentChatMessageContentImageChunkImageURL: TypeAlias = Union[
    ContentStructuredContentChatMessageContentImageChunkImageURLURL, str
]


class ContentStructuredContentChatMessageContentImageChunk(BaseModel):
    image_url: ContentStructuredContentChatMessageContentImageChunkImageURL

    type: Literal["image_url"]


class ContentStructuredContentChatMessageContentFileChunkFileURLURL(BaseModel):
    url: str


ContentStructuredContentChatMessageContentFileChunkFileURL: TypeAlias = Union[
    ContentStructuredContentChatMessageContentFileChunkFileURLURL, str
]


class ContentStructuredContentChatMessageContentFileChunk(BaseModel):
    file_url: ContentStructuredContentChatMessageContentFileChunkFileURL

    type: Literal["file_url"]

    file_name: Optional[str] = None


class ContentStructuredContentChatMessageContentPdfChunkPdfURLURL(BaseModel):
    url: str


ContentStructuredContentChatMessageContentPdfChunkPdfURL: TypeAlias = Union[
    ContentStructuredContentChatMessageContentPdfChunkPdfURLURL, str
]


class ContentStructuredContentChatMessageContentPdfChunk(BaseModel):
    pdf_url: ContentStructuredContentChatMessageContentPdfChunkPdfURL

    type: Literal["pdf_url"]


class ContentStructuredContentChatMessageContentVideoChunkVideoURLVideoURL(BaseModel):
    url: str

    frame_interval: Union[str, int, None] = None


ContentStructuredContentChatMessageContentVideoChunkVideoURL: TypeAlias = Union[
    ContentStructuredContentChatMessageContentVideoChunkVideoURLVideoURL, str
]


class ContentStructuredContentChatMessageContentVideoChunk(BaseModel):
    type: Literal["video_url"]

    video_url: ContentStructuredContentChatMessageContentVideoChunkVideoURL


ContentStructuredContent: TypeAlias = Union[
    ContentStructuredContentChatMessageContentTextChunk,
    ContentStructuredContentChatMessageContentImageChunk,
    ContentStructuredContentChatMessageContentFileChunk,
    ContentStructuredContentChatMessageContentPdfChunk,
    ContentStructuredContentChatMessageContentVideoChunk,
]


class ReasoningStepAgentProgress(BaseModel):
    action: Optional[str] = None

    screenshot: Optional[str] = None

    url: Optional[str] = None


class ReasoningStepBrowserAgent(BaseModel):
    result: str

    url: str


class ReasoningStepBrowserToolExecution(BaseModel):
    tool: Dict[str, object]


class ReasoningStepExecutePython(BaseModel):
    code: str

    result: str


class ReasoningStepFetchURLContent(BaseModel):
    contents: List[APIPublicSearchResult]


class ReasoningStepFileAttachmentSearch(BaseModel):
    attachment_urls: List[str]


class ReasoningStepWebSearch(BaseModel):
    search_keywords: List[str]

    search_results: List[APIPublicSearchResult]


class ReasoningStep(BaseModel):
    thought: str

    type: Literal[
        "web_search",
        "fetch_url_content",
        "execute_python",
        "agent_progress",
        "browser_agent",
        "browser_tool_execution",
        "file_attachment_search",
    ]

    agent_progress: Optional[ReasoningStepAgentProgress] = None
    """Agent progress class for live-browsing updates"""

    browser_agent: Optional[ReasoningStepBrowserAgent] = None
    """Browser agent step summary class"""

    browser_tool_execution: Optional[ReasoningStepBrowserToolExecution] = None
    """Tool input for kicking off browser tool automation"""

    execute_python: Optional[ReasoningStepExecutePython] = None
    """Code generation step details wrapper class"""

    fetch_url_content: Optional[ReasoningStepFetchURLContent] = None
    """Fetch url content step details wrapper class"""

    file_attachment_search: Optional[ReasoningStepFileAttachmentSearch] = None
    """File attachment search step details wrapper class"""

    web_search: Optional[ReasoningStepWebSearch] = None
    """Web search step details wrapper class"""


class ToolCallFunction(BaseModel):
    arguments: Optional[str] = None

    name: Optional[str] = None


class ToolCall(BaseModel):
    id: Optional[str] = None

    function: Optional[ToolCallFunction] = None

    type: Optional[Literal["function"]] = None


class ChatMessageOutput(BaseModel):
    content: Union[str, List[ContentStructuredContent]]

    role: Literal["system", "user", "assistant", "tool"]
    """Chat roles enum"""

    reasoning_steps: Optional[List[ReasoningStep]] = None

    tool_calls: Optional[List[ToolCall]] = None
