from aegis.tools.planner import PlannerTool


def test_planner_tool() -> None:
    tool = PlannerTool()

    plan = tool.run("Build AI")

    assert plan.goal == "Build AI"
    assert len(plan.steps) == 3
