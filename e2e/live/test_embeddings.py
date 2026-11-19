from __future__ import annotations

import zlib
import base64
import struct

from e2e.live.helpers import create_client


def png_data_uri(size: int = 64) -> str:
    """Build a small RGB gradient PNG so the test needs no fixture file."""

    def chunk(kind: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data))

    rows = b"".join(
        b"\x00" + b"".join(bytes([x * 255 // size, y * 255 // size, 128]) for x in range(size)) for y in range(size)
    )
    png = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(rows))
        + chunk(b"IEND", b"")
    )
    return "data:image/png;base64," + base64.b64encode(png).decode()


def test_embeddings() -> None:
    with create_client() as client:
        embeddings = client.embeddings.create(
            dimensions=128,
            input="Perplexity answers questions.",
            model="pplx-embed-v1-0.6b",
        )

    assert embeddings.model
    assert embeddings.data
    assert embeddings.data[0].index == 0
    assert embeddings.data[0].embedding


def test_embeddings_v2_query() -> None:
    with create_client() as client:
        embeddings = client.embeddings.create(
            input=["What does Perplexity do?"],
            input_type="query",
            model="pplx-embed-v2-context-0.6b",
        )

    assert embeddings.model
    assert embeddings.data
    assert embeddings.data[0].index == 0
    assert embeddings.data[0].embedding


def test_embeddings_v2_document() -> None:
    with create_client() as client:
        embeddings = client.embeddings.create(
            input=[["Perplexity answers questions.", "Its answers include citations."]],
            input_type="document",
            model="pplx-embed-v2-context-0.6b",
        )

    assert embeddings.model
    assert embeddings.data
    chunks = embeddings.data[0].data
    assert chunks
    assert [chunk.index for chunk in chunks] == [0, 1]
    assert all(chunk.embedding for chunk in chunks)


def test_embeddings_v2_image() -> None:
    with create_client() as client:
        embeddings = client.embeddings.create(
            input=[{"type": "image", "image": png_data_uri()}],
            input_type="document",
            model="pplx-embed-v2-context-0.6b",
        )

    assert embeddings.data
    assert embeddings.data[0].index == 0
    assert embeddings.data[0].embedding


def test_embeddings_v2_image_regions() -> None:
    with create_client() as client:
        embeddings = client.embeddings.create(
            input=[{"type": "image", "image": png_data_uri(256)}],
            input_type="document",
            model="pplx-embed-v2-context-0.6b",
            num_chunks=2,
        )

    assert embeddings.data
    regions = embeddings.data[0].data
    assert regions
    # Small images can return fewer regions than requested.
    assert 1 <= len(regions) <= 2
    assert all(region.embedding for region in regions)
