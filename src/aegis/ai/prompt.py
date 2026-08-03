class PromptBuilder:
    def build(self, user: str, context: str = "") -> str:
        if context:
            return f"{context}\n\nUser: {user}"
        return user
