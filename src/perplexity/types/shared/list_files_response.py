# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .file_entry import FileEntry

__all__ = ["ListFilesResponse"]


class ListFilesResponse(BaseModel):
    """Response containing directory listing"""

    entries: Optional[List[FileEntry]] = None
    """List of file and directory entries"""
