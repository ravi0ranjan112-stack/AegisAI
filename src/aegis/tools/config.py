from aegis.config.loader import ConfigLoader
from aegis.tools.base import BaseTool


class ConfigTool(BaseTool):
    @property
    def name(self) -> str:
        return "config"

    def run(self, command: str) -> str:
        return ConfigLoader().execute(command)
