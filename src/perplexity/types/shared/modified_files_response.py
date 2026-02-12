# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ModifiedFilesResponse"]


class ModifiedFilesResponse(BaseModel):
    """Response containing list of modified files since session start"""

    files: Optional[List[str]] = None
    """List of modified file paths"""
