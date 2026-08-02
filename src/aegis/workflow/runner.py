from aegis.workflow.registry import WorkflowRegistry

_REGISTRY = WorkflowRegistry()


class WorkflowRunner:
    def execute(self, command: str) -> str:
        action, _, rest = command.partition(" ")

        if action == "create":
            return _REGISTRY.create(rest)

        if action == "add":
            name, _, step = rest.partition(" ")
            workflow = _REGISTRY.get(name)

            if workflow is None:
                return "Not found"

            workflow.add(step)
            return "OK"

        if action == "show":
            workflow = _REGISTRY.get(rest)

            if workflow is None:
                return "Not found"

            return "\n".join(workflow.steps) or "Empty"

        return "Usage: create|add|show"
