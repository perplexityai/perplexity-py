# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatMessage", "ContentMultipartContent", "ContentMultipartContentImageURL"]


class ContentMultipartContentImageURL(TypedDict, total=False):
    url: Required[str]
    """URL of the image (base64 or HTTPS)"""


class ContentMultipartContent(TypedDict, total=False):
    type: Required[Literal["text", "image_url"]]
    """The type of content"""

    image_url: Optional[ContentMultipartContentImageURL]

    text: Optional[str]
    """Text content"""


class ChatMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[ContentMultipartContent]]]
    """The content of the message"""

    role: Required[Literal["system", "user", "assistant"]]
    """The role of the message author"""
