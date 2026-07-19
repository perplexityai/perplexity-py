from __future__ import annotations

import pytest

from perplexity.lib.model_capabilities import (
    ReturnImagesUnsupportedError,
    UnsupportedParameterError,
    model_supports_reasoning_effort,
    model_supports_search_context_size,
    validate_chat_completion_params,
    validate_return_images,
    validate_search_domain_filter,
)


def test_sonar_rejects_reasoning_effort() -> None:
    with pytest.raises(UnsupportedParameterError, match="reasoning_effort"):
        validate_chat_completion_params(model="sonar", reasoning_effort="high")


def test_sonar_deep_research_allows_reasoning_effort() -> None:
    validate_chat_completion_params(model="sonar-deep-research", reasoning_effort="high")


def test_sonar_rejects_search_context_size() -> None:
    with pytest.raises(UnsupportedParameterError, match="search_context_size"):
        validate_chat_completion_params(model="sonar", search_context_size="high")


def test_sonar_pro_allows_search_context_size() -> None:
    validate_chat_completion_params(model="sonar-pro", search_context_size="medium")


def test_search_domain_filter_rejects_too_many_domains() -> None:
    with pytest.raises(UnsupportedParameterError, match="at most 3"):
        validate_search_domain_filter(
            model="sonar-pro",
            search_domain_filter=["a.com", "b.com", "c.com", "d.com"],
        )


def test_model_supports_flags() -> None:
    assert model_supports_reasoning_effort("sonar-reasoning-pro")
    assert not model_supports_reasoning_effort("sonar")
    assert model_supports_search_context_size("sonar-pro")
    assert not model_supports_search_context_size("sonar")


def test_return_images_still_raises_for_sonar() -> None:
    with pytest.raises(ReturnImagesUnsupportedError):
        validate_return_images(model="sonar", return_images=True)


def test_sonar_pro_supports_return_images() -> None:
    from perplexity.lib.model_capabilities import model_supports_return_images

    assert model_supports_return_images("sonar-pro")


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
