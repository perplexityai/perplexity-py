# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["EmbeddingCreateParams"]


class EmbeddingCreateParams(TypedDict, total=False):
    input: Required[Union[str, SequenceNotStr[str]]]
    """Input text to embed, encoded as a string or array of strings.

    Maximum 512 texts per request. Each input must not exceed 32K tokens. All inputs
    in a single request must not exceed 120,000 tokens combined. Empty strings are
    not allowed.
    """

    model: Required[Literal["pplx-embed-v1-0.6b", "pplx-embed-v1-4b"]]
    """The embedding model to use"""

    dimensions: int
    """Number of dimensions for output embeddings (Matryoshka).

    Range: 128-1024 for pplx-embed-v1-0.6b, 128-2560 for pplx-embed-v1-4b. Defaults
    to full dimensions (1024 or 2560).
    """

    encoding_format: Literal["base64_int8", "base64_binary"]
    """Output encoding format for embeddings.

    base64_int8 returns base64-encoded signed int8 values. base64_binary returns
    base64-encoded packed binary (1 bit per dimension).
    """
