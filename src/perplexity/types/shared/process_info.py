# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ProcessInfo"]


class ProcessInfo(BaseModel):
    """Information about a running process"""

    command: Optional[str] = None
    """Command that started the process"""

    pid: Optional[int] = None
    """Process ID"""

    status: Optional[str] = None
    """Current status of the process"""
