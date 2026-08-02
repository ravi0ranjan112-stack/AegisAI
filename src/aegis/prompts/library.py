from aegis.prompts.store import PromptStore


class PromptLibrary:
    def execute(self, command: str) -> str:
        return PromptStore().execute(command)
