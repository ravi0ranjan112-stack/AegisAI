from aegis.tools.vector import VectorTool


def test_vector_tool():
    tool = VectorTool()

    assert tool.run("add python Python language") == "OK"

    result = tool.run("search python")

    assert "python" in result
