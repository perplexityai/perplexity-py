# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .error_info import ErrorInfo
from .output_item import OutputItem
from .responses_usage import ResponsesUsage

__all__ = ["ResponseCreateResponse"]


class ResponseCreateResponse(BaseModel):
    """Non-streaming response returned when stream is false"""

    id: str

    created_at: int

    model: str

    object: Literal["response"]
    """Object type in API responses"""

    output: List[OutputItem]

    status: Literal["completed", "failed", "in_progress"]
    """Status of a response or output item"""

    error: Optional[ErrorInfo] = None

    usage: Optional[ResponsesUsage] = None
