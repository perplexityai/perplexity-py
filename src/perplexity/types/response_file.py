# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ResponseFile"]


class ResponseFile(BaseModel):
    """Metadata for a file shared from a response sandbox via the share_file tool."""

    id: str
    """File identifier, scoped to the parent response."""

    bytes: int
    """Size of the file in bytes."""

    created_at: int
    """Unix timestamp (seconds) when the file was produced."""

    filename: str
    """Original filename set by the share_file tool call."""

    object: Literal["file"]
    """Object type. Always `file`."""
