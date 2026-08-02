import ast

from aegis.ast.parser import ASTParser


class SymbolExtractor:
    def extract(self, path: str) -> list[str]:
        tree = ASTParser().parse(path)

        names: list[str] = []

        for node in ast.walk(tree):
            if isinstance(
                node,
                (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef),
            ):
                names.append(node.name)

        return sorted(names)
