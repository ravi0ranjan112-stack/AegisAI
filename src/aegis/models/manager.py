from aegis.models.model import Model
from aegis.models.registry import ModelRegistry
from aegis.models.router import ModelRouter


class ModelManager:
    def __init__(self) -> None:
        self.registry = ModelRegistry()
        self.router = ModelRouter()

    def register(self, model: Model, task: str) -> None:
        self.registry.register(model)
        self.router.register(
            task,
            model.provider,
            model.name,
        )

    def resolve(self, task: str) -> Model:
        route = self.router.route(task)
        return self.registry.get(route.model)
