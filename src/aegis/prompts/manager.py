from aegis.prompts.library import PromptLibrary


class PromptManager:
    def execute(self, command: str) -> str:
        return PromptLibrary().execute(command)
