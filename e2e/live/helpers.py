from __future__ import annotations

import os

from perplexity import Perplexity


def api_key() -> str:
    value = os.environ.get("PPLX_API_TOKEN")
    if not value:
        raise AssertionError("PPLX_API_TOKEN must be set")
    return value


def create_client() -> Perplexity:
    return Perplexity(api_key=api_key(), max_retries=0)
