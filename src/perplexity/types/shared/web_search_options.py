# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .user_location import UserLocation

__all__ = ["WebSearchOptions"]


class WebSearchOptions(BaseModel):
    image_results_enhanced_relevance: Optional[bool] = None

    search_context_size: Optional[Literal["low", "medium", "high"]] = None

    search_type: Optional[Literal["fast", "pro", "auto"]] = None

    user_location: Optional[UserLocation] = None
