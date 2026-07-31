from collections.abc import Iterator

from aegis.ai.request import AIRequest
from aegis.ai.response import AIResponse
from aegis.providers.base import BaseAIProvider
from aegis.providers.ollama.client import OllamaClient
from aegis.providers.ollama.config import OllamaConfig


class OllamaProvider(BaseAIProvider):
    def __init__(self) -> None:
        self._client = OllamaClient(OllamaConfig())

    @property
    def name(self) -> str:
        return "ollama"

    def generate(self, request: AIRequest) -> AIResponse:
        return self._client.generate(request)

    def stream_generate(
        self,
        request: AIRequest,
    ) -> Iterator[str]:
        return self._client.stream_generate(request)
