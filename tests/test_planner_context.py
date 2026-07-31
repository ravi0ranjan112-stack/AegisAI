from aegis.planner.planner import Planner


def test_context_records_observation():
    planner = Planner()

    context = planner.create("pwd")

    context.add_observation(
        tool="shell",
        command="pwd",
        result="/tmp",
    )

    assert len(context.observations) == 1
    obs = context.observations[0]
    assert obs.tool == "shell"
    assert obs.command == "pwd"
    assert obs.result == "/tmp"
