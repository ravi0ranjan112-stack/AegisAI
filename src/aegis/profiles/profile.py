from dataclasses import dataclass


@dataclass(slots=True)
class Profile:
    values: dict[str, str]
