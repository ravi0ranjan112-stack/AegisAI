from pathlib import Path

from aegis.lsp.client import LSPClient


def test_client(tmp_path: Path):
    good = tmp_path / "good.py"
    good.write_text("x=1\n", encoding="utf-8")

    bad = tmp_path / "bad.py"
    bad.write_text("def x(:\n    pass\n", encoding="utf-8")

    client = LSPClient()

    assert client.open(str(good)) == "x=1\n"
    assert client.diagnostics(str(good)) == []
    assert client.diagnostics(str(bad))
