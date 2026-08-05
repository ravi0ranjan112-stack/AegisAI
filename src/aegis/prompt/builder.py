from aegis.prompt.system import SystemPrompt


class PromptBuilder:
    def __init__(self) -> None:
        self.system = SystemPrompt()

    def build(self, user_prompt: str) -> str:
        return f"{self.system.text}\n\nUser: {user_prompt}"
