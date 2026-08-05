from aegis.context.context import Context


class ContextInjector:
    def inject(self, prompt: str, context: Context) -> str:
        if not context.items:
            return prompt

        joined = "\n".join(context.items)
        return f"Context:\n{joined}\n\nUser: {prompt}"
