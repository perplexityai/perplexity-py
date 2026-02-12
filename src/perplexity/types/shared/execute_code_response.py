# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ExecuteCodeResponse", "Output"]


class Output(BaseModel):
    content: Optional[str] = None
    """Output content"""

    type: Optional[str] = None
    """Output type (stdout, stderr)"""


class ExecuteCodeResponse(BaseModel):
    """Response from code execution"""

    error: Optional[str] = None
    """Error message if execution failed"""

    execution_time_ms: Optional[float] = None
    """Time taken to execute the code in milliseconds"""

    exit_code: Optional[int] = None
    """Process exit code (0 for success)"""

    is_background: Optional[bool] = None
    """Whether this was a background execution"""

    output: Optional[List[Output]] = None
    """Structured output from the execution"""

    process_id: Optional[int] = None
    """PID of the background process (only for background execution)"""

    stderr: Optional[str] = None
    """Standard error from the execution"""

    stdout: Optional[str] = None
    """Standard output from the execution"""

    success: Optional[bool] = None
    """Whether the execution completed successfully"""
