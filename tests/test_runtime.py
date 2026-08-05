from aegis.runtime.runtime import Runtime


def test_runtime() -> None:
    runtime = Runtime()

    assert "AEGIS AI" in runtime.start()
    assert runtime.handle("Hello") == "Aegis > You said: Hello"
    assert runtime.handle("") == "Aegis > Please enter a command."
    assert runtime.handle("exit") == "Goodbye."
