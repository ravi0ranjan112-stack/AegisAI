import json
from collections.abc import Iterator
from urllib.request import Request, urlopen

from aegis.ai.request import AIRequest
from aegis.ai.response import AIResponse
from aegis.providers.ollama.config import OllamaConfig


class OllamaClient:
    def __init__(self, config: OllamaConfig) -> None:
        self._config = config

    def generate(self, request: AIRequest) -> AIResponse:
        messages = [
            {
                "role": message.role,
                "content": message.content,
            }
            for message in request.messages
        ]

        if not messages:
            messages.append(
                {
                    "role": "user",
                    "content": request.prompt,
                }
            )

        payload = {
            "model": self._config.model,
            "messages": messages,
            "stream": False,
        }

        req = Request(
            url=f"{self._config.host}/api/chat",
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        with urlopen(req, timeout=self._config.timeout) as response:
            result = json.loads(response.read().decode())

        return AIResponse(
            text=result["message"]["content"],
            provider="ollama",
            model=self._config.model,
        )

    def stream_generate(
        self,
        request: AIRequest,
    ) -> Iterator[str]:
        messages = [
            {
                "role": message.role,
                "content": message.content,
            }
            for message in request.messages
        ]

        if not messages:
            messages.append(
                {
                    "role": "user",
                    "content": request.prompt,
                }
            )

        payload = {
            "model": self._config.model,
            "messages": messages,
            "stream": True,
        }

        req = Request(
            url=f"{self._config.host}/api/chat",
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        with urlopen(req, timeout=self._config.timeout) as response:
            for line in response:
                if not line.strip():
                    continue

                chunk = json.loads(line.decode())

                if chunk.get("done"):
                    break

                yield chunk["message"]["content"]
