from aegis.agents.profile import AgentProfile

_AGENTS: dict[str, AgentProfile] = {}


class AgentRegistry:
    def execute(self, command: str) -> str:
        action, _, rest = command.partition(" ")

        if action == "add":
            name, _, prompt = rest.partition(" ")
            _AGENTS[name] = AgentProfile(name, prompt)
            return "OK"

        if action == "show":
            agent = _AGENTS.get(rest)
            return agent.system_prompt if agent else "Not found"

        if action == "list":
            return "\n".join(sorted(_AGENTS)) or "Empty"

        return "Usage: add|show|list"
