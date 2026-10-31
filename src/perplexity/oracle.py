"""Dependency-free tarot-style readings with an optional audio renderer."""

from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Callable

__all__ = ["OracleCard", "OracleReading", "TarotOracle"]


@dataclass(frozen=True)
class OracleCard:
    name: str
    meaning: str


@dataclass(frozen=True)
class OracleReading:
    question: str
    cards: tuple[OracleCard, ...]

    @property
    def text(self) -> str:
        lines = [f"Reading for: {self.question}"]
        for position, card in zip(("Past", "Present", "Future"), self.cards):
            lines.append(f"{position}: {card.name} - {card.meaning}")
        return "\n".join(lines)

    def render_audio(self, renderer: Callable[[str], bytes]) -> bytes:
        """Render this reading with a caller-provided text-to-speech function."""
        return renderer(self.text)


class TarotOracle:
    """Draw a three-card, past/present/future tarot-style reading."""

    _cards: tuple[OracleCard, ...] = (
        OracleCard("The Star", "hope, renewal, and a clear direction forward"),
        OracleCard("The Sun", "confidence, warmth, and an outcome becoming visible"),
        OracleCard("The Hermit", "reflection, patience, and insight found within"),
        OracleCard("The Chariot", "focused movement, discipline, and determined progress"),
        OracleCard("Justice", "honest choices, balance, and consequences settling"),
        OracleCard("The Moon", "uncertainty, intuition, and facts still coming into focus"),
        OracleCard("The Tower", "a sudden change that clears away an unstable foundation"),
        OracleCard("The World", "completion, integration, and a cycle reaching its result"),
    )

    def __init__(self, *, seed: int | None = None) -> None:
        self._random = random.Random(seed)

    def read(self, question: str) -> OracleReading:
        """Return a reading, raising ``ValueError`` for an empty question."""
        question = question.strip()
        if not question:
            raise ValueError("question must not be empty")
        return OracleReading(question, tuple(self._random.sample(self._cards, k=3)))
