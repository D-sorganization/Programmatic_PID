from __future__ import annotations

import tomllib
from pathlib import Path


def test_pytest_config_does_not_require_undeclared_plugins() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))
    pytest_options = pyproject["tool"]["pytest"]["ini_options"]
    dev_dependencies = set(pyproject["project"]["optional-dependencies"]["dev"])

    assert "asyncio_mode" not in pytest_options
    assert "asyncio_default_fixture_loop_scope" not in pytest_options
    assert not any(dependency.startswith("pytest-asyncio") for dependency in dev_dependencies)


def test_ci_security_tool_is_declared_in_dev_requirements() -> None:
    dev_requirements = Path("dev-requirements.txt").read_text(encoding="utf-8").splitlines()

    assert any(requirement.startswith("pip-audit") for requirement in dev_requirements)
