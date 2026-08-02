from aegis.project.stats import ProjectStats


def test_stats():
    stats = ProjectStats().collect(".")
    assert stats["files"] >= 1
    assert stats["lines"] >= 1
