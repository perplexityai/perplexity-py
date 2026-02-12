# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FileEntry"]


class FileEntry(BaseModel):
    """A file or directory entry"""

    path: Optional[str] = None
    """Absolute path of the entry"""

    size: Optional[int] = None
    """Size in bytes (0 for directories)"""

    type: Optional[Literal["file", "directory"]] = None
    """Entry type"""
