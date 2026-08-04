from aegis.services.service import Service
from aegis.services.service_registry import ServiceRegistry


class ServiceManager:
    def __init__(self) -> None:
        self.registry = ServiceRegistry()

    def add(self, name: str) -> None:
        self.registry.register(Service(name))
