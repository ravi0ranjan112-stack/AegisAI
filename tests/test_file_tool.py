from pathlib import Path

from aegis.tools.file import FileTool


def test_write_and_read(tmp_path: Path):
    tool = FileTool()

    file = tmp_path / "hello.txt"

    assert tool.run(f"write {file} hello world") == "OK"
    assert tool.run(f"read {file}") == "hello world"


def test_list(tmp_path: Path):
    tool = FileTool()

    (tmp_path / "a.txt").write_text("a")
    (tmp_path / "b.txt").write_text("b")

    result = tool.run(f"list {tmp_path}")

    assert "a.txt" in result
    assert "b.txt" in result
