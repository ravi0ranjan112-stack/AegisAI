from aegis.skills.manager import SkillManager
from aegis.tools.base import BaseTool


class SkillTool(BaseTool):
    @property
    def name(self) -> str:
        return "skill"

    def run(self, command: str) -> str:
        return SkillManager().execute(command)
