# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ResponseCancelResponse"]


class ResponseCancelResponse(BaseModel):
    response_id: str
    """The response id (resp\\__...)."""

    status: Literal["cancelling"]
    """Always `cancelling`: the cancel was accepted and the run stops asynchronously.

    An already terminal run returns 400 instead, so no terminal status appears here.
    """
