from aegis.chat.session import ChatSession
from aegis.llm.manager import LLMManager


class ChatEngine:
    def __init__(self) -> None:
        self.session = ChatSession()
        self.llm = LLMManager()

    def chat(self, prompt: str) -> str:
        self.session.add("user", prompt)

        reply = self.llm.ask(prompt)

        self.session.add("assistant", reply)

        return reply
