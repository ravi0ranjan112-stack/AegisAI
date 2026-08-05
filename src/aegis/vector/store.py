from aegis.vector.document import Document


class VectorStore:
    def __init__(self) -> None:
        self._documents: dict[str, Document] = {}

    def add(self, doc_id: str, text: str) -> None:
        self._documents[doc_id] = Document(doc_id, text)

    def get(self, doc_id: str) -> Document | None:
        return self._documents.get(doc_id)

    def all(self) -> list[Document]:
        return list(self._documents.values())

    # Backward-compatible API
    def search(self, query: str) -> list[str]:
        query = query.lower()

        return [
            doc.id
            for doc in self._documents.values()
            if query in doc.id.lower() or query in doc.text.lower()
        ]
