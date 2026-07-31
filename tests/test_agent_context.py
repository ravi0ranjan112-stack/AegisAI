from aegis.planner.planner import Planner


def test_context_goal():
    planner = Planner()

    context = planner.create("Run pytest")

    assert context.goal == "Run pytest"
    assert context.steps == []
    assert context.observations == []
