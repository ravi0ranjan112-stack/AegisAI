from aegis.prompts.prompt import Prompt

_PROMPTS: dict[str, Prompt] = {}


class PromptStore:
    def execute(self, command: str) -> str:
        action, _, rest = command.partition(" ")

        if action == "add":
            name, _, text = rest.partition(" ")
            _PROMPTS[name] = Prompt(name, text)
            return "OK"

        if action == "show":
            prompt = _PROMPTS.get(rest)
            return prompt.text if prompt else "Not found"

        if action == "list":
            return "\n".join(sorted(_PROMPTS)) or "Empty"

        return "Usage: add|show|list"
