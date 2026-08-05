from aegis.context.manager import ContextManager


def test_context_manager() -> None:
    manager = ContextManager()

    manager.add("Python")
    manager.add("Linux")

    prompt = manager.build("Explain")

    assert "Python" in prompt
    assert "Linux" in prompt
    assert "User: Explain" in prompt
