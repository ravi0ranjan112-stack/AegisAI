from abc import ABC, abstractmethod


class BaseTool(ABC):
    """Base class for every tool."""

    @property
    @abstractmethod
    def name(self) -> str: ...

    @abstractmethod
    def run(self, command: str) -> str:
        """Execute the tool and return its output."""
        ...
