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


def test_runtime_dependencies_do_not_install_qt_draw_extras() -> None:
    requirements = Path("requirements.txt").read_text(encoding="utf-8")
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))

    assert "ezdxf[draw]" not in requirements
    assert "ezdxf[draw]" not in pyproject["project"]["dependencies"]
    assert "ezdxf>=1.4.3" in requirements
    assert "ezdxf>=1.4.3" in pyproject["project"]["dependencies"]
    assert "Pillow>=10.0" in requirements
    assert "Pillow>=10.0" in pyproject["project"]["dependencies"]


def test_nightly_workflow_retries_installs_and_deduplicates_failure_issues() -> None:
    workflow = Path(".github/workflows/nightly.yml").read_text(encoding="utf-8")

    assert 'PIP_DEFAULT_TIMEOUT: "120"' in workflow
    assert 'PIP_RETRIES: "5"' in workflow
    assert "labels: labels.join" in workflow
    assert "issues.listForRepo" in workflow
    assert "issues.createComment" in workflow
    assert "issues.create({" in workflow
    assert "Run ID:" in workflow and "context.runId" in workflow
    assert "Commit:" in workflow and "context.sha" in workflow
    assert "Runner:" in workflow and "RUNNER_NAME" in workflow
    assert "Failing step: `nightly-tests`" in workflow
    assert "Signature:" in workflow and "normalizedSignature" in workflow
