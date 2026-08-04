from aegis.services.service import Service


class ServiceRegistry:
    def __init__(self) -> None:
        self._services: dict[str, Service] = {}

    def register(self, service: Service) -> None:
        self._services[service.name] = service

    def get(self, name: str) -> Service | None:
        return self._services.get(name)

    @property
    def services(self) -> dict[str, Service]:
        return self._services
