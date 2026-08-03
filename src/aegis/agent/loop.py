from aegis.agent.context import AgentContext


class AgentLoop:
    def run(self, goal: str, steps: int = 1) -> AgentContext:
        ctx = AgentContext(goal)

        ctx.state.running = True

        for _ in range(steps):
            if ctx.state.finished:
                break
            ctx.state.next_step()

        ctx.state.completed = True
        ctx.state.running = False
        return ctx
