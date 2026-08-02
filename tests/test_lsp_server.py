from pathlib import Path

from aegis.lsp.server import LSPServer


def test_server(tmp_path: Path):
    good = tmp_path / "good.py"
    good.write_text("x=1\n", encoding="utf-8")

    bad = tmp_path / "bad.py"
    bad.write_text("def x(:\n    pass\n", encoding="utf-8")

    server = LSPServer()

    assert server.execute(f"open {good}") == "x=1\n"
    assert server.execute(f"diagnostics {good}") == "OK"
    assert server.execute(f"diagnostics {bad}") != "OK"
