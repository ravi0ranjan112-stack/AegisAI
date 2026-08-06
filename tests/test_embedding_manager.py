from unittest.mock import Mock, patch

from aegis.embedding.manager import EmbeddingManager


def test_embedding_manager() -> None:
    fake = Mock()
    fake.raise_for_status.return_value = None
    fake.json.return_value = {"embedding": [0.5, 0.7]}

    with patch("httpx.post", return_value=fake):
        manager = EmbeddingManager()

        assert manager.create("hello") == [0.5, 0.7]
