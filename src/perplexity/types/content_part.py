# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .annotation import Annotation

__all__ = ["ContentPart"]


class ContentPart(BaseModel):
    text: str

    type: Literal["output_text"]
    """Type of a content part"""

    annotations: Optional[List[Annotation]] = None
