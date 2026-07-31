from aegis.ai.manager import AIManager
from aegis.ai.settings import AISettings
from aegis.conversation.session import ConversationSession
from aegis.providers.factory import ProviderFactory
from aegis.providers.router import ProviderRouter
from aegis.tools.factory import ToolFactory
from aegis.tools.manager import ToolManager


class AegisKernel:
    def __init__(self) -> None:
        self.settings = AISettings()

        self.session = ConversationSession()

        registry = ProviderFactory.create_registry()

        self.router = ProviderRouter(
            registry=registry,
            default_provider=self.settings.provider,
        )

        self.ai = AIManager(
            router=self.router,
            session=self.session,
        )

        tool_registry = ToolFactory.create_registry()

        self.tools = ToolManager(tool_registry)
