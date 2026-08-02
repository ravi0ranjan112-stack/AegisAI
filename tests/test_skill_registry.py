from aegis.skills.registry import SkillRegistry


def test_registry():
    registry = SkillRegistry()
    assert registry.add("python", "Write Python") == "OK"
    assert registry.get("python")
