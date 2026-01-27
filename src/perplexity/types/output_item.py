# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .content_part import ContentPart
from .shared.search_result import SearchResult
from .function_call_output_item import FunctionCallOutputItem

__all__ = [
    "OutputItem",
    "MessageOutputItem",
    "SearchResultsOutputItem",
    "FetchURLResultsOutputItem",
    "FetchURLResultsOutputItemContent",
]


class MessageOutputItem(BaseModel):
    id: str

    content: List[ContentPart]

    role: Literal["assistant"]
    """Role in a message"""

    status: Literal["completed", "failed", "in_progress", "requires_action"]
    """Status of a response or output item"""

    type: Literal["message"]


class SearchResultsOutputItem(BaseModel):
    results: List[SearchResult]

    type: Literal["search_results"]

    queries: Optional[List[str]] = None


class FetchURLResultsOutputItemContent(BaseModel):
    """Content fetched from a URL"""

    snippet: str
    """The fetched content snippet"""

    title: str
    """The title of the page"""

    url: str
    """The URL from which content was fetched"""


class FetchURLResultsOutputItem(BaseModel):
    contents: List[FetchURLResultsOutputItemContent]

    type: Literal["fetch_url_results"]


OutputItem: TypeAlias = Annotated[
    Union[MessageOutputItem, SearchResultsOutputItem, FetchURLResultsOutputItem, FunctionCallOutputItem],
    PropertyInfo(discriminator="type"),
]
