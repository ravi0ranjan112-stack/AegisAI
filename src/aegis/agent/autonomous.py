from aegis.agent.executor import AgentExecutor
from aegis.agent.history import AgentHistory
from aegis.agent.parser import parse_tool_call
from aegis.agent.result import LoopResult
from aegis.agent.state import AgentState
from aegis.ai.autonomous_prompt import AUTONOMOUS_AGENT_PROMPT
from aegis.ai.manager import AIManager


class AutonomousLoop:
    def __init__(
        self,
        ai: AIManager,
        executor: AgentExecutor,
        max_steps: int = 5,
    ) -> None:
        self._ai = ai
        self._executor = executor
        self._max_steps = max_steps

    def run(self, prompt: str) -> LoopResult:
        state = AgentState(max_steps=self._max_steps)
        history = AgentHistory()

        current = prompt
        handled = False

        while not state.finished:
            state.next_step()

            response = self._ai.ask(
                current,
                system_prompt=AUTONOMOUS_AGENT_PROMPT,
            )

            call = parse_tool_call(response)

            if call is None:
                return LoopResult(
                    handled=handled,
                    result=response,
                    history=history,
                )

            handled = True

            result = self._executor.execute(call)

            history.add(f"Tool: {call.tool}")
            history.add(f"Command: {call.command}")
            history.add(f"Result:\n{result}")

            current = (
                f"Original request:\n{prompt}\n\n"
                f"{history.render()}\n\n"
                "Continue. If another tool is required output exactly one tool call. "
                "Otherwise answer the original request."
            )

        return LoopResult(
            handled=True,
            result="Maximum tool steps reached.",
            history=history,
        )
