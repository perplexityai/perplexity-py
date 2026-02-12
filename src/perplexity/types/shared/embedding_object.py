# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["EmbeddingObject"]


class EmbeddingObject(BaseModel):
    """A single embedding result"""

    embedding: Optional[str] = None
    """Base64-encoded embedding vector.

    For base64_int8: decode to signed int8 array (length = dimensions). For
    base64_binary: decode to packed bits (length = dimensions / 8 bytes).
    """

    index: Optional[int] = None
    """The index of the input text this embedding corresponds to"""

    object: Optional[str] = None
    """The object type"""
