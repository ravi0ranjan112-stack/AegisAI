from aegis.runtime.console import Console


def test_console() -> None:
    console = Console()

    assert "AEGIS AI" in console.banner()
    assert console.prompt() == "You > "
    assert console.reply("Hello") == "Aegis > Hello"
