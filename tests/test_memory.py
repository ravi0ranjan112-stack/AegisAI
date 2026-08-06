from aegis.memory.memory import Memory


def test_memory() -> None:
    memory = Memory("name", "Aegis")

    assert memory.key == "name"
    assert memory.value == "Aegis"
