from collections.abc import Iterator

from aegis.ai.request import AIRequest
from aegis.ai.response import AIResponse
from aegis.providers.base import BaseAIProvider


class MockProvider(BaseAIProvider):
    @property
    def name(self) -> str:
        return "mock"

    def generate(self, request: AIRequest) -> AIResponse:
        return AIResponse(
            text=f"Mock response: {request.prompt}",
            provider="mock",
            model="mock-v1",
        )

    def stream_generate(
        self,
        request: AIRequest,
    ) -> Iterator[str]:
        yield f"Mock response: {request.prompt}"
