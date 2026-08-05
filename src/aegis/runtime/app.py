from aegis.runtime.runtime import Runtime


class AegisApp:
    def __init__(self) -> None:
        self.runtime = Runtime()

    def start(self) -> str:
        return self.runtime.start()

    def execute(self, command: str) -> str:
        return self.runtime.handle(command)
