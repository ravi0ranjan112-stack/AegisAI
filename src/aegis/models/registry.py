from aegis.models.model import Model


class ModelRegistry:
    def __init__(self) -> None:
        self._models: dict[str, Model] = {}

    def register(self, model: Model) -> None:
        self._models[model.name] = model

    def get(self, name: str) -> Model:
        return self._models[name]

    def names(self) -> list[str]:
        return sorted(self._models)
