from aegis.commands.engine import CommandEngine


def test_command_engine():
    engine = CommandEngine()

    command = engine.parse("Create calculator app")

    assert command.text == "Create calculator app"
