from aegis.plugins.loader import PluginLoader

_PLUGINS: dict[str, bool] = {}


class PluginManager:
    def __init__(self) -> None:
        self._plugins = _PLUGINS

    def execute(self, command: str) -> str:
        action, _, value = command.partition(" ")

        if action == "load":
            self._plugins[value] = PluginLoader().load(value).enabled
            return "OK"

        if action == "list":
            return "\n".join(sorted(self._plugins)) or "No plugins"

        if action == "status":
            return str(self._plugins.get(value, False))

        return "Usage: load|list|status"
