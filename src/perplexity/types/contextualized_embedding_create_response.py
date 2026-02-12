# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.embeddings_usage import EmbeddingsUsage
from .shared.contextualized_embedding_object import ContextualizedEmbeddingObject

__all__ = ["ContextualizedEmbeddingCreateResponse"]


class ContextualizedEmbeddingCreateResponse(BaseModel):
    """Response body for contextualized embeddings request"""

    data: Optional[List[ContextualizedEmbeddingObject]] = None
    """List of contextualized embedding objects"""

    model: Optional[str] = None
    """The model used to generate embeddings"""

    object: Optional[str] = None
    """The object type"""

    usage: Optional[EmbeddingsUsage] = None
    """Token usage for the embeddings request"""
