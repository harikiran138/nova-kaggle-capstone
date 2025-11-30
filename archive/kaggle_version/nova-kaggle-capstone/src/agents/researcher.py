import os

class Researcher:
    def __init__(self, docs_path="data/workspace_samples/docs.txt"):
        self.docs_path = docs_path

    def execute(self, task):
        """
        Searches the documentation for keywords related to the task.
        """
        description = task.get("description", "").lower()
        
        # Simple keyword extraction (very basic for demo)
        keywords = []
        if "release date" in description:
            keywords.append("release")
        
        results = []
        try:
            with open(self.docs_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    for kw in keywords:
                        if kw in line.lower():
                            results.append(line.strip())
        except FileNotFoundError:
            return f"Error: Documentation file not found at {self.docs_path}"

        if results:
            return "\n".join(results)
        return "No relevant information found."
