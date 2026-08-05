from aegis.context.context import Context


def test_context() -> None:
    context = Context()

    context.add("Hello")
    context.add("World")

    assert len(context.items) == 2
    assert context.items[0] == "Hello"
    assert context.items[1] == "World"
