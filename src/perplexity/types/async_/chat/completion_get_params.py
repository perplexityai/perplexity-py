# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CompletionGetParams"]


class CompletionGetParams(TypedDict, total=False):
    local_mode: bool

    x_client_env: Annotated[str, PropertyInfo(alias="x-client-env")]

    x_client_name: Annotated[str, PropertyInfo(alias="x-client-name")]

    x_created_at_epoch_seconds: Annotated[str, PropertyInfo(alias="x-created-at-epoch-seconds")]

    x_request_time: Annotated[str, PropertyInfo(alias="x-request-time")]

    x_usage_tier: Annotated[str, PropertyInfo(alias="x-usage-tier")]

    x_user_id: Annotated[str, PropertyInfo(alias="x-user-id")]
