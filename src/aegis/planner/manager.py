from aegis.planner.planner import Planner


class PlannerManager:
    def __init__(self) -> None:
        self._planner = Planner()

    def execute(self, command: str):
        return self._planner.create(command)
