from aegis.tools.base import BaseTool
from aegis.workflow.pipeline import Pipeline


class WorkflowTool(BaseTool):
    @property
    def name(self) -> str:
        return "workflow"

    def run(self, command: str) -> str:
        return Pipeline().run(command)
