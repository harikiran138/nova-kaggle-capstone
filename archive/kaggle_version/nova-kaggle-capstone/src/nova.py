from src.agents.supervisor import Supervisor
from src.agents.coder import Coder
from src.agents.researcher import Researcher
from src.agents.fixer import Fixer

class Nova:
    def __init__(self):
        self.supervisor = Supervisor()
        self.agents = {
            "Coder": Coder(),
            "Researcher": Researcher(),
            "Fixer": Fixer()
        }

    def run_task(self, task):
        """
        Runs a single task through the Nova pipeline.
        """
        print(f"--- Processing Task: {task['id']} ---")
        agent_name = self.supervisor.route_task(task)
        print(f"Supervisor routed to: {agent_name}")
        
        if agent_name in self.agents:
            agent = self.agents[agent_name]
            result = agent.execute(task)
            return {
                "task_id": task["id"],
                "agent": agent_name,
                "status": "completed",
                "output": result
            }
        else:
            return {
                "task_id": task["id"],
                "agent": "None",
                "status": "failed",
                "output": "No suitable agent found."
            }
