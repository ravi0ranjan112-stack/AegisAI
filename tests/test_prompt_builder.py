from aegis.prompt.builder import PromptBuilder


def test_prompt_builder() -> None:
    builder = PromptBuilder()

    prompt = builder.build("Hello")

    assert "You are Aegis AI." in prompt
    assert "User: Hello" in prompt
