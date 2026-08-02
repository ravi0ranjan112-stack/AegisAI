from pathlib import Path

from aegis.lsp.workspace import Workspace


def test_workspace(tmp_path: Path):
    f = tmp_path / "demo.py"
    f.write_text("print('hello')", encoding="utf-8")

    doc = Workspace().open(str(f))

    assert doc.path.endswith("demo.py")
    assert "hello" in doc.text
