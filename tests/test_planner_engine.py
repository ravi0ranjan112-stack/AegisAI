from aegis.planner.engine import PlannerEngine


def test_planner() -> None:
    planner = PlannerEngine()

    plan = planner.create("Build AI")

    assert plan.goal == "Build AI"
    assert len(plan.steps) > 0
    assert plan.steps[0].id == 1
    assert plan.steps[0].description != ""
