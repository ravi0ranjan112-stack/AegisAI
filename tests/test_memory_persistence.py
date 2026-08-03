from aegis.memory.models import Memory
from aegis.memory.persistence import MemoryPersistence


def test_memory_persistence(tmp_path):
    file = tmp_path / "memory.json"

    persistence = MemoryPersistence()

    persistence.save(
        str(file),
        [
            Memory("hello", "world"),
            Memory("python", "rocks"),
        ],
    )

    loaded = persistence.load(str(file))

    assert len(loaded) == 2
    assert loaded[0].key == "hello"
    assert loaded[0].value == "world"
