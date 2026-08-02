from aegis.tools.agent import AgentTool
from aegis.tools.config import ConfigTool
from aegis.tools.file import FileTool
from aegis.tools.git import GitTool
from aegis.tools.memory import MemoryTool
from aegis.tools.patch import PatchTool
from aegis.tools.plugin import PluginTool
from aegis.tools.profile import ProfileTool
from aegis.tools.project import ProjectTool
from aegis.tools.prompt import PromptTool
from aegis.tools.python import PythonTool
from aegis.tools.rag import RagTool
from aegis.tools.registry import ToolRegistry
from aegis.tools.runtime import RuntimeTool
from aegis.tools.search import SearchTool
from aegis.tools.shell import ShellTool
from aegis.tools.skill import SkillTool
from aegis.tools.task import TaskTool
from aegis.tools.template import TemplateTool
from aegis.tools.workflow import WorkflowTool
from aegis.tools.workspace import WorkspaceTool


class ToolFactory:
    @staticmethod
    def create_registry() -> ToolRegistry:
        registry = ToolRegistry()

        registry.register(ShellTool())
        registry.register(FileTool())
        registry.register(GitTool())
        registry.register(SearchTool())
        registry.register(MemoryTool())
        registry.register(ProjectTool())
        registry.register(PatchTool())
        registry.register(WorkspaceTool())
        registry.register(TaskTool())
        registry.register(WorkflowTool())
        registry.register(SkillTool())
        registry.register(RuntimeTool())
        registry.register(PluginTool())
        registry.register(ConfigTool())
        registry.register(ProfileTool())
        registry.register(TemplateTool())
        registry.register(PromptTool())
        registry.register(AgentTool())
        registry.register(RagTool())
        registry.register(PythonTool())

        return registry
