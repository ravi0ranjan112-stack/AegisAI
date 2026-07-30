from aegis.ai.request import AIRequest
from aegis.ai.response import AIResponse
from aegis.providers.base import BaseAIProvider


class OllamaProvider(BaseAIProvider):
    @property
    def name(self) -> str:
        return "ollama"

    def generate(self, request: AIRequest) -> AIResponse:
        raise NotImplementedError("Ollama provider is not implemented yet.")
