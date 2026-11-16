"""The vendored GAAI framework is gone and must not come back.

The owner retired GAAI fleet-wide (Repository_Management#2725). The checked-in
``.gaai/`` tree, daemon launchers, and GAAI slash-commands are removed; these
checks keep them, and live pointers to them, from returning.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

import pytest

pytestmark = pytest.mark.unit

REPO_ROOT = Path(__file__).resolve().parents[1]

LIVE_ENTRY_POINTS = (
    'CLAUDE.md',
    'AGENTS.md',
    'README.md',
)

_GAAI = re.compile(r"gaai", re.IGNORECASE)


def test_vendored_tree_is_removed() -> None:
    assert not (REPO_ROOT / ".gaai").exists()


def test_daemon_launcher_is_removed() -> None:
    assert not (REPO_ROOT / "start-gaai-daemon.sh").exists()
    assert not (REPO_ROOT / "scripts" / "maintenance" / "start-gaai-daemon.sh").exists()
    assert not (REPO_ROOT / "gaai-fleet").exists()


def _tracked_files() -> list[str]:
    return subprocess.run(
        ["git", "ls-files"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.splitlines()


def test_no_tracked_gaai_launcher_or_slash_command() -> None:
    this_file = Path(__file__).resolve().relative_to(REPO_ROOT).as_posix()
    found = [
        path
        for path in _tracked_files()
        if path != this_file
        and (
            path.startswith(".gaai/")
            or path == ".gaai"
            or Path(path).name.startswith("gaai-")
            or Path(path).name.startswith("start-gaai")
            or path.startswith("gaai-fleet/")
        )
    ]
    assert found == []


@pytest.mark.parametrize("relative_path", LIVE_ENTRY_POINTS)
def test_live_entry_point_does_not_mention_gaai(relative_path: str) -> None:
    path = REPO_ROOT / relative_path
    if not path.is_file():
        pytest.skip(f"{relative_path} is not present in this repo")
    hits = [
        f"{relative_path}:{number}"
        for number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), start=1
        )
        if _GAAI.search(line)
    ]
    assert hits == []
