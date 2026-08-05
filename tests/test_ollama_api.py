from unittest.mock import Mock, patch

from aegis.llm.ollama import OllamaProvider


def test_ollama_api() -> None:
    fake = Mock()
    fake.raise_for_status.return_value = None
    fake.json.return_value = {"response": "Hello from Ollama"}

    with patch("httpx.post", return_value=fake):
        provider = OllamaProvider()
        assert provider.generate("Hi") == "Hello from Ollama"
