from unittest.mock import Mock, patch

from aegis.embedding.api import EmbeddingAPI


def test_embedding_api() -> None:
    fake = Mock()
    fake.raise_for_status.return_value = None
    fake.json.return_value = {"embedding": [0.1, 0.2, 0.3]}

    with patch("httpx.post", return_value=fake):
        api = EmbeddingAPI()

        assert api.embed("hello") == [0.1, 0.2, 0.3]
