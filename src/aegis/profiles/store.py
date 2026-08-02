from aegis.profiles.profile import Profile

_PROFILE = Profile(values={})


class ProfileStore:
    def execute(self, command: str) -> str:
        action, _, rest = command.partition(" ")

        if action == "set":
            key, _, value = rest.partition(" ")
            _PROFILE.values[key] = value
            return "OK"

        if action == "get":
            return _PROFILE.values.get(rest, "")

        if action == "list":
            return "\n".join(f"{k}={v}" for k, v in sorted(_PROFILE.values.items())) or "Empty"

        return "Usage: set|get|list"
