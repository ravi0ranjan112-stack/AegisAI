from aegis.agents.manager import AgentManager


class AgentExecutor:
    def execute(self, command: str) -> str:
        return AgentManager().execute(command)
