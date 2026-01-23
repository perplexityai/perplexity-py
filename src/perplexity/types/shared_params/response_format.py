# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .json_schema_format import JsonSchemaFormat

__all__ = ["ResponseFormat"]


class ResponseFormat(TypedDict, total=False):
    """Specifies the desired output format for the model response"""

    type: Required[Literal["json_schema"]]
    """The type of response format"""

    json_schema: JsonSchemaFormat
    """Defines a JSON schema for structured output validation"""
