from dataclasses import dataclass


@dataclass(slots=True)
class Command:
    text: str


class CommandEngine:
    def parse(self, text: str) -> Command:
        return Command(text=text.strip())
