import re

from aegis.agent.types import ToolCall

_XML = re.compile(
    r"<tool:(?P<tool>\w+)>\s*(?P<command>.*?)\s*</tool>",
    re.DOTALL,
)

_BASH = re.compile(
    r"```(?:bash|sh)?\n(?P<command>.*?)```",
    re.DOTALL,
)

_ALLOWED = {
    "pwd",
    "ls",
    "git status",
    "pytest",
    "ruff",
    "mypy",
}


def parse_tool_call(text: str) -> ToolCall | None:
    text = text.strip()

    match = _XML.search(text)
    if match:
        return ToolCall(
            tool=match.group("tool"),
            command=match.group("command").strip(),
        )

    match = _BASH.search(text)
    if match:
        command = match.group("command").strip()
        if command in _ALLOWED:
            return ToolCall(
                tool="shell",
                command=command,
            )

    if text in _ALLOWED:
        return ToolCall(
            tool="shell",
            command=text,
        )

    return None
