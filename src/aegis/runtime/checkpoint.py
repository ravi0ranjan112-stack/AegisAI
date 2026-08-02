from aegis.runtime.session import RuntimeSession


class Checkpoint:
    def save(self, session: RuntimeSession) -> dict[str, str]:
        return dict(session.values)

    def load(
        self,
        session: RuntimeSession,
        data: dict[str, str],
    ) -> None:
        session.values.update(data)
