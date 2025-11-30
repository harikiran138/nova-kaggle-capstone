import os

class Fixer:
    def __init__(self, workspace_path="data/workspace_samples"):
        self.workspace_path = workspace_path

    def execute(self, task):
        """
        Fixes known bugs in files.
        """
        # For demo purposes, we look for specific file targets in the description
        target_file = "buggy_code.py"
        file_path = os.path.join(self.workspace_path, target_file)
        
        if target_file in task.get("description", ""):
            return self._fix_buggy_code(file_path)
        
        return "No fix applied."

    def _fix_buggy_code(self, file_path):
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Deterministic fix: replace Python 2 print with Python 3 print
            if 'print "Hello, " + name' in content:
                fixed_content = content.replace('print "Hello, " + name', 'print("Hello, " + name)')
                
                with open(file_path, 'w') as f:
                    f.write(fixed_content)
                
                return f"Fixed syntax error in {file_path}"
            
            return f"No known bugs found in {file_path}"
            
        except FileNotFoundError:
            return f"Error: File {file_path} not found."
