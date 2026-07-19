from __future__ import annotations

from typing import Final, FrozenSet, Iterable

from perplexity._types import Omit, omit

MODELS_SUPPORTING_RETURN_IMAGES: Final[FrozenSet[str]] = frozenset(
    {
        "sonar-pro",
        "sonar-reasoning-pro",
        "sonar-deep-research",
    }
)

MODELS_WITHOUT_RETURN_IMAGES: Final[FrozenSet[str]] = frozenset(
    {
        "sonar",
    }
)

MODELS_SUPPORTING_REASONING_EFFORT: Final[FrozenSet[str]] = frozenset(
    {
        "sonar-deep-research",
        "sonar-reasoning-pro",
    }
)

MODELS_SUPPORTING_SEARCH_CONTEXT_SIZE: Final[FrozenSet[str]] = frozenset(
    {
        "sonar-pro",
        "sonar-reasoning-pro",
    }
)

MAX_SEARCH_DOMAIN_FILTERS: Final[int] = 3


class UnsupportedParameterError(ValueError):
    """Raised when a request parameter is not supported for the selected model."""


class ReturnImagesUnsupportedError(UnsupportedParameterError):
    """Raised when return_images=True is requested for a model that does not return images."""


def _normalize_model(model: str) -> str:
    return model.strip().lower()


def _is_omitted(value: object) -> bool:
    return value is omit or value is None or value is False


def model_supports_return_images(model: str) -> bool:
    normalized = _normalize_model(model)
    if normalized in MODELS_WITHOUT_RETURN_IMAGES:
        return False
    if normalized in MODELS_SUPPORTING_RETURN_IMAGES:
        return True
    return True


def model_supports_reasoning_effort(model: str) -> bool:
    return _normalize_model(model) in MODELS_SUPPORTING_REASONING_EFFORT


def model_supports_search_context_size(model: str) -> bool:
    return _normalize_model(model) in MODELS_SUPPORTING_SEARCH_CONTEXT_SIZE


def validate_return_images(*, model: str, return_images: object) -> None:
    if _is_omitted(return_images):
        return
    if return_images is True and not model_supports_return_images(model):
        raise ReturnImagesUnsupportedError(
            f"Model {model!r} does not return images when return_images=True. "
            f"Use one of {sorted(MODELS_SUPPORTING_RETURN_IMAGES)} instead."
        )


def validate_reasoning_effort(*, model: str, reasoning_effort: object) -> None:
    if _is_omitted(reasoning_effort):
        return
    if not model_supports_reasoning_effort(model):
        raise UnsupportedParameterError(
            f"Model {model!r} does not support reasoning_effort. "
            f"Use one of {sorted(MODELS_SUPPORTING_REASONING_EFFORT)} instead."
        )


def validate_search_context_size(*, model: str, search_context_size: object) -> None:
    if _is_omitted(search_context_size):
        return
    if not model_supports_search_context_size(model):
        raise UnsupportedParameterError(
            f"Model {model!r} does not support search_context_size. "
            f"Use one of {sorted(MODELS_SUPPORTING_SEARCH_CONTEXT_SIZE)} instead."
        )


def validate_search_domain_filter(*, model: str, search_domain_filter: object) -> None:
    if _is_omitted(search_domain_filter):
        return
    if not isinstance(search_domain_filter, Iterable) or isinstance(search_domain_filter, (str, bytes)):
        raise UnsupportedParameterError("search_domain_filter must be a sequence of domain strings")
    domains = list(search_domain_filter)
    if len(domains) > MAX_SEARCH_DOMAIN_FILTERS:
        raise UnsupportedParameterError(
            f"search_domain_filter accepts at most {MAX_SEARCH_DOMAIN_FILTERS} domains; got {len(domains)}"
        )


def validate_chat_completion_params(
    *,
    model: str,
    return_images: object = omit,
    reasoning_effort: object = omit,
    search_context_size: object = omit,
    search_domain_filter: object = omit,
) -> None:
    validate_return_images(model=model, return_images=return_images)
    validate_reasoning_effort(model=model, reasoning_effort=reasoning_effort)
    validate_search_context_size(model=model, search_context_size=search_context_size)
    validate_search_domain_filter(model=model, search_domain_filter=search_domain_filter)
