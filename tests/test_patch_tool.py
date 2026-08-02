from aegis.tools.patch import PatchTool


def test_patch(tmp_path):
    file = tmp_path / "a.txt"
    file.write_text("hello", encoding="utf-8")

    tool = PatchTool()

    assert tool.run(f"read {file}") == "hello"
    assert tool.run(f"write {file} world") == "OK"
    assert file.read_text(encoding="utf-8") == "world"
