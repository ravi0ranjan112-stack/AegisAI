from aegis.planner.engine import PlannerEngine


def test_create_plan() -> None:
    plan = PlannerEngine().create("Build AI")
    assert plan.goal == "Build AI"
    assert plan.steps == ["Build AI"]
