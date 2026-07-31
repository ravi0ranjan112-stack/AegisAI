from aegis.agent.executor import AgentExecutor
from aegis.agent.parser import parse_tool_call


class AgentLoop:
    MAX_STEPS = 5

    def __init__(self, executor: AgentExecutor) -> None:
        self._executor = executor

    def run(self, response: str) -> tuple[bool, str]:
        current = response
        handled = False

        for _ in range(self.MAX_STEPS):
            call = parse_tool_call(current)

            if call is None:
                return handled, current

            handled = True
            current = self._executor.execute(call)

        return handled, current
