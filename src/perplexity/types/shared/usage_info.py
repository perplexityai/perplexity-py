# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UsageInfo", "Cost"]


class Cost(BaseModel):
    input_tokens_cost: float

    output_tokens_cost: float

    total_cost: float

    citation_tokens_cost: Optional[float] = None

    reasoning_tokens_cost: Optional[float] = None

    request_cost: Optional[float] = None

    search_queries_cost: Optional[float] = None


class UsageInfo(BaseModel):
    completion_tokens: int

    cost: Cost

    prompt_tokens: int

    total_tokens: int

    citation_tokens: Optional[int] = None

    num_search_queries: Optional[int] = None

    reasoning_tokens: Optional[int] = None

    search_context_size: Optional[str] = None
