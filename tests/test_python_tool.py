from aegis.tools.python import PythonTool


def test_python_print():
    tool = PythonTool()
    result = tool.run("print('hello')")

    assert result == "hello"


def test_python_math():
    tool = PythonTool()
    result = tool.run("print(6 * 7)")

    assert result == "42"


def test_python_error():
    tool = PythonTool()
    result = tool.run("raise ValueError('boom')")

    assert "ValueError" in result
