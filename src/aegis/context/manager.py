from aegis.context.context import Context
from aegis.context.injector import ContextInjector


class ContextManager:
    def __init__(self) -> None:
        self.context = Context()
        self.injector = ContextInjector()

    def add(self, text: str) -> None:
        self.context.add(text)

    def build(self, prompt: str) -> str:
        return self.injector.inject(prompt, self.context)
