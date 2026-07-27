import re
import sys
from pathlib import Path

CONVENTIONAL_COMMIT = re.compile(
    r"^(build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)"
    r"(\([^)]+\))?!?: \S.+$"
)


def valid_subject(subject: str) -> bool:
    return bool(CONVENTIONAL_COMMIT.fullmatch(subject)) or subject.startswith(("Merge ", "Revert "))


def main() -> int:
    message = Path(sys.argv[1]).read_text()
    subject = message.splitlines()[0] if message else ""
    if valid_subject(subject):
        return 0
    sys.stderr.write(f"invalid conventional commit: {subject!r}\n")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
