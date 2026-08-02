from aegis.tasks.queue import TaskQueue

_QUEUE = TaskQueue()


class Scheduler:
    def queue(self) -> TaskQueue:
        return _QUEUE
