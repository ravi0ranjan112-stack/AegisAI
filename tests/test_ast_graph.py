from pathlib import Path

from aegis.ast.graph import DependencyGraph
from aegis.ast.references import ReferenceFinder


def test_graph(tmp_path: Path):
    f = tmp_path / "demo.py"

    f.write_text(
        "def b():\n    pass\n\ndef a():\n    b()\n    b()\n    return b\n",
        encoding="utf-8",
    )

    graph = DependencyGraph().build(str(f))

    assert graph["a"] == ["b"]
    assert ReferenceFinder().find(str(f), "b") == [5, 6]
