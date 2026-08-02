from dataclasses import dataclass

from aegis.agent.history import AgentHistory


@dataclass(slots=True)
class LoopResult:
    handled: bool
    result: str
    history: AgentHistory
