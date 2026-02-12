# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["WriteFileResponse"]


class WriteFileResponse(BaseModel):
    """Response from writing a file"""

    path: Optional[str] = None
    """Path where the file was written"""

    success: Optional[bool] = None
    """Whether the file was written successfully"""
