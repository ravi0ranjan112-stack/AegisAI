from aegis.conversation.session import ConversationSession


def test_conversation_session():
    session = ConversationSession()

    session.add("user", "hello")
    session.add("assistant", "hi")

    msgs = session.all()

    assert len(msgs) == 2
    assert msgs[0].content == "hello"

    session.clear()
    assert session.all() == []
