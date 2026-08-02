from aegis.agents.executor import AgentExecutor
from aegis.tools.base import BaseTool


class AgentTool(BaseTool):
    @property
    def name(self) -> str:
        return "agent"

    def run(self, command: str) -> str:
        return AgentExecutor().execute(command)
