from aegis.agent.parser import parse_tool_call


def test_xml():
    call = parse_tool_call("<tool:shell>\npwd\n</tool>")
    assert call
    assert call.tool == "shell"
    assert call.command == "pwd"


def test_plain():
    call = parse_tool_call("pwd")
    assert call
    assert call.tool == "shell"
    assert call.command == "pwd"


def test_git():
    call = parse_tool_call("git status")
    assert call
    assert call.command == "git status"


def test_codeblock():
    call = parse_tool_call("```bash\npwd\n```")
    assert call
    assert call.command == "pwd"


def test_none():
    assert parse_tool_call("Hello world") is None
