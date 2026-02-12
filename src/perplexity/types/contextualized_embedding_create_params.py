# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ContextualizedEmbeddingCreateParams"]


class ContextualizedEmbeddingCreateParams(TypedDict, total=False):
    input: Required[Iterable[SequenceNotStr[str]]]
    """
    Nested array structure where each inner array contains chunks from a single
    document. Chunks within the same document are encoded with document-level
    context awareness. Maximum 512 documents. Total chunks across all documents must
    not exceed 16,000. Total tokens per document must not exceed 32K. All chunks in
    a single request must not exceed 120,000 tokens combined. Empty strings are not
    allowed.
    """

    model: Required[Literal["pplx-embed-context-v1-0.6b", "pplx-embed-context-v1-4b"]]
    """The contextualized embedding model to use"""

    dimensions: int
    """Number of dimensions for output embeddings (Matryoshka).

    Range: 128-1024 for pplx-embed-context-v1-0.6b, 128-2560 for
    pplx-embed-context-v1-4b. Defaults to full dimensions (1024 or 2560).
    """

    encoding_format: Literal["base64_int8", "base64_binary"]
    """Output encoding format for embeddings.

    base64_int8 returns base64-encoded signed int8 values. base64_binary returns
    base64-encoded packed binary (1 bit per dimension).
    """
