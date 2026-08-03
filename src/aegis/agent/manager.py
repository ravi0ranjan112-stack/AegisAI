from aegis.agent.loop import AgentLoop


class AgentManager:
    def __init__(self) -> None:
        self._loop = AgentLoop()

    def execute(self, goal: str):
        return self._loop.run(goal, steps=3)
