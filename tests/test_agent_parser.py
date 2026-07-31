from aegis.agent.parser import parse_tool_call


def test_parse_shell():
    result = parse_tool_call(
        """
Hello

<tool:shell>
pwd
</tool>
"""
    )

    assert result is not None
    assert result.tool == "shell"
    assert result.command == "pwd"


def test_parse_none():
    assert parse_tool_call("Hello world") is None
