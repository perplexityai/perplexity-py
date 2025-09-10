# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SearchCreateResponse", "Result"]


class Result(BaseModel):
    snippet: str
    """A brief excerpt or summary of the page content"""

    title: str
    """The title of the search result page"""

    url: str
    """The URL of the search result page"""

    date: Optional[str] = None
    """The publication date of the content (if available)"""

    last_updated: Optional[str] = None
    """When the content was last updated (if available)"""


class SearchCreateResponse(BaseModel):
    id: str
    """Unique identifier for this search request"""

    results: List[Result]
    """Array of search result pages matching the query"""
