# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SearchCreateParams"]


class SearchCreateParams(TypedDict, total=False):
    query: Required[Union[str, SequenceNotStr[str]]]
    """Search query string or array of query strings to search for"""

    country: Optional[str]
    """Country code to bias search results towards (e.g., 'US', 'GB', 'CA')"""

    last_updated_after_filter: Optional[str]
    """Only include results last updated after this date (ISO 8601 format: YYYY-MM-DD)"""

    last_updated_before_filter: Optional[str]
    """
    Only include results last updated before this date (ISO 8601 format: YYYY-MM-DD)
    """

    max_results: int
    """Maximum number of search results to return"""

    max_tokens: int
    """Maximum number of tokens to return across all results"""

    max_tokens_per_page: int
    """Maximum number of tokens to return per individual search result"""

    safe_search: Optional[bool]
    """Enable safe search filtering to exclude adult content"""

    search_after_date_filter: Optional[str]
    """Only include results published after this date (ISO 8601 format: YYYY-MM-DD)"""

    search_before_date_filter: Optional[str]
    """Only include results published before this date (ISO 8601 format: YYYY-MM-DD)"""

    search_domain_filter: Optional[SequenceNotStr[str]]
    """
    List of domains to restrict search results to (e.g., ['example.com',
    'another.com'])
    """

    search_mode: Optional[Literal["web", "academic", "sec"]]
    """
    Type of search to perform: 'web' for general web search, 'academic' for
    scholarly articles, 'sec' for SEC filings
    """

    search_recency_filter: Optional[Literal["hour", "day", "week", "month", "year"]]
    """
    Filter results by how recently they were published (hour, day, week, month, or
    year)
    """
