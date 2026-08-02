from aegis.tools.template import TemplateTool


def test_template_tool():
    tool = TemplateTool()
    assert tool.run("add demo Test") == "OK"
    assert tool.run("show demo") == "Test"
