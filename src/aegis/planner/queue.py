from aegis.planner.task import Task


class TaskQueue:
    def __init__(self) -> None:
        self._queue: list[Task] = []

    def add(self, task: Task) -> None:
        self._queue.append(task)

    def pop(self) -> Task | None:
        if not self._queue:
            return None
        return self._queue.pop(0)

    def empty(self) -> bool:
        return not self._queue
