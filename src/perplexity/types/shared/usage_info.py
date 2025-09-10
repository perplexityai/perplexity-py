# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UsageInfo"]


class UsageInfo(BaseModel):
    completion_tokens: int

    prompt_tokens: int

    total_tokens: int

    citation_tokens: Optional[int] = None

    num_search_queries: Optional[int] = None

    reasoning_tokens: Optional[int] = None

    search_context_size: Optional[str] = None
