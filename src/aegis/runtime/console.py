class Console:
    def banner(self) -> str:
        return (
            "=================================\n"
            "        AEGIS AI v2.0\n"
            "================================="
        )

    def prompt(self) -> str:
        return "You > "

    def reply(self, text: str) -> str:
        return f"Aegis > {text}"
