import os
import google.generativeai as genai

class Researcher:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.0-flash-exp')

    def execute(self, task_description: str) -> str:
        if not hasattr(self, 'model'):
            return "Error: GOOGLE_API_KEY not configured."

        prompt = f"""
        You are a Researcher agent. Your goal is to provide accurate information, summaries, or explanations based on the user's request.
        
        Request: "{task_description}"
        
        Provide a comprehensive and well-structured response.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Researcher error: {e}"
