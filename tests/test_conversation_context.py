from aegis.conversation.context import ConversationContext
from aegis.conversation.session import ConversationSession


def test_conversation_context():
    session = ConversationSession()

    session.add_user("hello")
    session.add_assistant("hi")
    session.add_user("how are you?")

    context = ConversationContext(session)

    result = context.build()

    assert "user: hello" in result
    assert "assistant: hi" in result
    assert "how are you?" in result
