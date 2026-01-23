# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ErrorInfo"]


class ErrorInfo(BaseModel):
    message: str

    code: Optional[str] = None

    type: Optional[str] = None
