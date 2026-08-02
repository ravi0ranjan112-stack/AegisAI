from pathlib import Path


class ProjectStats:
    def collect(self, root: str = ".") -> dict[str, int]:
        files = 0
        lines = 0

        for path in Path(root).rglob("*.py"):
            files += 1
            try:
                lines += len(
                    path.read_text(
                        encoding="utf-8",
                    ).splitlines()
                )
            except Exception:
                pass

        return {
            "files": files,
            "lines": lines,
        }
