# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Annotation"]


class Annotation(BaseModel):
    """Text annotation (e.g., URL citation)"""

    end_index: Optional[int] = None

    start_index: Optional[int] = None

    title: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None
