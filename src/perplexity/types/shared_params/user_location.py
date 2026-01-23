# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["UserLocation"]


class UserLocation(TypedDict, total=False):
    city: Optional[str]

    country: Optional[str]

    latitude: Optional[float]

    longitude: Optional[float]

    region: Optional[str]
