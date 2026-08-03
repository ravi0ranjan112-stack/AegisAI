from aegis.planner.queue import TaskQueue
from aegis.planner.task import Task


def test_queue() -> None:
    q = TaskQueue()

    q.add(Task("A"))
    q.add(Task("B"))

    first = q.pop()
    second = q.pop()

    assert first is not None
    assert second is not None

    assert first.title == "A"
    assert second.title == "B"
    assert q.empty()
