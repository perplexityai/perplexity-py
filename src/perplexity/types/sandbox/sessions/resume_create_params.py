# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ResumeCreateParams"]


class ResumeCreateParams(TypedDict, total=False):
    network_enabled: bool
    """Override network setting when resuming"""
