import pytest

from perplexity import TarotOracle


def test_oracle_returns_a_reading() -> None:
    reading = TarotOracle(seed=7).read("What should I focus on?")

    assert len(reading.cards) == 3
    assert reading.text.startswith("Reading for: What should I focus on?")
    assert "Past:" in reading.text
    assert "Present:" in reading.text
    assert "Future:" in reading.text


def test_oracle_is_reproducible_with_a_seed() -> None:
    assert TarotOracle(seed=3).read("Question").text == TarotOracle(seed=3).read("Question").text


def test_oracle_audio_hook_receives_the_reading() -> None:
    reading = TarotOracle(seed=1).read("Question")

    assert reading.render_audio(lambda text: text.encode("utf-8")) == reading.text.encode("utf-8")


def test_oracle_rejects_empty_questions() -> None:
    with pytest.raises(ValueError, match="question must not be empty"):
        TarotOracle().read("  ")
