from src.utils.sandbox import run_code
import os

class Evaluator:
    def __init__(self):
        pass

    def evaluate(self, results):
        """
        Evaluates the results of the tasks.
        """
        scores = []
        
        for res in results:
            task_id = res["task_id"]
            output = res["output"]
            score = 0
            feedback = ""
            
            if task_id == "task_001":
                # Verify factorial code
                test_code = output + "\nassert factorial(5) == 120\nprint('Test Passed')"
                out, err = run_code(test_code)
                if "Test Passed" in out:
                    score = 1
                    feedback = "Factorial function works correctly."
                else:
                    feedback = f"Test failed. Error: {err}"
            
            elif task_id == "task_002":
                # Verify research
                if "2025" in output:
                    score = 1
                    feedback = "Correct release date found."
                else:
                    feedback = "Incorrect or missing information."
            
            elif task_id == "task_003":
                # Verify fix
                # Check if file runs without error now
                try:
                    # We need to run the file itself
                    file_path = "data/workspace_samples/buggy_code.py"
                    with open(file_path, 'r') as f:
                        code = f.read()
                    out, err = run_code(code)
                    if not err:
                        score = 1
                        feedback = "File runs successfully."
                    else:
                        feedback = f"File still errors: {err}"
                except Exception as e:
                    feedback = f"Evaluation error: {e}"
            
            scores.append({
                "task_id": task_id,
                "score": score,
                "feedback": feedback
            })
            
        return scores
