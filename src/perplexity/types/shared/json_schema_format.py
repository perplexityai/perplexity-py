# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["JsonSchemaFormat"]


class JsonSchemaFormat(BaseModel):
    """Defines a JSON schema for structured output validation"""

    name: str
    """Name of the schema (1-64 alphanumeric chars)"""

    schema_: Dict[str, object] = FieldInfo(alias="schema")
    """The JSON schema object"""

    description: Optional[str] = None
    """Optional description of the schema"""

    strict: Optional[bool] = None
    """Whether to enforce strict schema validation"""
