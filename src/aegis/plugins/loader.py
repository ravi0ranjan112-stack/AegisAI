from aegis.plugins.plugin import Plugin


class PluginLoader:
    def load(self, name: str) -> Plugin:
        return Plugin(name)
