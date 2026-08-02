from dataclasses import dataclass


@dataclass(slots=True)
class ModelRoute:
    provider: str
    model: str


class ModelRouter:
    def __init__(self) -> None:
        self._routes: dict[str, ModelRoute] = {}

    def register(self, task: str, provider: str, model: str) -> None:
        self._routes[task] = ModelRoute(provider, model)

    def route(self, task: str) -> ModelRoute:
        return self._routes.get(
            task,
            ModelRoute("default", "default"),
        )
