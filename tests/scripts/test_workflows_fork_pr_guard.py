"""This repository's workflows never run fork PR code on the self-hosted fleet (RM#1989)."""

from __future__ import annotations

from pathlib import Path

import pytest

from scripts import fork_pr_runner_guard as guard

pytestmark = pytest.mark.unit

WORKFLOWS = Path(__file__).resolve().parents[2] / ".github" / "workflows"

GUARDED_IF = (
    "(!github.event.pull_request || " "github.event.pull_request.head.repo.full_name == github.repository)"
)


def test_real_workflows_have_no_fork_pr_findings() -> None:
    assert guard.find_violations(WORKFLOWS) == []


def test_anti_phantom_guard_if_is_exactly_the_guarded_condition() -> None:
    import yaml

    data = yaml.safe_load((WORKFLOWS / "anti-phantom-merge.yml").read_text("utf-8"))
    condition = " ".join(str(data["jobs"]["guard"]["if"]).split())
    assert condition == (
        f"{GUARDED_IF} && "
        "((github.event.pull_request.base.ref == 'main' && "
        "(github.event_name == 'pull_request' || "
        "github.event.label.name == 'phantom-guard-override')) || "
        "github.event.pull_request.base.ref == 'master')"
    )
