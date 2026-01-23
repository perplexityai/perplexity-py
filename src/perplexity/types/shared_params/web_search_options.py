# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .user_location import UserLocation

__all__ = ["WebSearchOptions"]


class WebSearchOptions(TypedDict, total=False):
    image_results_enhanced_relevance: bool

    search_context_size: Literal["low", "medium", "high"]

    search_type: Optional[Literal["fast", "pro", "auto"]]

    user_location: Optional[UserLocation]
