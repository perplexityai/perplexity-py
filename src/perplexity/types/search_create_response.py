# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SearchCreateResponse", "Result"]


class Result(BaseModel):
    snippet: str

    title: str

    url: str

    date: Optional[str] = None

    last_updated: Optional[str] = None


class SearchCreateResponse(BaseModel):
    id: str

    results: List[Result]

    server_time: Optional[str] = None
