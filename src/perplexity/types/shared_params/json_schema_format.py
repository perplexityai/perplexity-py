# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["JsonSchemaFormat"]


class JsonSchemaFormat(TypedDict, total=False):
    """Defines a JSON schema for structured output validation"""

    name: Required[str]
    """Name of the schema (1-64 alphanumeric chars)"""

    schema: Required[Dict[str, object]]
    """The JSON schema object"""

    description: str
    """Optional description of the schema"""

    strict: bool
    """Whether to enforce strict schema validation"""
