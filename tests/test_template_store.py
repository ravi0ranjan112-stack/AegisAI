from aegis.templates.store import TemplateStore


def test_template_store():
    store = TemplateStore()
    assert store.execute("add hello HelloWorld") == "OK"
    assert store.execute("show hello") == "HelloWorld"
