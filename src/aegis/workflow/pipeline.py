from aegis.workflow.runner import WorkflowRunner


class Pipeline:
    def run(self, command: str) -> str:
        return WorkflowRunner().execute(command)
