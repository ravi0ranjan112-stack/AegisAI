from aegis.index.document import Document


class ProjectSearch:
    def search(
        self,
        docs: list[Document],
        query: str,
    ) -> str:
        matches: list[str] = []

        for doc in docs:
            if query.lower() in doc.text.lower():
                matches.append(doc.path)

        return "\n".join(matches) or "No matches."
