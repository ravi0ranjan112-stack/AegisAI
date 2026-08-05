from aegis.llm.provider import LLMProvider


class OllamaProvider(LLMProvider):
    def generate(self, prompt: str) -> str:
        return f"Ollama: {prompt}"
