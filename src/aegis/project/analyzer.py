from aegis.project.filetree import FileTree
from aegis.project.stats import ProjectStats


class ProjectAnalyzer:
    def summary(self) -> str:
        stats = ProjectStats().collect()
        tree = FileTree().build()

        return (
            f"Python files: {stats['files']}\nLines: {stats['lines']}\nFiles indexed: {len(tree)}"
        )
