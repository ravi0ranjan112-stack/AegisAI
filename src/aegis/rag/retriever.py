from aegis.rag.store import RagStore


class Retriever:
    def execute(self, command: str) -> str:
        return RagStore().execute(command)
