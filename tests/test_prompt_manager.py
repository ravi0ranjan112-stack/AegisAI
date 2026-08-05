from aegis.prompt.manager import PromptManager


def test_prompt_manager() -> None:
    manager = PromptManager()

    prompt = manager.create("Explain Python")

    assert "You are Aegis AI." in prompt
    assert "User: Explain Python" in prompt
