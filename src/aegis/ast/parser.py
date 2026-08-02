import ast
from pathlib import Path


class ASTParser:
    def parse(self, path: str) -> ast.AST:
        return ast.parse(Path(path).read_text(encoding="utf-8"))
