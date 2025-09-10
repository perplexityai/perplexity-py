# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel
from ...shared.usage_info import UsageInfo
from ...shared.chat_choice import ChatChoice
from ...shared.search_result import SearchResult

__all__ = ["CompletionGetResponse", "Response"]


class Response(BaseModel):
    id: str
    """Unique identifier for the chat completion"""

    choices: List[ChatChoice]

    created: int
    """Unix timestamp of creation"""

    model: str
    """The model used"""

    object: str

    usage: UsageInfo

    search_results: Optional[List[SearchResult]] = None
    """Search results used in generating the response"""


class CompletionGetResponse(BaseModel):
    id: str
    """Unique identifier for the async job"""

    created_at: int
    """Unix timestamp of creation"""

    model: str

    status: Literal["CREATED", "IN_PROGRESS", "COMPLETED", "FAILED"]

    completed_at: Optional[int] = None

    error_message: Optional[str] = None

    failed_at: Optional[int] = None

    response: Optional[Response] = None
    """The completion response when status is COMPLETED"""

    started_at: Optional[int] = None
