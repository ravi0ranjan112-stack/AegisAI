from aegis.agent.executor import AgentExecutor
from aegis.agent.loop import AgentLoop
from aegis.ai.manager import AIManager
from aegis.planner.planner import Planner


class Agent:
    def __init__(
        self,
        ai: AIManager,
        executor: AgentExecutor,
    ) -> None:
        self._ai = ai
        self._planner = Planner()
        self._loop = AgentLoop(executor)

    def run(self, prompt: str) -> str:
        context = self._planner.create(prompt)

        response = self._ai.ask(prompt)

        handled, result = self._loop.run(response)

        if handled:
            context.add_observation(
                tool="agent",
                command=prompt,
                result=result,
            )

            follow_up = (
                f"Original request:\n{prompt}\n\n"
                f"Tool result:\n{result}\n\n"
                "Answer the original request."
            )

            return self._ai.ask(follow_up)

        return result
