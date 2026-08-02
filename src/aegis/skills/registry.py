from aegis.skills.skill import Skill


class SkillRegistry:
    def __init__(self) -> None:
        self._skills: dict[str, Skill] = {}

    def add(
        self,
        name: str,
        prompt: str,
    ) -> str:
        self._skills[name] = Skill(name, prompt)
        return "OK"

    def get(self, name: str) -> Skill | None:
        return self._skills.get(name)

    def names(self) -> str:
        return "\n".join(sorted(self._skills)) or "No skills"
