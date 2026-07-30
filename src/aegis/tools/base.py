from abc import ABC, abstractmethod


class BaseTool(ABC):
    name: str = "tool"
    description: str = ""

    @abstractmethod
    def execute(self, *args, **kwargs):
        raise NotImplementedError
