from aegis.agent.executor import AgentExecutor
from aegis.agent.history import AgentHistory
from aegis.agent.parser import parse_tool_call
from aegis.agent.state import AgentState


class AgentLoop:
    def __init__(
        self,
        executor: AgentExecutor,
        max_steps: int = 5,
    ) -> None:
        self._executor = executor
        self._max_steps = max_steps

    def run(self, response: str) -> tuple[bool, str, AgentHistory]:
        state = AgentState(max_steps=self._max_steps)
        history = AgentHistory()

        current = response
        handled = False

        while not state.finished:
            call = parse_tool_call(current)

            if call is None:
                return handled, current, history

            handled = True
            state.next_step()

            result = self._executor.execute(call)

            history.add(f"Tool: {call.tool}")
            history.add(f"Command: {call.command}")
            history.add(f"Result:\n{result}")

            current = result

        return handled, current, history
