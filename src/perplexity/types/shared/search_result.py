# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SearchResult"]


class SearchResult(BaseModel):
    """A single search result used in LLM responses"""

    id: int

    snippet: str

    title: str

    url: str

    date: Optional[str] = None

    last_updated: Optional[str] = None

    source: Optional[Literal["web"]] = None
    """Source of search results"""
