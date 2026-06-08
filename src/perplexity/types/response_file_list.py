# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .response_file import ResponseFile

__all__ = ["ResponseFileList"]


class ResponseFileList(BaseModel):
    data: List[ResponseFile]

    object: Literal["list"]
    """Object type. Always `list`."""
