from aegis.tasks.manager import TaskManager
from aegis.tools.base import BaseTool


class TaskTool(BaseTool):
    @property
    def name(self) -> str:
        return "task"

    def run(self, command: str) -> str:
        return TaskManager().execute(command)
