from aegis.chat.message import Message


def test_message() -> None:
    msg = Message("user", "Hello")

    assert msg.role == "user"
    assert msg.content == "Hello"
