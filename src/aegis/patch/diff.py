import difflib


class DiffGenerator:
    def create(
        self,
        old: str,
        new: str,
    ) -> str:
        return "".join(
            difflib.unified_diff(
                old.splitlines(True),
                new.splitlines(True),
                fromfile="before",
                tofile="after",
            )
        )
