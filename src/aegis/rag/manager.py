from aegis.rag.retriever import Retriever


class RagManager:
    def execute(self, command: str) -> str:
        return Retriever().execute(command)
