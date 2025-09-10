# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.usage_info import UsageInfo
from ..shared.chat_choice import ChatChoice
from ..shared.search_result import SearchResult

__all__ = ["CompletionCreateResponse"]


class CompletionCreateResponse(BaseModel):
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
