from aegis.prompts.store import PromptStore


def test_prompt_store():
    store = PromptStore()
    assert store.execute("add code WritePython") == "OK"
    assert store.execute("show code") == "WritePython"
