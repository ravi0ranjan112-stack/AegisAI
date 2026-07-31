import re

from aegis.agent.types import ToolCall

_PATTERN = re.compile(
    r"<tool:(?P<tool>\w+)>\s*(?P<command>.*?)\s*</tool>",
    re.DOTALL,
)


def parse_tool_call(text: str) -> ToolCall | None:
    match = _PATTERN.search(text)

    if match is None:
        return None

    return ToolCall(
        tool=match.group("tool"),
        command=match.group("command").strip(),
    )
