"""Hand-maintained helpers that are not modified by the Stainless generator."""

from .model_capabilities import (
    MODELS_SUPPORTING_RETURN_IMAGES,
    MODELS_WITHOUT_RETURN_IMAGES,
    ReturnImagesUnsupportedError,
    model_supports_return_images,
    validate_return_images,
)

__all__ = [
    "MODELS_SUPPORTING_RETURN_IMAGES",
    "MODELS_WITHOUT_RETURN_IMAGES",
    "ReturnImagesUnsupportedError",
    "model_supports_return_images",
    "validate_return_images",
]
