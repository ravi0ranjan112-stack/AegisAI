from aegis.tasks.task import Task


class TaskQueue:
    def __init__(self) -> None:
        self._tasks: list[Task] = []

    def add(self, title: str) -> str:
        self._tasks.append(Task(len(self._tasks) + 1, title))
        return "OK"

    def done(self, task_id: int) -> str:
        for task in self._tasks:
            if task.id == task_id:
                task.done = True
                return "OK"
        return "Not found"

    def list(self) -> str:
        return (
            "\n".join(f"[{'x' if t.done else ' '}] {t.id}. {t.title}" for t in self._tasks)
            or "No tasks"
        )
