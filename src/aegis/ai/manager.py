from aegis.ai.prompt import PromptBuilder
from aegis.ai.request import AIRequest
from aegis.ai.response import AIResponse


class AIManager:
    def __init__(self, provider=None, router=None, session=None) -> None:
        self._provider = provider
        self._router = router
        self._session = session
        self._prompt = PromptBuilder()

    @property
    def active_provider(self) -> str:
        if self._router is not None:
            return self._router.active
        if self._provider is not None:
            return getattr(self._provider, "name", "unknown")
        return "unknown"

    def ask(self, text: str, context: str = ""):
        prompt = self._prompt.build(text, context)

        if self._session is not None:
            self._session.add_user(text)

        if self._provider is not None:
            result = self._provider.generate(prompt)
            if not isinstance(result, AIResponse):
                result = AIResponse(text=result)

            if self._session is not None:
                self._session.add_assistant(result.text)

            return result

        if self._router is not None:
            result = self._router.provider().generate(AIRequest(prompt=prompt))

            if isinstance(result, AIResponse):
                text_out = result.text
            else:
                text_out = result

            if self._session is not None:
                self._session.add_assistant(text_out)

            return text_out

        return AIResponse(text="No provider configured")
