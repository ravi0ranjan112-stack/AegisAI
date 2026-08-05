from aegis.chat.engine import ChatEngine


class MemoryChat:
    def __init__(self) -> None:
        self.engine = ChatEngine()

    def ask(self, prompt: str) -> str:
        return self.engine.chat(prompt)

    @property
    def history(self):
        return self.engine.session.messages
