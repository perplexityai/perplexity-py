# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "InputItemParam",
    "InputMessage",
    "InputMessageContentContentPartArray",
    "FunctionCallOutputInput",
    "FunctionCallInput",
]


class InputMessageContentContentPartArray(TypedDict, total=False):
    type: Required[Literal["input_text", "input_image"]]

    image_url: str

    text: str


class InputMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[InputMessageContentContentPartArray]]]
    """Message content - either a string or array of content parts"""

    role: Required[Literal["user", "assistant", "system", "developer"]]

    type: Required[Literal["message"]]


class FunctionCallOutputInput(TypedDict, total=False):
    call_id: Required[str]
    """The call_id from function_call output"""

    output: Required[str]
    """Function result (JSON string)"""

    type: Required[Literal["function_call_output"]]

    name: str
    """Function name (required by some providers)"""

    thought_signature: str
    """Base64-encoded signature from function_call"""


class FunctionCallInput(TypedDict, total=False):
    arguments: Required[str]
    """Function arguments (JSON string)"""

    call_id: Required[str]
    """The call_id that correlates with function_call_output"""

    name: Required[str]
    """The function name"""

    type: Required[Literal["function_call"]]

    thought_signature: str
    """Base64-encoded signature for thinking models"""


InputItemParam: TypeAlias = Union[InputMessage, FunctionCallOutputInput, FunctionCallInput]
