class Embedder:
    def embed(self, text: str) -> list[float]:
        if not text:
            return []

        return [float(ord(char)) for char in text]
