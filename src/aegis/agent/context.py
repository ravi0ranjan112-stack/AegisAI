from aegis.agent.state import AgentState


class AgentContext:
    def __init__(self, goal: str) -> None:
        self.state = AgentState(goal=goal)

    @property
    def goal(self) -> str:
        return self.state.goal
