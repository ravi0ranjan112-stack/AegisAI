from aegis.runtime.session import RuntimeSession

_RUNTIME = RuntimeSession()


class Runtime:
    def execute(self, command: str) -> str:
        action, _, rest = command.partition(" ")

        if action == "set":
            key, _, value = rest.partition(" ")
            _RUNTIME.set(key, value)
            return "OK"

        if action == "get":
            return _RUNTIME.get(rest)

        return "Usage: set|get"
