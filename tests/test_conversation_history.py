from aegis.conversation.history import ConversationHistory
from aegis.conversation.session import ConversationSession


def test_conversation_history():
    session = ConversationSession()

    session.add_user("hello")
    session.add_assistant("hi")
    session.add_user("how are you?")

    history = ConversationHistory(session)

    assert len(history.last(2)) == 2
    assert "hello" in history.text()
    assert "assistant: hi" in history.text()
