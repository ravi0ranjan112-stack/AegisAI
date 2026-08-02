from aegis.agent.executor import AgentExecutor
from aegis.agent.history import AgentHistory
from aegis.agent.result import LoopResult
from aegis.ai.manager import AIManager
from aegis.memory.store import MemoryStore
from aegis.planner.engine import PlannerEngine


class AutonomousLoop:
    def __init__(
        self,
        ai: AIManager,
        executor: AgentExecutor,
    ) -> None:
        self.ai = ai
        self.executor = executor
        self.memory = MemoryStore()
        self.planner = PlannerEngine()

    def run(self, goal: str) -> LoopResult:
        self.memory.add(goal)

        history = AgentHistory()
        history.add(goal)

        plan = self.planner.create(goal)

        return LoopResult(
            handled=True,
            result="\n".join(plan.steps),
            history=history,
        )
