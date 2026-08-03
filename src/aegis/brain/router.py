from aegis.brain.intent import Intent
from aegis.tools.conversation import ConversationTool
from aegis.tools.lsp import LSPTool
from aegis.tools.memory import MemoryTool
from aegis.tools.vector import VectorTool


class ToolRouter:
    def __init__(self) -> None:
        self._tools = {
            "conversation": ConversationTool(),
            "lsp": LSPTool(),
            "memory": MemoryTool(),
            "vector": VectorTool(),
        }

    def execute(self, intent: Intent) -> str:
        tool = self._tools[intent.tool]
        return tool.run(intent.command)
