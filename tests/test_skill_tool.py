from aegis.tools.skill import SkillTool


def test_skill_tool():
    tool = SkillTool()
    assert tool.run("add python WritePython") == "OK"
    assert tool.run("show python") == "WritePython"
