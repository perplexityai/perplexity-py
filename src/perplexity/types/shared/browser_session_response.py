# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BrowserSessionResponse"]


class BrowserSessionResponse(BaseModel):
    """Response containing browser session details"""

    session_id: Optional[str] = None
    """Unique identifier for the browser session"""

    status: Optional[Literal["running", "stopped"]] = None
    """Current status of the session"""
