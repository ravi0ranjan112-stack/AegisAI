from aegis.patch.editor import FileEditor


def test_replace(tmp_path) -> None:
    f = tmp_path / "demo.txt"
    f.write_text("hello world", encoding="utf-8")

    editor = FileEditor()

    assert editor.replace(str(f), "world", "Aegis")
    assert editor.read(str(f)) == "hello Aegis"
