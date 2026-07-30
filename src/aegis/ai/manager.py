from aegis.ai.request import AIRequest
from aegis.ai.response import AIResponse
from aegis.providers.router import ProviderRouter


class AIManager:
    def __init__(self, router: ProviderRouter) -> None:
        self._router = router

    def ask(self, prompt: str) -> str:
        provider = self._router.provider()

        request = AIRequest(prompt=prompt)
        response: AIResponse = provider.generate(request)

        return response.text

    @property
    def active_provider(self) -> str:
        return self._router.active

    def switch_provider(self, name: str) -> None:
        self._router.set_active(name)
