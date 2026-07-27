import os
import sys
from pathlib import Path

from mypy.__main__ import console_entry

if __name__ == "__main__":
    workspace = Path(__file__).resolve().parent
    os.chdir(workspace)
    sys.argv[1:1] = ["--cache-dir", os.environ["TEST_TMPDIR"]]
    console_entry()
