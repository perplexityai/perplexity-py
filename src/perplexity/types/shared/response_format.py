# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .json_schema_format import JsonSchemaFormat

__all__ = ["ResponseFormat"]


class ResponseFormat(BaseModel):
    """Specifies the desired output format for the model response"""

    type: Literal["json_schema"]
    """The type of response format"""

    json_schema: Optional[JsonSchemaFormat] = None
    """Defines a JSON schema for structured output validation"""
