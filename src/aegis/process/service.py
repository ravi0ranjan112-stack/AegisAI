import subprocess
from dataclasses import dataclass


@dataclass(slots=True)
class ProcessResult:
    command: list[str]
    returncode: int
    stdout: str
    stderr: str


class ProcessService:
    def run(self, command: list[str], cwd: str | None = None) -> ProcessResult:
        process = subprocess.run(
            command,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=False,
        )

        return ProcessResult(
            command=command,
            returncode=process.returncode,
            stdout=process.stdout,
            stderr=process.stderr,
        )
