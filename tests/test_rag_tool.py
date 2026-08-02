from aegis.tools.rag import RagTool


def test_rag_tool():
    tool = RagTool()
    assert tool.run("add python ai") == "OK"
    assert "python ai" in tool.run("search python")
