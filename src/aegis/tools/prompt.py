from aegis.prompts.manager import PromptManager
from aegis.tools.base import BaseTool


class PromptTool(BaseTool):
    @property
    def name(self) -> str:
        return "prompt"

    def run(self, command: str) -> str:
        return PromptManager().execute(command)
