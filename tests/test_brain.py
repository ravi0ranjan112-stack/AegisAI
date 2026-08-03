from aegis.brain.intent import Intent, IntentDetector
from aegis.brain.router import ToolRouter


def test_intent_detector() -> None:
    detector = IntentDetector()

    assert detector.detect("remember hello").tool == "memory"
    assert detector.detect("diagnostics main.py").tool == "lsp"
    assert detector.detect("add python").tool == "vector"
    assert detector.detect("hello").tool == "conversation"


def test_router() -> None:
    router = ToolRouter()

    assert router.execute(Intent("memory", "remember hello")) == "OK"
    assert router.execute(Intent("conversation", "user hi")) == "OK"
