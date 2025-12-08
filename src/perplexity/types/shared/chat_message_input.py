# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
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


class ReasoningStepExecutePython(BaseModel):
    """Code generation step details wrapper class"""

    code: str

    result: str


class ReasoningStepFetchURLContent(BaseModel):
    """Fetch url content step details wrapper class"""

    contents: List[APIPublicSearchResult]


class ReasoningStepWebSearch(BaseModel):
    """Web search step details wrapper class"""

    search_keywords: List[str]

    search_results: List[APIPublicSearchResult]


class ReasoningStep(BaseModel):
    """Reasoning step wrapper class"""

    thought: str

    execute_python: Optional[ReasoningStepExecutePython] = None
    """Code generation step details wrapper class"""

    fetch_url_content: Optional[ReasoningStepFetchURLContent] = None
    """Fetch url content step details wrapper class"""

    type: Optional[str] = None

    web_search: Optional[ReasoningStepWebSearch] = None
    """Web search step details wrapper class"""


class ToolCallFunction(BaseModel):
    arguments: Optional[str] = None

    name: Optional[str] = None


class ToolCall(BaseModel):
    id: Optional[str] = None

    function: Optional[ToolCallFunction] = None

    type: Optional[Literal["function"]] = None


class ChatMessageInput(BaseModel):
    content: Union[str, List[ContentStructuredContent], None] = None

    role: Literal["system", "user", "assistant", "tool"]
    """Chat roles enum"""

    reasoning_steps: Optional[List[ReasoningStep]] = None

    tool_call_id: Optional[str] = None

    tool_calls: Optional[List[ToolCall]] = None
