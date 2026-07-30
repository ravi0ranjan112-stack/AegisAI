import tomllib
from pathlib import Path


class ConfigLoader:
    def __init__(self, path: str = "configs/default.toml") -> None:
        self.path = Path(path)

    def load(self) -> dict:
        with self.path.open("rb") as f:
            return tomllib.load(f)
