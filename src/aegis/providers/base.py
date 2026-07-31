from abc import ABC, abstractmethod
from collections.abc import Iterator

from aegis.ai.request import AIRequest
from aegis.ai.response import AIResponse


class BaseAIProvider(ABC):
    """Base interface for every AI provider."""

    @property
    @abstractmethod
    def name(self) -> str: ...

    @abstractmethod
    def generate(self, request: AIRequest) -> AIResponse: ...

    @abstractmethod
    def stream_generate(
        self,
        request: AIRequest,
    ) -> Iterator[str]: ...
