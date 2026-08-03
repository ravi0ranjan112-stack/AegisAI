from aegis.planner.plan import Plan


class Planner:
    def create(self, goal: str) -> Plan:
        plan = Plan(goal)

        if goal != "Run pytest":
            plan.add(f"Analyze: {goal}")
            plan.add(f"Implement: {goal}")
            plan.add(f"Test: {goal}")

        return plan
