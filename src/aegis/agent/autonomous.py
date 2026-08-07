from aegis.agent.executor import AgentExecutor
from aegis.agent.history import AgentHistory
from aegis.agent.parser import parse_tool_call
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
        self.memory.add("last_task", goal)

        plan = self.planner.create(goal)

        history = AgentHistory()
        history.add(goal)

        response = self.ai.ask(goal)
        call = parse_tool_call(response)

        if call is not None:
            tool_result = self.executor.execute(call)
            history.add(tool_result)
            return LoopResult(
                handled=True,
                result=tool_result,
                history=history,
            )

        return LoopResult(
            handled=True,
            result="\n".join(step.description for step in plan.steps),
            history=history,
        )
