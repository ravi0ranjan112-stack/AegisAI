from aegis.profiles.store import ProfileStore


class ProfileManager:
    def execute(self, command: str) -> str:
        return ProfileStore().execute(command)
