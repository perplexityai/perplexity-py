# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["APIPublicSearchResult"]


class APIPublicSearchResult(TypedDict, total=False):
    title: Required[str]

    url: Required[str]

    date: Optional[str]

    last_updated: Optional[str]

    snippet: str
