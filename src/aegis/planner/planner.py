from aegis.planner.context import PlannerContext


class Planner:
    def create(self, goal: str) -> PlannerContext:
        return PlannerContext(goal=goal)
