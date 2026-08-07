from aegis.agent.context import AgentContext
from aegis.agent.parser import parse_tool_call


class AgentLoop:
    def __init__(self, llm=None, tools=None) -> None:
        self._llm = llm
        self._tools = tools

    def run(self, goal: str, steps: int = 1) -> AgentContext:
        ctx = AgentContext(goal)

        ctx.state.running = True

        for _ in range(steps):
            if ctx.state.finished:
                break

            if self._llm is not None and self._tools is not None:
                response = self._llm.ask(goal)
                call = parse_tool_call(response)

                if call is not None:
                    self._tools.execute(call.tool, call.command)

            ctx.state.next_step()

        ctx.state.completed = True
        ctx.state.running = False
        return ctx
