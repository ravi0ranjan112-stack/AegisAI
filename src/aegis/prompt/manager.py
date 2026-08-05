from aegis.prompt.builder import PromptBuilder


class PromptManager:
    def __init__(self) -> None:
        self.builder = PromptBuilder()

    def create(self, user_prompt: str) -> str:
        return self.builder.build(user_prompt)
