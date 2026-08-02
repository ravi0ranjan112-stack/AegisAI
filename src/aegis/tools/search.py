from aegis.index.indexer import ProjectIndexer
from aegis.index.search import ProjectSearch
from aegis.tools.base import BaseTool


class SearchTool(BaseTool):
    @property
    def name(self) -> str:
        return "search"

    def run(self, command: str) -> str:
        docs = ProjectIndexer().build(".")
        return ProjectSearch().search(docs, command)
