# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["EmbeddingCreateParams", "ImageInput"]


class ImageInput(TypedDict, total=False):
    type: Required[Literal["image"]]

    image: Required[str]
    """Base64 data URI, for example `data:image/png;base64,...`."""


class EmbeddingCreateParams(TypedDict, total=False):
    input: Required[Union[str, SequenceNotStr[str], Iterable[SequenceNotStr[str]], Iterable[ImageInput]]]
    """Input to embed.

    - A string or array of strings: one embedding per string. Use this for
      queries with any model, and for documents with pplx-embed-v1 models.
    - An array of string arrays (pplx-embed-v2 models, `input_type="document"`):
      each inner array is one document split into chunks. Each chunk is embedded
      in the context of its whole document, and the response returns one
      embedding per chunk in `data[i].data[j]`.
    - An array of `{"type": "image", "image": <data URI>}` objects (pplx-embed-v2
      models, `input_type="document"`). Images cannot be mixed with text.

    Maximum 512 texts per request. Each input must not exceed 32K tokens. All inputs
    in a single request must not exceed 120,000 tokens combined. Empty strings are
    not allowed.
    """

    model: Required[
        Literal[
            "pplx-embed-v2-context-9b",
            "pplx-embed-v2-context-0.6b",
            "pplx-embed-v1-0.6b",
            "pplx-embed-v1-4b",
        ]
    ]
    """The embedding model to use.

    Prefer the pplx-embed-v2 models for new integrations:
    `pplx-embed-v2-context-9b` for the highest quality and
    `pplx-embed-v2-context-0.6b` for lower latency and cost. pplx-embed-v2 models
    require `input_type`. The pplx-embed-v1 models remain supported.
    """

    dimensions: int
    """Number of dimensions for output embeddings (Matryoshka).

    Range: 128-1024 for pplx-embed-v1-0.6b, 128-2560 for pplx-embed-v1-4b, 1024 for
    pplx-embed-v2-context-0.6b, 1024 or 2048 for pplx-embed-v2-context-9b.
    Defaults to full dimensions (1024, 2560, 1024, or 2048 respectively).
    """

    encoding_format: Literal["base64_int8", "base64_binary"]
    """Output encoding format for embeddings.

    base64_int8 returns base64-encoded signed int8 values. base64_binary returns
    base64-encoded packed binary (1 bit per dimension).
    """

    input_type: Literal["query", "document"]
    """Whether the inputs are search queries or documents.

    Required for pplx-embed-v2 models. Embed search queries with `"query"` and
    the content you search over with `"document"`.
    """

    num_chunks: Literal[1, 2, 4, 8, 16, 32]
    """Embeddings per image input (pplx-embed-v2 models only)."""
