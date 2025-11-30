import os
import google.generativeai as genai
import json

class Supervisor:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            print("Warning: GOOGLE_API_KEY not found.")
        else:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.0-flash-exp')

    def route_task(self, task_description: str) -> str:
        """
        Analyzes the task description and routes it to the appropriate agent:
        - Coder: For writing, debugging, or explaining code.
        - Researcher: For finding information, summarizing docs, or answering general questions.
        - Fixer: For fixing specific errors or bugs provided in the task.
        
        Returns: "Coder", "Researcher", or "Fixer"
        """
        if not hasattr(self, 'model'):
             return "Researcher" # Default fallback

        prompt = f"""
        You are a Supervisor agent in a multi-agent system.
        Your job is to route the following task to the most appropriate agent.
        
        Agents:
        1. Coder: Writes code, refactors code, explains code, builds applications.
        2. Researcher: Searches for information, answers questions, summarizes text, explains concepts.
        3. Fixer: Fixes specific bugs, errors, or issues in provided code or logs.

        Task: "{task_description}"

        Return ONLY the name of the agent (Coder, Researcher, or Fixer) as a JSON object with key "agent".
        Example: {{"agent": "Coder"}}
        """
        
        try:
            response = self.model.generate_content(prompt)
            text = response.text.strip()
            # Clean up potential markdown code blocks
            if text.startswith("```json"):
                text = text[7:-3]
            elif text.startswith("```"):
                text = text[3:-3]
            
            data = json.loads(text)
            return data.get("agent", "Researcher")
        except Exception as e:
            print(f"Supervisor routing error: {e}")
            return "Researcher"
