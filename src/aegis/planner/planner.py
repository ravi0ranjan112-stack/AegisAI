from aegis.planner.context import AgentContext


class Planner:
    def create(self, goal: str) -> AgentContext:
        return AgentContext(goal=goal)
