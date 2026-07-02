# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .content_part import ContentPart
from .shared.search_result import SearchResult
from .function_call_output_item import FunctionCallOutputItem

__all__ = [
    "OutputItem",
    "MessageOutputItem",
    "SearchResultsOutputItem",
    "FetchURLResultsOutputItem",
    "FetchURLResultsOutputItemContent",
    "McpListToolsOutputItem",
    "McpListToolsOutputItemTool",
    "McpCallOutputItem",
]


class MessageOutputItem(BaseModel):
    id: str

    content: List[ContentPart]

    role: Literal["assistant"]
    """Role in a message"""

    status: Literal["completed", "failed", "in_progress", "queued", "cancelled", "requires_action"]
    """Status of a response or output item"""

    type: Literal["message"]


class SearchResultsOutputItem(BaseModel):
    results: List[SearchResult]

    type: Literal["search_results"]

    queries: Optional[List[str]] = None


class FetchURLResultsOutputItemContent(BaseModel):
    """Content fetched from a URL"""

    snippet: str
    """The fetched content snippet"""

    title: str
    """The title of the page"""

    url: str
    """The URL from which content was fetched"""


class FetchURLResultsOutputItem(BaseModel):
    contents: List[FetchURLResultsOutputItemContent]

    type: Literal["fetch_url_results"]


class McpListToolsOutputItemTool(BaseModel):
    """One tool discovered on a remote MCP server."""

    input_schema: Dict[str, object]
    """The server's JSON Schema for the tool, passed through unmodified."""

    name: str

    description: Optional[str] = None


class McpListToolsOutputItem(BaseModel):
    """Tools discovered on one external MCP server at boot.

    Matches OpenAI's mcp_list_tools item.
    """

    id: str

    server_label: str

    tools: List[McpListToolsOutputItemTool]

    type: Literal["mcp_list_tools"]

    error: Optional[str] = None


class McpCallOutputItem(BaseModel):
    """
    One tool call executed against an external MCP server, modeled on OpenAI's mcp_call item.
    """

    id: str

    arguments: str
    """JSON-encoded arguments the model passed."""

    name: str

    server_label: str

    type: Literal["mcp_call"]

    error: Optional[str] = None
    """
    The failure string when the call failed (also returned to the model in-band);
    null on success, matching OpenAI's mcp_call.
    """

    output: Optional[str] = None
    """Tool output text; empty when the call failed."""


OutputItem: TypeAlias = Annotated[
    Union[
        MessageOutputItem,
        SearchResultsOutputItem,
        FetchURLResultsOutputItem,
        FunctionCallOutputItem,
        McpListToolsOutputItem,
        McpCallOutputItem,
    ],
    PropertyInfo(discriminator="type"),
]
