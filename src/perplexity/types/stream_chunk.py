# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.choice import Choice
from .shared.usage_info import UsageInfo
from .shared.api_public_search_result import APIPublicSearchResult

__all__ = ["StreamChunk"]


class StreamChunk(BaseModel):
    id: str

    choices: List[Choice]

    created: int

    model: str

    citations: Optional[List[str]] = None

    object: Optional[str] = None

    search_results: Optional[List[APIPublicSearchResult]] = None

    status: Optional[Literal["PENDING", "COMPLETED"]] = None

    type: Optional[Literal["message", "info", "end_of_stream"]] = None

    usage: Optional[UsageInfo] = None
