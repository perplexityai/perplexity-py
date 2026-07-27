import os

from mypy.__main__ import console_entry

workspace = os.environ.get("BUILD_WORKSPACE_DIRECTORY")
if workspace:
    os.chdir(workspace)

raise SystemExit(console_entry())
