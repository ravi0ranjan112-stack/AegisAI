from aegis.integration.bootstrap import bootstrap


class IntegrationManager:
    def __init__(self) -> None:
        self.kernel = bootstrap()

    def ready(self) -> bool:
        return (
            self.kernel.agent is not None
            and self.kernel.memory is not None
            and self.kernel.workflow is not None
        )
