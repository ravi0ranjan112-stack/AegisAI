from aegis.rag.store import RagStore


def test_rag_store():
    store = RagStore()
    assert store.execute("add hello world") == "OK"
    assert "hello world" in store.execute("search hello")
