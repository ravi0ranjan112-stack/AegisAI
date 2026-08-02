import ast

from aegis.ast.parser import ASTParser


class DependencyGraph:
    def build(self, path: str) -> dict[str, list[str]]:
        tree = ASTParser().parse(path)
        assert isinstance(tree, ast.Module)

        graph: dict[str, list[str]] = {}

        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                calls: list[str] = []

                for child in ast.walk(node):
                    if isinstance(child, ast.Call) and isinstance(child.func, ast.Name):
                        calls.append(child.func.id)

                graph[node.name] = sorted(set(calls))

        return graph
