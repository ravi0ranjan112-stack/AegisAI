from aegis.memory.index import MemoryIndex


class MemorySearch:
    def __init__(self, index: MemoryIndex) -> None:
        self._index = index

    def find(self, query: str):
        return [doc for doc in self._index.documents if query.lower() in doc.text.lower()]
