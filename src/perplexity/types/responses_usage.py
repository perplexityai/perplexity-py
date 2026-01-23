# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ResponsesUsage", "Cost", "InputTokensDetails", "ToolCallsDetails"]


class Cost(BaseModel):
    currency: Literal["USD"]
    """Currency code for cost values"""

    input_cost: float

    output_cost: float

    total_cost: float

    cache_creation_cost: Optional[float] = None

    cache_read_cost: Optional[float] = None

    tool_calls_cost: Optional[float] = None


class InputTokensDetails(BaseModel):
    cache_creation_input_tokens: Optional[int] = None

    cache_read_input_tokens: Optional[int] = None


class ToolCallsDetails(BaseModel):
    invocation: Optional[int] = None
    """Number of times this tool was invoked"""


class ResponsesUsage(BaseModel):
    input_tokens: int

    output_tokens: int

    total_tokens: int

    cost: Optional[Cost] = None

    input_tokens_details: Optional[InputTokensDetails] = None

    tool_calls_details: Optional[Dict[str, ToolCallsDetails]] = None
