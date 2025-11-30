class Coder:
    def execute(self, task):
        """
        Generates code based on the task description.
        For this deterministic demo, it uses a template for specific task IDs.
        """
        task_id = task.get("id")
        
        if task_id == "task_001":
            return self._generate_factorial()
        
        return "# No code generated for this task."

    def _generate_factorial(self):
        return """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
"""
