from aegis.planner.plan import Plan


class PlannerEngine:
    def create(self, goal: str) -> Plan:
        plan = Plan(goal)
        plan.add(goal)
        return plan
