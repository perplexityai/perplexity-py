from __future__ import annotations

import pytest

from perplexity.lib.model_capabilities import (
    ReturnImagesUnsupportedError,
    model_supports_return_images,
    validate_return_images,
)


def test_sonar_does_not_support_return_images() -> None:
    assert not model_supports_return_images("sonar")


def test_sonar_pro_supports_return_images() -> None:
    assert model_supports_return_images("sonar-pro")


def test_validate_return_images_raises_for_sonar() -> None:
    with pytest.raises(ReturnImagesUnsupportedError, match="sonar"):
        validate_return_images(model="sonar", return_images=True)


def test_validate_return_images_allows_sonar_pro() -> None:
    validate_return_images(model="sonar-pro", return_images=True)


def test_validate_return_images_ignores_false_and_omit() -> None:
    validate_return_images(model="sonar", return_images=False)
    validate_return_images(model="sonar", return_images=None)


def test_stream_chunk_parses_images_field() -> None:
    from perplexity.types import StreamChunk

    chunk = StreamChunk.model_validate(
        {
            "id": "id",
            "choices": [
                {
                    "index": 0,
                    "delta": {"role": "assistant", "content": ""},
                    "message": {"role": "assistant", "content": "hi"},
                    "finish_reason": "stop",
                }
            ],
            "created": 1,
            "model": "sonar-pro",
            "images": ["https://example.com/a.png"],
        }
    )
    assert chunk.images == ["https://example.com/a.png"]
