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

        handled, result = self._loop.run(response)

        if not handled:
            return result

        follow_up = (
            f"Original user request:\n{prompt}\n\n"
            f"Tool result:\n{result}\n\n"
            "Answer the original request using the tool result."
        )

        return self._ai.ask(follow_up)
