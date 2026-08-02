from aegis.tasks.scheduler import Scheduler


class TaskManager:
    def __init__(self) -> None:
        self._queue = Scheduler().queue()

    def execute(self, command: str) -> str:
        action, _, value = command.partition(" ")

        if action == "add":
            return self._queue.add(value)

        if action == "done":
            return self._queue.done(int(value))

        if action == "list":
            return self._queue.list()

        return "Usage: add|done|list"
