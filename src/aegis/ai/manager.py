from collections.abc import Iterator

from aegis.ai.request import AIRequest
from aegis.ai.response import AIResponse
from aegis.ai.system_prompt import SYSTEM_PROMPT
from aegis.conversation.session import ConversationSession
from aegis.providers.router import ProviderRouter


class AIManager:
    def __init__(
        self,
        router: ProviderRouter,
        session: ConversationSession,
    ) -> None:
        self._router = router
        self._session = session

    def ask(
        self,
        prompt: str,
        *,
        system_prompt: str | None = None,
    ) -> str:
        provider = self._router.provider()

        self._session.add_user(prompt)

        request = AIRequest(
            prompt=prompt,
            system_prompt=system_prompt or SYSTEM_PROMPT,
            messages=self._session.messages,
        )

        response: AIResponse = provider.generate(request)

        self._session.add_assistant(response.text)

        return response.text

    def stream(
        self,
        prompt: str,
        *,
        system_prompt: str | None = None,
    ) -> Iterator[str]:
        provider = self._router.provider()

        self._session.add_user(prompt)

        request = AIRequest(
            prompt=prompt,
            system_prompt=system_prompt or SYSTEM_PROMPT,
            messages=self._session.messages,
        )

        chunks: list[str] = []

        for chunk in provider.stream_generate(request):
            chunks.append(chunk)
            yield chunk

        self._session.add_assistant("".join(chunks))

    @property
    def active_provider(self) -> str:
        return self._router.active

    def switch_provider(self, name: str) -> None:
        self._router.set_active(name)
