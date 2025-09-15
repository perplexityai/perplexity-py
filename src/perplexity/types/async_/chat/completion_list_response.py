# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CompletionListResponse", "Request"]


class Request(BaseModel):
    id: str

    created_at: int

    model: str

    status: Literal["CREATED", "IN_PROGRESS", "COMPLETED", "FAILED"]
    """Status enum for async processing."""

    completed_at: Optional[int] = None

    failed_at: Optional[int] = None

    started_at: Optional[int] = None


class CompletionListResponse(BaseModel):
    requests: List[Request]

    next_token: Optional[str] = None
