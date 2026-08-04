from aegis.config.settings import Settings


class SettingsLoader:
    def __init__(self) -> None:
        self._settings = Settings()
        self._extra: dict[str, str] = {}

    def load(self) -> Settings:
        return self._settings


class ConfigLoader(SettingsLoader):
    def execute(self, command: str) -> str:
        parts = command.split()

        if len(parts) >= 3 and parts[0] == "set":
            key = parts[1]
            value = " ".join(parts[2:])

            if hasattr(self._settings, key):
                setattr(self._settings, key, value)
            else:
                self._extra[key] = value

            return "OK"

        if len(parts) == 2 and parts[0] == "get":
            key = parts[1]

            if hasattr(self._settings, key):
                return str(getattr(self._settings, key))

            return self._extra.get(key, "Unknown config")

        return "Unknown config"
