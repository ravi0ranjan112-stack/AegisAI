from aegis.planner.planner import Planner


def test_create_plan():
    planner = Planner()

    context = planner.create("Run pytest")

    assert context.goal == "Run pytest"
    assert context.steps == []
    assert context.observations == []


def test_add_step():
    planner = Planner()

    context = planner.create("Goal")

    context.add_step("Run pytest")

    assert len(context.steps) == 1
    assert context.steps[0].description == "Run pytest"


def test_add_observation():
    planner = Planner()

    context = planner.create("Goal")

    context.add_observation(
        "shell",
        "pwd",
        "/home/user",
    )

    assert len(context.observations) == 1
    assert context.observations[0].tool == "shell"
