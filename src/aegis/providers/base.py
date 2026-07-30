from abc import ABC, abstractmethod

from aegis.ai.request import AIRequest
from aegis.ai.response import AIResponse


class BaseAIProvider(ABC):
    """Base interface for every AI provider."""

    @property
    @abstractmethod
    def name(self) -> str: ...

    @abstractmethod
    def generate(self, request: AIRequest) -> AIResponse: ...
