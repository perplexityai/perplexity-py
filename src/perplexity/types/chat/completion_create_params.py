# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from ..shared_params.chat_message import ChatMessage

__all__ = ["CompletionCreateParams", "WebSearchOptions", "WebSearchOptionsUserLocation"]


class CompletionCreateParams(TypedDict, total=False):
    messages: Required[Iterable[ChatMessage]]
    """A list of messages comprising the conversation so far"""

    model: Required[Literal["sonar", "sonar-pro", "sonar-deep-research", "sonar-reasoning", "sonar-reasoning-pro"]]
    """The name of the model that will complete your prompt"""

    disable_search: bool
    """Disables web search completely - model uses only training data"""

    enable_search_classifier: bool
    """Enables classifier that decides if web search is needed"""

    last_updated_after_filter: Optional[str]
    """Only include content last updated after this date (YYYY-MM-DD)"""

    last_updated_before_filter: Optional[str]
    """Only include content last updated before this date (YYYY-MM-DD)"""

    reasoning_effort: Optional[Literal["low", "medium", "high"]]
    """Controls computational effort for sonar-deep-research model.

    Higher effort = more thorough but more tokens
    """

    return_images: bool
    """Whether to include images in search results"""

    return_related_questions: bool
    """Whether to return related questions"""

    search_after_date_filter: Optional[str]
    """Only include content published after this date (YYYY-MM-DD)"""

    search_before_date_filter: Optional[str]
    """Only include content published before this date (YYYY-MM-DD)"""

    search_domain_filter: Optional[SequenceNotStr[str]]
    """List of domains to limit search results to. Use '-' prefix to exclude domains"""

    search_mode: Optional[Literal["web", "academic", "sec"]]
    """
    Type of search: 'web' for general, 'academic' for scholarly, 'sec' for SEC
    filings
    """

    search_recency_filter: Optional[Literal["hour", "day", "week", "month", "year"]]
    """Filter results by how recently they were published"""

    web_search_options: WebSearchOptions


class WebSearchOptionsUserLocation(TypedDict, total=False):
    city: Optional[str]

    country: Optional[str]
    """Two-letter ISO country code"""

    latitude: Optional[float]

    longitude: Optional[float]

    region: Optional[str]
    """State/province name"""


class WebSearchOptions(TypedDict, total=False):
    image_search_relevance_enhanced: bool
    """Improves relevance of image search results"""

    search_context_size: Literal["low", "medium", "high"]
    """
    Amount of search context retrieved: low (cost-saving), medium (balanced), high
    (comprehensive)
    """

    user_location: WebSearchOptionsUserLocation
