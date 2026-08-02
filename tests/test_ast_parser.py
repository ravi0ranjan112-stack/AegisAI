from pathlib import Path

from aegis.ast.parser import ASTParser
from aegis.ast.symbols import SymbolExtractor


def test_parser(tmp_path: Path):
    f = tmp_path / "demo.py"

    f.write_text(
        "class A:\n    pass\n\ndef hello():\n    pass\n",
        encoding="utf-8",
    )

    assert ASTParser().parse(str(f))
    assert SymbolExtractor().extract(str(f)) == [
        "A",
        "hello",
    ]
