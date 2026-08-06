from aegis.embedding.model import Embedding


class VectorStore:
    def __init__(self) -> None:
        self._items: list[Embedding] = []

    def add(
        self,
        embedding: Embedding | str,
        vector: str | None = None,
    ) -> None:
        if isinstance(embedding, Embedding):
            self._items.append(embedding)
        else:
            self._items.append(
                Embedding(
                    text=embedding,
                    vector=[float(len(vector or ""))],
                )
            )

    def all(self) -> list[Embedding]:
        return list(self._items)

    def search(self, query: str) -> list[str]:
        return [item.text for item in self._items if query.lower() in item.text.lower()]
