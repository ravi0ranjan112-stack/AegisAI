from aegis.code.index import CodeIndex


def test_code_index() -> None:
    index = CodeIndex()
    assert index.build() > 0
    assert isinstance(index.search("MemoryStore"), list)
