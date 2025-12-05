# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SearchCreateParams"]


class SearchCreateParams(TypedDict, total=False):
    query: Required[Union[str, SequenceNotStr[str]]]

    country: Optional[str]

    display_server_time: bool

    last_updated_after_filter: Optional[str]

    last_updated_before_filter: Optional[str]

    max_results: int

    max_tokens: int

    max_tokens_per_page: int

    search_after_date_filter: Optional[str]

    search_before_date_filter: Optional[str]

    search_domain_filter: Optional[SequenceNotStr[str]]

    search_language_filter: Optional[SequenceNotStr[str]]

    search_mode: Optional[Literal["web", "academic", "sec"]]

    search_recency_filter: Optional[Literal["hour", "day", "week", "month", "year"]]
