from aegis.chat.session import ChatSession


def test_session() -> None:
    session = ChatSession()

    session.add("user", "Hello")
    session.add("assistant", "Hi")

    assert len(session.messages) == 2
    assert session.messages[0].content == "Hello"
    assert session.messages[1].content == "Hi"
