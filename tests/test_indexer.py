from aegis.index.indexer import ProjectIndexer


def test_index():
    docs = ProjectIndexer().build(".")
    assert isinstance(docs, list)
