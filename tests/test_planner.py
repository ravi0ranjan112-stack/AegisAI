from aegis.planner.engine import PlannerEngine


def test_planner():
    planner = PlannerEngine()

    plan = planner.create_plan("Build calculator app")

    assert plan.goal == "Build calculator app"
    assert len(plan.tasks) == 6
    assert plan.tasks[0].title == "Analyze request"
