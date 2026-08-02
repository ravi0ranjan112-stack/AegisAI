from aegis.rag.chunk import Chunk

_CHUNKS: list[Chunk] = []


class RagStore:
    def execute(self, command: str) -> str:
        action, _, rest = command.partition(" ")

        if action == "add":
            _CHUNKS.append(Chunk(len(_CHUNKS), rest))
            return "OK"

        if action == "search":
            result = [chunk.text for chunk in _CHUNKS if rest.lower() in chunk.text.lower()]
            return "\n".join(result) or "No results"

        if action == "count":
            return str(len(_CHUNKS))

        return "Usage: add|search|count"
