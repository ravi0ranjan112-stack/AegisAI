from aegis.runtime.runtime import Runtime


def test_runtime():
    runtime = Runtime()
    assert runtime.execute("set language python") == "OK"
    assert runtime.execute("get language") == "python"
