from aegis.conversation.manager import ConversationManager


def test_conversation_manager():
    manager = ConversationManager()

    assert manager.execute("user hello") == "OK"
    assert manager.execute("assistant hi") == "OK"

    ctx = manager.execute("context")

    assert "user: hello" in ctx
    assert "assistant: hi" in ctx

    assert manager.execute("clear") == "OK"
