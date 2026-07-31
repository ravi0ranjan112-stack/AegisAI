from pathlib import Path

from aegis.tools.base import BaseTool


class FileTool(BaseTool):
    @property
    def name(self) -> str:
        return "file"

    def run(self, command: str) -> str:
        parts = command.split(maxsplit=1)

        if not parts:
            return "Invalid command."

        action = parts[0]
        argument = parts[1] if len(parts) > 1 else ""

        result: str

        try:
            if action == "read":
                result = Path(argument).read_text(encoding="utf-8")

            elif action == "list":
                path = Path(argument or ".")
                result = "\n".join(sorted(item.name for item in path.iterdir()))

            elif action == "write":
                values = argument.split(" ", 1)

                if len(values) != 2:
                    result = "Usage: write <path> <content>"
                else:
                    Path(values[0]).write_text(
                        values[1],
                        encoding="utf-8",
                    )
                    result = "OK"

            else:
                result = f"Unknown action: {action}"

        except Exception as exc:
            result = f"Error: {exc}"

        return result
