# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["PauseSandboxResponse"]


class PauseSandboxResponse(BaseModel):
    """Response from pausing a sandbox session"""

    file_count: Optional[int] = None
    """Number of files in the snapshot"""

    file_list: Optional[List[str]] = None
    """List of files included in the snapshot"""

    s3_bucket: Optional[str] = None
    """S3 bucket containing the snapshot"""

    s3_key: Optional[str] = None
    """S3 object key for the snapshot"""

    s3_uploaded: Optional[bool] = None
    """Whether the snapshot was uploaded to S3"""

    success: Optional[bool] = None
    """Whether the pause was successful"""

    tarball_size: Optional[int] = None
    """Size of the snapshot in bytes"""
