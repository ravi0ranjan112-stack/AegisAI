import subprocess

from aegis.tools.base import BaseTool


class ShellTool(BaseTool):
    _ALLOWED = {
        "pwd",
        "ls",
        "git status",
        "pytest",
        "ruff",
        "mypy",
    }

    @property
    def name(self) -> str:
        return "shell"

    def run(self, command: str) -> str:
        command = command.strip()

        if command not in self._ALLOWED:
            return f"Command not allowed: {command}"

        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                check=False,
            )

            output = result.stdout.strip()

            if result.stderr.strip():
                output += "\n" + result.stderr.strip()

            return output or "(no output)"

        except Exception as exc:
            return f"Error: {exc}"
