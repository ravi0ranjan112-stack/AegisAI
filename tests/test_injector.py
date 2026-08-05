from aegis.context.context import Context
from aegis.context.injector import ContextInjector


def test_injector() -> None:
    context = Context()
    context.add("Python")
    context.add("Linux")

    injector = ContextInjector()

    prompt = injector.inject("Explain", context)

    assert "Python" in prompt
    assert "Linux" in prompt
    assert "User: Explain" in prompt
