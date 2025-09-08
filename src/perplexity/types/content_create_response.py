# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ContentCreateResponse", "Result"]


class Result(BaseModel):
    content: str

    title: str

    url: str

    date: Optional[str] = None


class ContentCreateResponse(BaseModel):
    id: str

    results: List[Result]
