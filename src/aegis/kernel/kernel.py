from aegis.ai.manager import AIManager
from aegis.ai.settings import AISettings
from aegis.conversation.session import ConversationSession
from aegis.providers.factory import ProviderFactory
from aegis.providers.router import ProviderRouter


class AegisKernel:
    def __init__(self) -> None:
        self.settings = AISettings()

        registry = ProviderFactory.create_registry()

        self.router = ProviderRouter(
            registry=registry,
            default_provider=self.settings.provider,
        )

        self.ai = AIManager(self.router)
        self.session = ConversationSession()
