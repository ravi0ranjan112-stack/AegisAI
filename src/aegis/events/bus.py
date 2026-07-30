from collections import defaultdict
from collections.abc import Callable
from typing import Any


class EventBus:
    def __init__(self) -> None:
        self._listeners: dict[str, list[Callable[..., None]]] = defaultdict(list)

    def subscribe(self, event: str, callback: Callable[..., None]) -> None:
        self._listeners[event].append(callback)

    def emit(self, event: str, *args: Any, **kwargs: Any) -> None:
        for callback in self._listeners.get(event, []):
            callback(*args, **kwargs)
