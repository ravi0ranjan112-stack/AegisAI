from aegis.runtime.console import Console


class Runtime:
    def __init__(self) -> None:
        self.console = Console()
        self._state: dict[str, str] = {}

    def start(self) -> str:
        return self.console.banner()

    def handle(self, command: str) -> str:
        command = command.strip()

        if command.lower() in {"exit", "quit"}:
            return "Goodbye."

        if not command:
            return self.console.reply("Please enter a command.")

        return self.console.reply(f"You said: {command}")

    # Backward compatibility for RuntimeTool
    def execute(self, command: str) -> str:
        parts = command.split()

        if len(parts) >= 3 and parts[0] == "set":
            self._state[parts[1]] = " ".join(parts[2:])
            return "OK"

        if len(parts) == 2 and parts[0] == "get":
            return self._state.get(parts[1], "Unknown")

        return "Unknown command"
