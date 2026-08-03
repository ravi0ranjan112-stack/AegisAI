from aegis.ai.manager import AIManager
from aegis.ai.provider import AIProvider
from aegis.ai.response import AIResponse


class DummyProvider(AIProvider):
    def generate(self, prompt: str) -> AIResponse:
        return AIResponse(prompt)


def test_ai_provider() -> None:
    ai = AIManager(DummyProvider())
    assert ai.ask("hello").text == "hello"
    assert "ctx" in ai.ask("hello", "ctx").text
