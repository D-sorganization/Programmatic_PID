from __future__ import annotations

import builtins
from pathlib import Path
from typing import Any

import programmatic_pid.generator as mod

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "examples" / "biochar" / "biochar_pid_spec.yml"


def test_generate_two_sheet_outputs(tmp_path: Path) -> None:
    out_dxf = tmp_path / "pid.dxf"
    out_svg = tmp_path / "pid.svg"

    mod.generate(str(SPEC_PATH), str(out_dxf), str(out_svg), sheet_set="two", profile="presentation")

    assert out_dxf.exists()
    assert out_svg.exists()
    assert (tmp_path / "pid_controls.dxf").exists()
    assert (tmp_path / "pid_controls.svg").exists()


def test_two_sheet_svg_generation_is_headless_without_qt(tmp_path: Path, monkeypatch: Any) -> None:
    original_import = builtins.__import__

    def reject_qt_import(name: str, *args: Any, **kwargs: Any) -> Any:
        if name.startswith(("PySide6", "PyQt6")):
            raise AssertionError(f"unexpected Qt import: {name}")
        return original_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", reject_qt_import)

    out_dxf = tmp_path / "headless.dxf"
    out_svg = tmp_path / "headless.svg"

    mod.generate(str(SPEC_PATH), str(out_dxf), str(out_svg), sheet_set="two", profile="presentation")

    assert out_dxf.stat().st_size > 0
    assert out_svg.stat().st_size > 0
    assert (tmp_path / "headless_controls.dxf").stat().st_size > 0
    assert (tmp_path / "headless_controls.svg").stat().st_size > 0
