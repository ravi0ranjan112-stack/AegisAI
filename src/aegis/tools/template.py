from aegis.templates.manager import TemplateManager
from aegis.tools.base import BaseTool


class TemplateTool(BaseTool):
    @property
    def name(self) -> str:
        return "template"

    def run(self, command: str) -> str:
        return TemplateManager().execute(command)
