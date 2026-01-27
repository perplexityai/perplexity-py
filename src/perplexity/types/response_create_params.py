# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .input_item_param import InputItemParam
from .function_tool_param import FunctionToolParam
from .shared_params.response_format import ResponseFormat

__all__ = [
    "ResponseCreateParamsBase",
    "Reasoning",
    "Tool",
    "ToolWebSearchTool",
    "ToolWebSearchToolFilters",
    "ToolWebSearchToolUserLocation",
    "ToolFetchURLTool",
    "ResponseCreateParamsNonStreaming",
    "ResponseCreateParamsStreaming",
]


class ResponseCreateParamsBase(TypedDict, total=False):
    input: Required[Union[str, Iterable[InputItemParam]]]
    """Input content - either a string or array of input items"""

    instructions: str
    """System instructions for the model"""

    language_preference: str
    """ISO 639-1 language code for response language"""

    max_output_tokens: int
    """Maximum tokens to generate"""

    max_steps: int
    """
    Maximum number of research loop steps. If provided, overrides the preset's
    max_steps value. Must be >= 1 if specified. Maximum allowed is 10.
    """

    model: str
    """
    Model ID in provider/model format (e.g., "xai/grok-4-1", "openai/gpt-4o"). If
    models is also provided, models takes precedence. Required if neither models nor
    preset is provided.
    """

    models: SequenceNotStr[str]
    """Model fallback chain.

    Each model is in provider/model format. Models are tried in order until one
    succeeds. Max 5 models allowed. If set, takes precedence over single model
    field. The response.model will reflect the model that actually succeeded.
    """

    preset: str
    """
    Preset configuration name (e.g., "sonar-pro", "sonar-reasoning"). Pre-configured
    model with system prompt and search parameters. Required if model is not
    provided.
    """

    reasoning: Reasoning

    response_format: ResponseFormat
    """Specifies the desired output format for the model response"""

    tools: Iterable[Tool]
    """Tools available to the model"""


class Reasoning(TypedDict, total=False):
    effort: Literal["low", "medium", "high"]
    """How much effort the model should spend on reasoning"""


class ToolWebSearchToolFilters(TypedDict, total=False):
    last_updated_after_filter: str
    """Input: MM/DD/YYYY, Output: YYYY-MM-DD"""

    last_updated_before_filter: str
    """Input: MM/DD/YYYY, Output: YYYY-MM-DD"""

    search_after_date_filter: str
    """Input: MM/DD/YYYY, Output: YYYY-MM-DD"""

    search_before_date_filter: str
    """Input: MM/DD/YYYY, Output: YYYY-MM-DD"""

    search_domain_filter: SequenceNotStr[str]

    search_recency_filter: Literal["hour", "day", "week", "month", "year"]


class ToolWebSearchToolUserLocation(TypedDict, total=False):
    """User's geographic location for search personalization"""

    city: str

    country: str
    """ISO 3166-1 alpha-2 country code"""

    latitude: float

    longitude: float

    region: str


class ToolWebSearchTool(TypedDict, total=False):
    type: Required[Literal["web_search"]]

    filters: ToolWebSearchToolFilters

    max_tokens: int

    max_tokens_per_page: int

    user_location: ToolWebSearchToolUserLocation
    """User's geographic location for search personalization"""


class ToolFetchURLTool(TypedDict, total=False):
    type: Required[Literal["fetch_url"]]

    max_urls: int
    """Maximum number of URLs to fetch per tool call"""


Tool: TypeAlias = Union[ToolWebSearchTool, ToolFetchURLTool, FunctionToolParam]


class ResponseCreateParamsNonStreaming(ResponseCreateParamsBase, total=False):
    stream: Literal[False]
    """If true, returns SSE stream instead of JSON"""


class ResponseCreateParamsStreaming(ResponseCreateParamsBase):
    stream: Required[Literal[True]]
    """If true, returns SSE stream instead of JSON"""


ResponseCreateParams = Union[ResponseCreateParamsNonStreaming, ResponseCreateParamsStreaming]
