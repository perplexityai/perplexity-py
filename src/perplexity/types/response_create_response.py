# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .error_info import ErrorInfo
from .output_item import OutputItem, MessageOutputItem
from .responses_usage import ResponsesUsage

__all__ = ["ResponseCreateResponse"]


class ResponseCreateResponse(BaseModel):
    """Non-streaming response returned when stream is false"""

    id: str

    created_at: int

    model: str

    object: Literal["response"]
    """Object type in API responses"""

    output: List[OutputItem]

    status: Literal["completed", "failed", "in_progress", "queued", "cancelled", "requires_action"]
    """Status of a response or output item"""

    background: Optional[bool] = None
    """Whether the response was created in background mode."""

    error: Optional[ErrorInfo] = None

    previous_response_id: Optional[str] = None
    """
    ID of the previous response in the chain, when the response was created with
    previous_response_id.
    """

    store: Optional[bool] = None
    """Whether the response is stored and visible to later retrieve calls.

    A response created with store=false can still be used as a previous_response_id
    continuation source.
    """

    usage: Optional[ResponsesUsage] = None

    @property
    def output_text(self) -> str:
        """Convenience property that aggregates all `output_text` items from the `output` list.

        If no `output_text` content blocks exist, then an empty string is returned.
        """
        texts: List[str] = []
        for output in self.output:
            if isinstance(output, MessageOutputItem):
                for content in output.content:
                    if content.type == "output_text":
                        texts.append(content.text)
        return "".join(texts)
