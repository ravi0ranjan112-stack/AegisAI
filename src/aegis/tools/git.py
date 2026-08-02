import subprocess

from aegis.tools.base import BaseTool


class GitTool(BaseTool):
    @property
    def name(self) -> str:
        return "git"

    def run(self, command: str) -> str:
        try:
            result = subprocess.run(
                ["git", *command.split()],
                capture_output=True,
                text=True,
                check=False,
            )

            output = result.stdout.strip()

            if result.stderr.strip():
                if output:
                    output += "\n"
                output += result.stderr.strip()

            return output or "(no output)"

        except Exception as exc:
            return f"Error: {exc}"
