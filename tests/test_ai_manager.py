from aegis.ai.manager import AIManager
from aegis.conversation.session import ConversationSession
from aegis.providers.mock.provider import MockProvider
from aegis.providers.registry import ProviderRegistry
from aegis.providers.router import ProviderRouter


def test_ai_manager():
    registry = ProviderRegistry()
    registry.register(MockProvider())

    router = ProviderRouter(
        registry=registry,
        default_provider="mock",
    )

    session = ConversationSession()

    manager = AIManager(
        router=router,
        session=session,
    )

    assert manager.active_provider == "mock"

    result = manager.ask("Hello")

    assert result == "Mock response: Hello"

    assert len(session.messages) == 2
    assert session.messages[0].role == "user"
    assert session.messages[0].content == "Hello"
    assert session.messages[1].role == "assistant"
    assert session.messages[1].content == "Mock response: Hello"
