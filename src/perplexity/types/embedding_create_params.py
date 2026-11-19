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
    """Input to embed. The shape of `input` sets the shape of the response.

    - A string or array of strings: one embedding per string in
      `data[i].embedding`. With pplx-embed-v2 models, set `input_type` to
      `"query"` for search queries or `"document"` for whole documents.
    - An array of string arrays (pplx-embed-v2, `input_type="document"`): each
      inner array holds one document's non-overlapping chunks in source order.
      Each chunk is embedded in the context of its whole document, and the
      response returns one embedding per chunk in `data[i].data[j].embedding`.
    - An array of `{"type": "image", "image": <data URI>}` objects (pplx-embed-v2,
      `input_type="document"`): JPEG, PNG, or WebP. One embedding per image in
      `data[i].embedding`, or one per region in `data[i].data[j].embedding` when
      `num_chunks` is above 1. A request holds either text or images, not both.

    Maximum 512 texts or documents, 16,000 chunks, or 96 images (20 MB of base64
    data) per request. Each text or document must not exceed 32K tokens, and all
    text in a request must not exceed 120,000 tokens. Empty strings are not
    allowed.
    """

    model: Required[
        Literal[
            "pplx-embed-v2-context-0.6b",
            "pplx-embed-v2-context-9b",
            "pplx-embed-v1-0.6b",
            "pplx-embed-v1-4b",
        ]
    ]
    """The embedding model to use.

    Start with `pplx-embed-v2-context-0.6b` for higher throughput and lower
    latency; choose `pplx-embed-v2-context-9b` for retrieval quality. Their
    1024-dimension outputs share one embedding space. pplx-embed-v2 models
    require `input_type`. pplx-embed-v1 models will be phased out during 2027.
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
    """Required for pplx-embed-v2 models.

    Use `"query"` only for the text a user types to search, and `"document"` for
    everything you index, including chunked documents and images. Omit for
    pplx-embed-v1 models.
    """

    num_chunks: Literal[1, 2, 4, 8, 16, 32]
    """Regions per image (pplx-embed-v2 image inputs only). Defaults to 1.

    Values above 1 split each image into horizontal regions, top to bottom, and
    return one embedding per region. This can improve retrieval for text-rich
    document screenshots. Small images can return fewer regions.
    """
