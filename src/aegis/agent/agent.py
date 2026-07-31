from aegis.agent.executor import AgentExecutor
from aegis.agent.loop import AgentLoop
from aegis.ai.manager import AIManager


class Agent:
    def __init__(
        self,
        ai: AIManager,
        executor: AgentExecutor,
    ) -> None:
        self._ai = ai
        self._loop = AgentLoop(executor)

    def run(self, prompt: str) -> str:
        response = self._ai.ask(prompt)

        handled, result = self._loop.handle(response)

        if handled:
            return result

        return response
