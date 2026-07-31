from aegis.agent.executor import AgentExecutor
from aegis.agent.parser import parse_tool_call


class AgentLoop:
    MAX_STEPS = 5

    def __init__(self, executor: AgentExecutor) -> None:
        self._executor = executor

    def handle(self, response: str) -> tuple[bool, str]:
        tool_call = parse_tool_call(response)

        if tool_call is None:
            return False, response

        result = self._executor.execute(tool_call)

        return True, result
