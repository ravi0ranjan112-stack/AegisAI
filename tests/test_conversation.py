from aegis.conversation.session import ConversationSession


def test_conversation():
    session = ConversationSession()

    session.add_user("Hello")
    session.add_assistant("Hi!")

    assert len(session.messages) == 2
    assert session.messages[0].role == "user"
    assert session.messages[1].role == "assistant"

    session.clear()

    assert len(session.messages) == 0
