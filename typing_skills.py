"""Consumer type checks; no network requests are executed."""

from perplexity import Perplexity, AsyncPerplexity
from perplexity.types import ManagedSkill, SkillListResponse, SkillDownloadResponse, SkillRevisionListResponse


def synchronous(client: Perplexity, zip_bytes: bytes) -> None:
    skill: ManagedSkill = client.skills.create(file=("bundle.zip", zip_bytes, "application/zip"))
    page: SkillListResponse = client.skills.list(limit=20)
    skill = client.skills.retrieve(skill.skill_id)
    if skill.revision is None:
        raise ValueError("A current revision is required to update")
    skill = client.skills.update(
        skill.skill_id,
        expected_revision=skill.revision,
        file=("bundle.zip", zip_bytes, "application/zip"),
    )
    if skill.revision is None:
        raise ValueError("A current revision is required to delete")
    revisions: SkillRevisionListResponse = client.skills.revisions.list(skill.skill_id)
    download: SkillDownloadResponse = client.skills.download(skill.skill_id, revision=skill.revision)
    client.skills.delete(skill.skill_id, expected_revision=skill.revision)
    _ = (page, revisions, download)


async def asynchronous(client: AsyncPerplexity, data: bytes) -> None:
    created: ManagedSkill = await client.skills.create(file=("bundle.zip", data))
    if created.revision is None:
        raise ValueError("A current revision is required to update")
    created = await client.skills.update(created.skill_id, file=data, expected_revision=created.revision)
    if created.revision is None:
        raise ValueError("A current revision is required to delete")
    await client.skills.delete(created.skill_id, expected_revision=created.revision)
