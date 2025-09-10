# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ChatMessage", "ContentMultipartContent", "ContentMultipartContentImageURL"]


class ContentMultipartContentImageURL(BaseModel):
    url: str
    """URL of the image (base64 or HTTPS)"""


class ContentMultipartContent(BaseModel):
    type: Literal["text", "image_url"]
    """The type of content"""

    image_url: Optional[ContentMultipartContentImageURL] = None

    text: Optional[str] = None
    """Text content"""


class ChatMessage(BaseModel):
    content: Union[str, List[ContentMultipartContent]]
    """The content of the message"""

    role: Literal["system", "user", "assistant"]
    """The role of the message author"""
