from aegis.memory.memory import Memory


def test_memory() -> None:
    memory = Memory("language", "Python")

    assert memory.key == "language"
    assert memory.value == "Python"
