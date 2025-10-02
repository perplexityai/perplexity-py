# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel
from ...stream_chunk import StreamChunk

__all__ = ["CompletionCreateResponse"]


class CompletionCreateResponse(BaseModel):
    id: str

    created_at: int

    model: str

    status: Literal["CREATED", "IN_PROGRESS", "COMPLETED", "FAILED"]
    """Status enum for async processing."""

    completed_at: Optional[int] = None

    error_message: Optional[str] = None

    failed_at: Optional[int] = None

    response: Optional[StreamChunk] = None

    started_at: Optional[int] = None
