import os
import sys
from pathlib import Path

workspace = os.environ.get("BUILD_WORKSPACE_DIRECTORY")
if workspace:
    os.chdir(workspace)

runfiles = Path(os.environ.get("RUNFILES_DIR", Path(__file__).parent.parent))
ruff = next(runfiles.glob("rules_python++pip+pip_*_ruff_*/bin/ruff*"))
os.execv(ruff, [ruff.name, *sys.argv[1:]])
