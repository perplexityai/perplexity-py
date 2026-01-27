# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FunctionCallOutputItem"]


class FunctionCallOutputItem(BaseModel):
    id: str

    arguments: str
    """JSON string of arguments"""

    call_id: str
    """Correlates with function_call_output input"""

    name: str

    status: Literal["completed", "failed", "in_progress", "requires_action"]
    """Status of a response or output item"""

    type: Literal["function_call"]

    thought_signature: Optional[str] = None
    """Base64-encoded opaque signature for thinking models"""
