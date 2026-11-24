from pathlib import Path

import os
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def run(*args, code=0):
    script = next(ROOT.glob("*.py"))
    result = subprocess.run(
        [sys.executable, "-B", str(script), *map(str, args)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=dict(os.environ, PYTHONUTF8="1"),
    )
    assert result.returncode == code, result.stderr
    return result.stdout


with tempfile.TemporaryDirectory() as temp:
    base = Path(temp)
    assert "GuestB -> GuestA: 20.00" in run("GuestA=90", "GuestB=15", "GuestC=0")
