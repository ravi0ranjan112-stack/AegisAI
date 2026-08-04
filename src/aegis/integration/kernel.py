from aegis.agent.manager import AgentManager
from aegis.memory.manager_v2 import MemoryManagerV2
from aegis.workflow.manager import WorkflowManager


class IntegrationKernel:
    def __init__(self) -> None:
        self.agent = AgentManager()
        self.memory = MemoryManagerV2()
        self.workflow = WorkflowManager()
