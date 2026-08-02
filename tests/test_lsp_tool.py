from pathlib import Path

from aegis.tools.lsp import LSPTool


def test_lsp_tool(tmp_path: Path):
    good = tmp_path / "good.py"
    good.write_text("x=1\n", encoding="utf-8")

    bad = tmp_path / "bad.py"
    bad.write_text("def x(:\n    pass\n", encoding="utf-8")

    tool = LSPTool()

    assert tool.run(f"open {good}") == "x=1\n"
    assert tool.run(f"diagnostics {good}") == "OK"
    assert tool.run(f"diagnostics {bad}") != "OK"
