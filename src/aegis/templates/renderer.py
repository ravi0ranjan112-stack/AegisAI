from aegis.templates.store import TemplateStore


class TemplateRenderer:
    def execute(self, command: str) -> str:
        return TemplateStore().execute(command)
