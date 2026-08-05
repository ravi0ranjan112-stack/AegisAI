from aegis.llm.provider import LLMProvider


class DummyProvider(LLMProvider):
    def generate(self, prompt: str) -> str:
        return prompt


def test_provider() -> None:
    provider = DummyProvider()
    assert provider.generate("hello") == "hello"
