from aegis.planner.models import Plan, Task


class PlannerEngine:
    def create_plan(self, goal: str) -> Plan:
        tasks = [
            Task(1, "Analyze request"),
            Task(2, "Create workspace"),
            Task(3, "Generate source code"),
            Task(4, "Run tests"),
            Task(5, "Fix detected issues"),
            Task(6, "Generate final report"),
        ]

        return Plan(goal=goal, tasks=tasks)
