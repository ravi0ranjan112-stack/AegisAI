from aegis.planner.planner import Planner


def test_planner() -> None:
    planner = Planner()

    plan = planner.create("Build AI")

    assert plan.goal == "Build AI"
    assert len(plan.steps) == 3
    assert plan.steps[0].id == 1
