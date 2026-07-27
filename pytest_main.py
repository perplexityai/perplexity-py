import sys

import pytest

if __name__ == "__main__":
    raise SystemExit(pytest.main(["--tb=short", *sys.argv[1:]]))
