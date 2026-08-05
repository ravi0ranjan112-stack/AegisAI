from aegis.llm.ollama import OllamaProvider


def test_ollama() -> None:
    provider = OllamaProvider()

    assert provider.generate("hi") == "Ollama: hi"
