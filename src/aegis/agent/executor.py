from aegis.agent.parser import ToolCall
from aegis.tools.manager import ToolManager


class AgentExecutor:
    def __init__(self, tools: ToolManager) -> None:
        self._tools = tools

    def execute(self, call: ToolCall) -> str:
        return self._tools.execute(call.tool, call.command)
