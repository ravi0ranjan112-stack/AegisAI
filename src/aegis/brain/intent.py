from dataclasses import dataclass


@dataclass(slots=True)
class Intent:
    tool: str
    command: str


class IntentDetector:
    def detect(self, text: str) -> Intent:
        command = text.strip()

        if command.startswith(("remember ", "search ", "clear")):
            return Intent("memory", command)

        if command.startswith(("diagnostics ", "open ")):
            return Intent("lsp", command)

        if command.startswith(("add ", "find ")):
            return Intent("vector", command)

        return Intent("conversation", f"user {command}")
