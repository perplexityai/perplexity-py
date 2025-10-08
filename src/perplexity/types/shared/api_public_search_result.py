# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["APIPublicSearchResult"]


class APIPublicSearchResult(BaseModel):
    title: str

    url: str

    date: Optional[str] = None

    last_updated: Optional[str] = None

    snippet: Optional[str] = None

    source: Optional[Literal["web", "attachment"]] = None
