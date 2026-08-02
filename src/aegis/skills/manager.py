from aegis.skills.registry import SkillRegistry

_REGISTRY = SkillRegistry()


class SkillManager:
    def execute(self, command: str) -> str:
        action, _, rest = command.partition(" ")

        if action == "add":
            name, _, prompt = rest.partition(" ")
            return _REGISTRY.add(name, prompt)

        if action == "show":
            skill = _REGISTRY.get(rest)
            return skill.prompt if skill else "Not found"

        if action == "list":
            return _REGISTRY.names()

        return "Usage: add|show|list"
