from aegis.tasks.queue import TaskQueue


def test_queue():
    q = TaskQueue()
    assert q.add("demo") == "OK"
    assert "demo" in q.list()
    assert q.done(1) == "OK"
