from aegis.tools.conversation import ConversationTool


def test_conversation_tool():
    tool = ConversationTool()

    assert tool.run("user hello") == "OK"
    assert tool.run("assistant hi") == "OK"

    ctx = tool.run("context")

    assert "user: hello" in ctx
    assert "assistant: hi" in ctx

    assert tool.run("clear") == "OK"
