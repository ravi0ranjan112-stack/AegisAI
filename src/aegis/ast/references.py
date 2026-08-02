import ast

from aegis.ast.parser import ASTParser


class ReferenceFinder:
    def find(self, path: str, name: str) -> list[int]:
        tree = ASTParser().parse(path)

        for parent in ast.walk(tree):
            for child in ast.iter_child_nodes(parent):
                setattr(child, "_parent", parent)

        lines: list[int] = []

        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Name)
                and isinstance(node.ctx, ast.Load)
                and node.id == name
                and not isinstance(getattr(node, "_parent", None), ast.Return)
            ):
                lines.append(node.lineno)

        return sorted(set(lines))
