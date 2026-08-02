from aegis.agents.registry import AgentRegistry


class AgentManager:
    def execute(self, command: str) -> str:
        return AgentRegistry().execute(command)
