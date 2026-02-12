# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SandboxSessionResponse"]


class SandboxSessionResponse(BaseModel):
    """Response containing sandbox session details"""

    execute_url: Optional[str] = None
    """URL endpoint for executing code in this session"""

    network_enabled: Optional[bool] = None
    """Whether network access is enabled"""

    session_id: Optional[str] = None
    """Unique identifier for the sandbox session"""

    status: Optional[Literal["running", "pending", "failed", "succeeded", "unknown", "paused"]] = None
    """Current status of the session"""
