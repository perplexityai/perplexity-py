# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EmbeddingsUsage", "Cost"]


class Cost(BaseModel):
    """Cost breakdown for the request"""

    currency: Optional[Literal["USD"]] = None
    """Currency of the cost values"""

    input_cost: Optional[float] = None
    """Cost for input tokens in USD"""

    total_cost: Optional[float] = None
    """Total cost for the request in USD"""


class EmbeddingsUsage(BaseModel):
    """Token usage for the embeddings request"""

    cost: Optional[Cost] = None
    """Cost breakdown for the request"""

    prompt_tokens: Optional[int] = None
    """Number of tokens in the input texts"""

    total_tokens: Optional[int] = None
    """Total number of tokens processed"""
