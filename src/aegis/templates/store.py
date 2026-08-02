from aegis.templates.template import Template

_TEMPLATES: dict[str, Template] = {}


class TemplateStore:
    def execute(self, command: str) -> str:
        action, _, rest = command.partition(" ")

        if action == "add":
            name, _, text = rest.partition(" ")
            _TEMPLATES[name] = Template(name, text)
            return "OK"

        if action == "show":
            template = _TEMPLATES.get(rest)
            return template.text if template else "Not found"

        if action == "list":
            return "\n".join(sorted(_TEMPLATES)) or "Empty"

        return "Usage: add|show|list"
