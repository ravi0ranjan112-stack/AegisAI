from unittest.mock import Mock, patch

from aegis.chat.engine import ChatEngine


def test_chat_engine() -> None:
    fake = Mock()
    fake.raise_for_status.return_value = None
    fake.json.return_value = {"response": "Hi there"}

    with patch("httpx.post", return_value=fake):
        engine = ChatEngine()

        reply = engine.chat("Hello")

        assert reply == "Hi there"
        assert len(engine.session.messages) == 2
        assert engine.session.messages[0].content == "Hello"
        assert engine.session.messages[1].content == "Hi there"
