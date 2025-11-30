import os
import google.generativeai as genai

class Fixer:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.0-flash-exp')

    def execute(self, task_description: str) -> str:
        if not hasattr(self, 'model'):
            return "Error: GOOGLE_API_KEY not configured."

        prompt = f"""
        You are a Fixer agent. Your goal is to analyze errors, bugs, or issues and provide a fix.
        
        Request: "{task_description}"
        
        Analyze the problem and provide a corrected solution or explanation of the fix.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Fixer error: {e}"
