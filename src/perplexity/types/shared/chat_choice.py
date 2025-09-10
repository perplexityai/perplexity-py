# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .chat_message import ChatMessage

__all__ = ["ChatChoice"]


class ChatChoice(BaseModel):
    index: int

    message: ChatMessage

    finish_reason: Optional[Literal["stop", "length"]] = None
