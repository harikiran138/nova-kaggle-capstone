class Supervisor:
    def __init__(self):
        self.agents = {
            "code": "Coder",
            "research": "Researcher",
            "fix": "Fixer"
        }

    def route_task(self, task):
        """
        Decides which agent should handle the task based on the 'type' field.
        """
        task_type = task.get("type")
        if task_type in self.agents:
            return self.agents[task_type]
        else:
            return "Unknown"
