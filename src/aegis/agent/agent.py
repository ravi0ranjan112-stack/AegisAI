from aegis.agent.autonomous import AutonomousLoop
from aegis.agent.executor import AgentExecutor
from aegis.ai.manager import AIManager


class Agent:
    def __init__(
        self,
        ai: AIManager,
        executor: AgentExecutor,
    ) -> None:
        self._loop = AutonomousLoop(
            ai,
            executor,
        )

    def run(self, prompt: str) -> str:
        return self._loop.run(prompt).result
