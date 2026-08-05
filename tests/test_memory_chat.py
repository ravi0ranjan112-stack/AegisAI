from unittest.mock import Mock, patch

from aegis.chat.memory_chat import MemoryChat


def test_memory_chat() -> None:
    fake = Mock()
    fake.raise_for_status.return_value = None
    fake.json.return_value = {"response": "Hello back"}

    with patch("httpx.post", return_value=fake):
        chat = MemoryChat()

        reply = chat.ask("Hello")

        assert reply == "Hello back"
        assert len(chat.history) == 2
        assert chat.history[0].role == "user"
        assert chat.history[1].role == "assistant"
