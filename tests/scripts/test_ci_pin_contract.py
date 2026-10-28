"""Tests verifying CI dependency pin contract compliance (#169)."""

from pathlib import Path


def test_dev_requirements_pins_pytest_below_92() -> None:
    """Verify that dev-requirements.txt pins pytest <9.2.0 to protect pytest-benchmark."""
    dev_req_path = Path(__file__).resolve().parents[2] / "dev-requirements.txt"
    content = dev_req_path.read_text(encoding="utf-8")
    assert (
        "<9.2" in content or "<9.2.0" in content
    ), "pytest must be pinned <9.2.0 in dev-requirements.txt to prevent pytest-benchmark Function._nodeid AttributeError"
