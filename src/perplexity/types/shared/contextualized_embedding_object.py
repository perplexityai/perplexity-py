# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .embedding_object import EmbeddingObject

__all__ = ["ContextualizedEmbeddingObject"]


class ContextualizedEmbeddingObject(BaseModel):
    """A single contextualized embedding result"""

    data: Optional[List[EmbeddingObject]] = None
    """List of embedding objects for chunks in this document"""

    index: Optional[int] = None
    """The index of the document this chunk belongs to"""

    object: Optional[str] = None
    """The object type"""
