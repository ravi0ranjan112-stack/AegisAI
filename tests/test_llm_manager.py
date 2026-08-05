from unittest.mock import Mock, patch

from aegis.llm.manager import LLMManager


def test_llm_manager() -> None:
    fake = Mock()
    fake.raise_for_status.return_value = None
    fake.json.return_value = {"response": "Ollama: Hello"}

    with patch("httpx.post", return_value=fake):
        manager = LLMManager()
        assert manager.ask("Hello") == "Ollama: Hello"
