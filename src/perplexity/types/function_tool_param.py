# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FunctionToolParam"]


class FunctionToolParam(TypedDict, total=False):
    name: Required[str]
    """The name of the function"""

    type: Required[Literal["function"]]

    description: str
    """A description of what the function does"""

    parameters: Dict[str, object]
    """JSON Schema defining the function's parameters"""

    strict: bool
    """Whether to enable strict schema validation"""
