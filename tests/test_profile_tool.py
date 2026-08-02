from aegis.tools.profile import ProfileTool


def test_profile_tool():
    tool = ProfileTool()
    assert tool.run("set mode smart") == "OK"
    assert tool.run("get mode") == "smart"
