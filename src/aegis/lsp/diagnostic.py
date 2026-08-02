import ast


class DiagnosticEngine:
    def check(self, source: str) -> list[str]:
        try:
            ast.parse(source)
            return []
        except SyntaxError as e:
            return [f"{e.lineno}:{e.offset} {e.msg}"]
