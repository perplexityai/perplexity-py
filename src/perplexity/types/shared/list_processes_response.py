# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .process_info import ProcessInfo

__all__ = ["ListProcessesResponse"]


class ListProcessesResponse(BaseModel):
    """Response containing list of running processes"""

    processes: Optional[List[ProcessInfo]] = None
    """List of running processes"""
