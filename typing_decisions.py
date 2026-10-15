from perplexity import Perplexity, AsyncPerplexity
from perplexity.types import DecisionCreateResponse


def decisions(client: Perplexity) -> DecisionCreateResponse:
    return client.decisions.create(
        model="pplx-decider-v1.1-27b",
        state={"review": "The battery stopped charging."},
        questions={
            "defect": {"type": "noul", "instructions": "Does this report a defect?"},
            "sentiment": {"type": "choice", "criteria": {"positive": None, "negative": "Dissatisfied"}},
            "severity": {"type": "score", "criteria": ["Cosmetic", {"description": "Unusable"}]},
        },
    )


async def async_decisions(client: AsyncPerplexity) -> DecisionCreateResponse:
    return await client.decisions.create(
        model="pplx-decider-v1.1-27b",
        state="The battery stopped charging.",
        questions={"defect": {"type": "noul", "criteria": {"true": "Broken", "false": None}}},
    )
