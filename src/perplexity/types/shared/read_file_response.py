# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ReadFileResponse"]


class ReadFileResponse(BaseModel):
    """Response containing file content"""

    content: Optional[str] = None
    """Base64 encoded file content"""

    path: Optional[str] = None
    """Path of the file"""

    size: Optional[int] = None
    """File size in bytes"""
