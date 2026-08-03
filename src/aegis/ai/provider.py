from abc import ABC, abstractmethod

from aegis.ai.response import AIResponse


class AIProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> AIResponse:
        raise NotImplementedError
