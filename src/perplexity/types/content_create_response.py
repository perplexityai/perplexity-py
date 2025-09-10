# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ContentCreateResponse", "Result"]


class Result(BaseModel):
    content: str
    """The full text content of the web page or document"""

    title: str
    """The title of the web page or document"""

    url: str
    """The URL of the web page or document"""

    date: Optional[str] = None
    """The publication date of the content (if available)"""


class ContentCreateResponse(BaseModel):
    id: str
    """Unique identifier for this content retrieval request"""

    results: List[Result]
    """Array of content objects retrieved from the requested URLs"""
