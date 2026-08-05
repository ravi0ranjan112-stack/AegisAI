from aegis.runtime.app import AegisApp


def test_app() -> None:
    app = AegisApp()

    assert "AEGIS AI" in app.start()
    assert app.execute("hello") == "Aegis > You said: hello"
    assert app.execute("") == "Aegis > Please enter a command."
