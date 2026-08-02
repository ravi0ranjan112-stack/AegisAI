from aegis.templates.renderer import TemplateRenderer


class TemplateManager:
    def execute(self, command: str) -> str:
        return TemplateRenderer().execute(command)
