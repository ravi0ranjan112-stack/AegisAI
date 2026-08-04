from aegis.workflow.workflow import Workflow


class WorkflowEngine:
    def create(self, name: str) -> Workflow:
        wf = Workflow(name)
        wf.add("Start")
        wf.add("Execute")
        wf.add("Finish")
        return wf
