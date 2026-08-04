from aegis.config.loader import ConfigLoader
from aegis.tools.base import BaseTool


class ConfigTool(BaseTool):
    def __init__(self) -> None:
        self._loader = ConfigLoader()

    @property
    def name(self) -> str:
        return "config"

    def run(self, command: str) -> str:
        return self._loader.execute(command)
