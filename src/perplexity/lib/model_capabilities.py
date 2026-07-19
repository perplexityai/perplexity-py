from __future__ import annotations

from typing import Final, FrozenSet

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


class ReturnImagesUnsupportedError(ValueError):
    """Raised when return_images=True is requested for a model that does not return images."""


def model_supports_return_images(model: str) -> bool:
    normalized = model.strip().lower()
    if normalized in MODELS_WITHOUT_RETURN_IMAGES:
        return False
    if normalized in MODELS_SUPPORTING_RETURN_IMAGES:
        return True
    # Unknown/new models: allow the request but callers should verify response.images.
    return True


def validate_return_images(*, model: str, return_images: object) -> None:
    if return_images is omit or return_images is None or return_images is False:
        return
    if return_images is True and not model_supports_return_images(model):
        raise ReturnImagesUnsupportedError(
            f"Model {model!r} does not return images when return_images=True. "
            f"Use one of {sorted(MODELS_SUPPORTING_RETURN_IMAGES)} instead."
        )
