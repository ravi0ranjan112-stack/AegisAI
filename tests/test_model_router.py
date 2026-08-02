from aegis.models.router import ModelRouter


def test_model_router() -> None:
    router = ModelRouter()

    router.register(
        "chat",
        "ollama",
        "llama3",
    )

    route = router.route("chat")

    assert route.provider == "ollama"
    assert route.model == "llama3"

    fallback = router.route("unknown")

    assert fallback.provider == "default"
    assert fallback.model == "default"
