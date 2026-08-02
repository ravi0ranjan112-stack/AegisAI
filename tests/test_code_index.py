from aegis.code.index import CodeIndex


def test_build():
    index = CodeIndex()
    assert index.build() > 0


def test_search():
    index = CodeIndex()
    index.build()

    assert isinstance(index.search("Agent"), list)
