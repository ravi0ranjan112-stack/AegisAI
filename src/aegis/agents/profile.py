from dataclasses import dataclass


@dataclass(slots=True)
class AgentProfile:
    name: str
    system_prompt: str
