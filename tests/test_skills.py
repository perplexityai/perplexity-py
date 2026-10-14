from __future__ import annotations

import io
import zipfile
from email import policy
from typing import Any, cast
from email.parser import BytesParser

import httpx
import pytest
from pydantic import ValidationError

from perplexity import Perplexity, AsyncPerplexity
from perplexity.types import ManagedSkill, SkillListResponse, SkillDownloadResponse, SkillRevisionListResponse


def bundle() -> bytes:
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w") as archive:
        archive.writestr("SKILL.md", "---\nname: example\ndescription: Example\n---\n")
    return output.getvalue()


@pytest.mark.parametrize(
    "invalid_file",
    ["bundle.zip", ("bundle.zip", "not bytes"), ("bundle.zip", "not bytes", "application/zip")],
)
def test_upload_rejects_strings_without_sending_a_request(invalid_file: object) -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(201, json={"skill_id": "example"})

    with Perplexity(
        api_key="test",
        base_url="https://example.test",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    ) as client:
        with pytest.raises(ValidationError):
            client.skills.create(file=cast(Any, invalid_file))
    assert requests == []


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.asyncio
async def test_skill_lifecycle(asynchronous: bool) -> None:
    payload = bundle()
    revision = "rev+a/b="
    skill = {"skill_id": "skill/id", "name": "example", "revision": "rev-old", "latest_revision": revision}
    calls: list[httpx.Request] = []
    responses = [
        skill,
        {"skills": [skill], "next_page_token": "next+a/b="},
        skill,
        skill,
        {"revisions": [{"revision": revision}], "next_page_token": None},
        {"download_url": "https://example.test/bundle.zip", "revision": revision},
        None,
    ]
    methods = ["POST", "GET", "GET", "PUT", "GET", "GET", "DELETE"]
    paths = [
        "/v1/skills",
        "/v1/skills",
        "/v1/skills/skill%2Fid",
        "/v1/skills/skill%2Fid",
        "/v1/skills/skill%2Fid/revisions",
        "/v1/skills/skill%2Fid/download",
        "/v1/skills/skill%2Fid",
    ]
    queries = [
        {},
        {"limit": "20", "page_token": "next+a/b="},
        {},
        {"expected_revision": revision},
        {"limit": "20", "page_token": "next+a/b="},
        {"revision": revision},
        {"expected_revision": revision},
    ]

    def handler(request: httpx.Request) -> httpx.Response:
        index = len(calls)
        calls.append(request)
        assert request.method == methods[index]
        assert request.url.raw_path.split(b"?")[0].decode() == paths[index]
        assert dict(request.url.params) == queries[index]
        assert request.headers["authorization"] == "Bearer test"
        if request.method in {"POST", "PUT"}:
            content_type = request.headers["content-type"]
            assert content_type.startswith("multipart/form-data; boundary=")
            body = BytesParser(policy=policy.default).parsebytes(
                f"Content-Type: {content_type}\r\n\r\n".encode() + request.content
            )
            parts = list(body.iter_parts())
            assert len(parts) == 1
            assert parts[0].get_filename() == "bundle.zip"
            assert parts[0].get_content_type() == "application/zip"
            assert parts[0].get_payload(decode=True) == payload
        else:
            assert request.content == b""
        response = responses[index]
        return httpx.Response(204) if response is None else httpx.Response(200, json=response)

    if asynchronous:
        async with AsyncPerplexity(
            api_key="test",
            base_url="https://example.test",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
        ) as client:
            created = await client.skills.create(file=("bundle.zip", payload, "application/zip"))
            page = await client.skills.list(limit=20, page_token="next+a/b=")
            retrieved = await client.skills.retrieve(created.skill_id)
            assert retrieved.latest_revision is not None
            updated = await client.skills.update(
                created.skill_id,
                expected_revision=retrieved.latest_revision,
                file=("bundle.zip", payload, "application/zip"),
            )
            revisions = await client.skills.revisions.list(created.skill_id, limit=20, page_token="next+a/b=")
            download = await client.skills.download(created.skill_id, revision=retrieved.latest_revision)
            assert updated.latest_revision is not None
            deleted = await client.skills.delete(created.skill_id, expected_revision=updated.latest_revision)
    else:
        with Perplexity(
            api_key="test",
            base_url="https://example.test",
            http_client=httpx.Client(transport=httpx.MockTransport(handler)),
        ) as sync:
            created = sync.skills.create(file=("bundle.zip", payload, "application/zip"))
            page = sync.skills.list(limit=20, page_token="next+a/b=")
            retrieved = sync.skills.retrieve(created.skill_id)
            assert retrieved.latest_revision is not None
            updated = sync.skills.update(
                created.skill_id,
                expected_revision=retrieved.latest_revision,
                file=("bundle.zip", payload, "application/zip"),
            )
            revisions = sync.skills.revisions.list(created.skill_id, limit=20, page_token="next+a/b=")
            download = sync.skills.download(created.skill_id, revision=retrieved.latest_revision)
            assert updated.latest_revision is not None
            deleted = sync.skills.delete(created.skill_id, expected_revision=updated.latest_revision)
    assert isinstance(created, ManagedSkill)
    assert isinstance(retrieved, ManagedSkill)
    assert isinstance(updated, ManagedSkill)
    assert isinstance(page, SkillListResponse)
    assert page.skills[0].skill_id == created.skill_id
    assert page.next_page_token == "next+a/b="
    assert isinstance(revisions, SkillRevisionListResponse)
    assert isinstance(download, SkillDownloadResponse)
    assert download.revision == revision
    assert deleted is None
    assert len(calls) == 7


@pytest.mark.parametrize("identifier", ["", ".", ".."])
def test_path_parameters_reject_empty_and_dot_segments(identifier: str) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        raise AssertionError(f"unexpected request to {request.url}")

    with Perplexity(
        api_key="test",
        base_url="https://example.test",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    ) as client:
        with pytest.raises(ValueError, match="non-empty value|cannot be used as a path parameter"):
            client.skills.retrieve(identifier)
        with pytest.raises(ValueError, match="non-empty value|cannot be used as a path parameter"):
            client.skills.delete(identifier, expected_revision="rev")
        with pytest.raises(ValueError, match="non-empty value|cannot be used as a path parameter"):
            client.responses.retrieve(identifier)


@pytest.mark.parametrize("identifier", ["", ".", ".."])
def test_path_segment_guard_rejects_empty_and_dot_segments(identifier: str) -> None:
    from perplexity.generated.api import _path_segment

    with pytest.raises(ValueError, match="cannot be used as a path parameter"):
        _path_segment(identifier)
    assert _path_segment("a/../b") == "a%2F..%2Fb"


@pytest.mark.parametrize("identifier", [True, None, object()])
def test_path_segment_guard_rejects_non_string_values(identifier: object) -> None:
    from perplexity.generated.api import _path_segment

    with pytest.raises(TypeError, match="cannot be used as a path parameter"):
        _path_segment(identifier)
    assert _path_segment(7) == "7"
