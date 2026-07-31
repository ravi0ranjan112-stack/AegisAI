import subprocess
import sys
import tempfile
from pathlib import Path

from aegis.tools.base import BaseTool


class PythonTool(BaseTool):
    TIMEOUT = 5

    @property
    def name(self) -> str:
        return "python"

    def run(self, command: str) -> str:
        try:
            with tempfile.TemporaryDirectory() as tmpdir:
                script = Path(tmpdir) / "script.py"
                script.write_text(command, encoding="utf-8")

                result = subprocess.run(
                    [sys.executable, str(script)],
                    capture_output=True,
                    text=True,
                    timeout=self.TIMEOUT,
                    check=False,
                )

                output = result.stdout.strip()

                if result.stderr.strip():
                    if output:
                        output += "\n"
                    output += result.stderr.strip()

                return output or "(no output)"

        except subprocess.TimeoutExpired:
            return "Execution timed out."

        except Exception as exc:
            return f"Error: {exc}"
