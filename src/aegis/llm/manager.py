from aegis.llm.ollama import OllamaProvider


class LLMManager:
    def __init__(self) -> None:
        self.provider = OllamaProvider()

    def ask(self, prompt: str) -> str:
        return self.provider.generate(prompt)
