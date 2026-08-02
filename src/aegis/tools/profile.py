from aegis.profiles.manager import ProfileManager
from aegis.tools.base import BaseTool


class ProfileTool(BaseTool):
    @property
    def name(self) -> str:
        return "profile"

    def run(self, command: str) -> str:
        return ProfileManager().execute(command)
