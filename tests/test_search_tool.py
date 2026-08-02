from aegis.tools.search import SearchTool


def test_search():
    result = SearchTool().run("class")
    assert isinstance(result, str)
