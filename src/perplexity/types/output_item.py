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
    "SkillLoadedOutputItem",
    "AdvisorResultOutputItem",
    "SandboxResultsOutputItem",
    "SandboxResultsOutputItemResult",
    "SandboxWriteFileOutputItem",
    "SandboxReadFileOutputItem",
    "SandboxEditFileOutputItem",
    "SandboxGrepOutputItem",
    "SandboxGlobOutputItem",
    "SandboxApplyPatchOutputItem",
    "ShareFileOutputItem",
    "UnknownOutputItem",
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


class SkillLoadedOutputItem(BaseModel):
    """Per-call result emitted by the `load_skill` tool.

    Only the resolved skill name is surfaced here; the skill body itself lives in the function_call_output input item the model consumes on its next turn.
    """

    name: str
    """Name of the skill that was loaded."""

    type: Literal["skill_loaded"]


class AdvisorResultOutputItem(BaseModel):
    """Preview API.

    Advisor tool invocation emitted in `response.output[]`.
    The advisor result is server-side guidance consumed by the agent loop;
    it is not a client-executable function call.
    """

    call_id: str

    status: Literal["completed", "failed", "in_progress", "queued", "cancelled", "requires_action"]
    """Status of a response or output item"""

    type: Literal["advisor_result"]

    advice: Optional[str] = None
    """Guidance returned by the advisor model."""

    arguments: Optional[str] = None
    """Raw JSON arguments the executor passed to the advisor tool."""

    error_code: Optional[str] = None
    """Non-fatal advisor error code when the advisor call failed."""

    error_message: Optional[str] = None
    """Non-fatal advisor error message when the advisor call failed."""

    question: Optional[str] = None
    """Parsed advisor question when present in arguments."""


class SandboxResultsOutputItemResult(BaseModel):
    """One sandbox execution result.

    `status` describes whether the sandbox
    runner completed, failed, or timed out. `exit_code` is the program exit
    code, so `status: completed` can still have a non-zero `exit_code`.
    """

    duration_ms: int

    exit_code: int

    status: Literal["in_progress", "completed", "failed", "timed_out"]

    stderr: str

    stdout: str


class SandboxResultsOutputItem(BaseModel):
    """Sandbox tool results emitted in `response.output[]`.

    Cost is aggregated
    into `Usage.tool_calls_details.sandbox.cost_usd`; this item does not
    carry per-execution cost.
    """

    call_id: str

    code: str

    language: Literal["python", "bash"]

    results: List[SandboxResultsOutputItemResult]

    status: Literal["in_progress", "completed", "failed", "timed_out"]

    type: Literal["sandbox_results"]

    container_id: Optional[str] = None


class SandboxWriteFileOutputItem(BaseModel):
    """Per-invocation result of the `write` tool inside the sandbox."""

    call_id: str

    file_path: str

    type: Literal["sandbox_write_file"]

    error: Optional[str] = None

    size_bytes: Optional[int] = None


class SandboxReadFileOutputItem(BaseModel):
    """Per-invocation result of the `read` tool inside the sandbox."""

    call_id: str

    file_path: str

    type: Literal["sandbox_read_file"]

    content: Optional[str] = None

    error: Optional[str] = None

    start_line: Optional[int] = None

    total_lines: Optional[int] = None


class SandboxEditFileOutputItem(BaseModel):
    """Per-invocation result of the `edit` tool inside the sandbox."""

    call_id: str

    type: Literal["sandbox_edit_file"]

    error: Optional[str] = None

    file_path: Optional[str] = None

    message: Optional[str] = None


class SandboxGrepOutputItem(BaseModel):
    """Per-invocation result of the `grep` tool inside the sandbox."""

    call_id: str

    type: Literal["sandbox_grep"]

    count: Optional[int] = None

    error: Optional[str] = None

    files: Optional[List[str]] = None

    truncated: Optional[bool] = None


class SandboxGlobOutputItem(BaseModel):
    """Per-invocation result of the `glob` tool inside the sandbox."""

    call_id: str

    type: Literal["sandbox_glob"]

    count: Optional[int] = None

    error: Optional[str] = None

    files: Optional[List[str]] = None

    truncated: Optional[bool] = None


class SandboxApplyPatchOutputItem(BaseModel):
    """Per-invocation result of the `apply_patch` tool inside the sandbox."""

    call_id: str

    type: Literal["sandbox_apply_patch"]

    added: Optional[List[str]] = None

    deleted: Optional[List[str]] = None

    error: Optional[str] = None

    modified: Optional[List[str]] = None


class ShareFileOutputItem(BaseModel):
    """Result of one `share_file` tool call.

    On success, file_id and filename identify a sandbox file downloadable at url.
    """

    call_id: str

    type: Literal["share_file"]

    error: Optional[str] = None

    file_id: Optional[str] = None

    filename: Optional[str] = None

    size_bytes: Optional[int] = None

    url: Optional[str] = None
    """Relative download path, /v1/responses/{id}/files/{file_id}/content."""


class UnknownOutputItem(BaseModel):
    """
    Forward-compat fallback for proto OutputItem variants the gateway does not yet have a typed schema for.
    """

    item_name: str

    payload: Dict[str, object]

    type: Literal["unknown"]


OutputItem: TypeAlias = Annotated[
    Union[
        MessageOutputItem,
        SearchResultsOutputItem,
        FetchURLResultsOutputItem,
        FunctionCallOutputItem,
        McpListToolsOutputItem,
        McpCallOutputItem,
        SkillLoadedOutputItem,
        AdvisorResultOutputItem,
        SandboxResultsOutputItem,
        SandboxWriteFileOutputItem,
        SandboxReadFileOutputItem,
        SandboxEditFileOutputItem,
        SandboxGrepOutputItem,
        SandboxGlobOutputItem,
        SandboxApplyPatchOutputItem,
        ShareFileOutputItem,
        UnknownOutputItem,
    ],
    PropertyInfo(discriminator="type"),
]
