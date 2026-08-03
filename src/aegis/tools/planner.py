from aegis.planner.manager import PlannerManager
from aegis.tools.base import BaseTool


class PlannerTool(BaseTool):
    @property
    def name(self) -> str:
        return "planner"

    def __init__(self) -> None:
        self._manager = PlannerManager()

    def run(self, command: str):
        return self._manager.execute(command)
