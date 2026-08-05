from aegis.prompt.system import SystemPrompt


def test_system_prompt() -> None:
    prompt = SystemPrompt()

    assert prompt.text == "You are Aegis AI."
