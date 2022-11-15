import os
import sys
from pathlib import Path

notebook_cwd = Path(os.getcwd())
workspace_cwd = notebook_cwd.parent
if workspace_cwd not in sys.path:
    sys.path.append(str(workspace_cwd))