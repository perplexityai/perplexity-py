# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExecuteCreateParams"]


class ExecuteCreateParams(TypedDict, total=False):
    code: Required[str]
    """Base64 encoded code to execute"""

    language: Required[Literal["python", "bash"]]
    """Programming language of the code"""

    background: bool
    """Run in background (bash only)"""

    execution_timeout: int
    """Execution timeout in seconds (max 120)"""
