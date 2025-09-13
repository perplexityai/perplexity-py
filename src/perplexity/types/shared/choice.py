# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .chat_message_output import ChatMessageOutput

__all__ = ["Choice"]


class Choice(BaseModel):
    delta: ChatMessageOutput

    index: int

    message: ChatMessageOutput

    finish_reason: Optional[Literal["stop", "length"]] = None
