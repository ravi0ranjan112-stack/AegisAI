from dataclasses import dataclass


@dataclass(slots=True)
class Config:
    values: dict[str, str]
