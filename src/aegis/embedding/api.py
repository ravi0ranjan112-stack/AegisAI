import httpx


class EmbeddingAPI:
    def __init__(
        self,
        model: str = "nomic-embed-text",
        host: str = "http://localhost:11434",
    ) -> None:
        self.model = model
        self.host = host.rstrip("/")

    def embed(self, text: str) -> list[float]:
        response = httpx.post(
            f"{self.host}/api/embeddings",
            json={
                "model": self.model,
                "prompt": text,
            },
            timeout=60,
        )

        response.raise_for_status()

        data = response.json()

        return data["embedding"]
