# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FileWriteParams"]


class FileWriteParams(TypedDict, total=False):
    content: Required[str]
    """Base64 encoded file content"""

    path: Required[str]
    """Absolute path where the file should be written"""
