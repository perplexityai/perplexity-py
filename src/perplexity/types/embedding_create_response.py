# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.embedding_object import EmbeddingObject
from .shared.embeddings_usage import EmbeddingsUsage

__all__ = ["EmbeddingCreateResponse"]


class EmbeddingCreateResponse(BaseModel):
    """Response body for embeddings request"""

    data: Optional[List[EmbeddingObject]] = None
    """List of embedding objects"""

    model: Optional[str] = None
    """The model used to generate embeddings"""

    object: Optional[str] = None
    """The object type"""

    usage: Optional[EmbeddingsUsage] = None
    """Token usage for the embeddings request"""
