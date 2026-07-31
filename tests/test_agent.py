from aegis.agent.agent import Agent
from aegis.agent.executor import AgentExecutor
from aegis.ai.manager import AIManager
from aegis.conversation.session import ConversationSession
from aegis.providers.mock.provider import MockProvider
from aegis.providers.registry import ProviderRegistry
from aegis.providers.router import ProviderRouter
from aegis.tools.factory import ToolFactory
from aegis.tools.manager import ToolManager


def test_agent_run():
    registry = ProviderRegistry()
    registry.register(MockProvider())

    router = ProviderRouter(
        registry=registry,
        default_provider="mock",
    )

    session = ConversationSession()

    ai = AIManager(
        router=router,
        session=session,
    )

    tools = ToolManager(
        ToolFactory.create_registry(),
    )

    executor = AgentExecutor(tools)

    agent = Agent(ai, executor)

    result = agent.run("Hello")

    assert isinstance(result, str)
    assert result
