from aegis.project.analyzer import ProjectAnalyzer
from aegis.tools.base import BaseTool


class ProjectTool(BaseTool):
    @property
    def name(self) -> str:
        return "project"

    def run(self, command: str) -> str:
        analyzer = ProjectAnalyzer()

        if command.strip() in {
            "",
            "summary",
        }:
            return analyzer.summary()

        return "Unknown command."
