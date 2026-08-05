from aegis.llm.manager import LLMManager


def test_llm_manager() -> None:
    manager = LLMManager()

    assert manager.ask("Hello") == "Ollama: Hello"
