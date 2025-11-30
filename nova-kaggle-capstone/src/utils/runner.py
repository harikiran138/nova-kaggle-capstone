import json

def load_tasks(filepath):
    """
    Loads tasks from a JSON file.
    """
    with open(filepath, 'r') as f:
        return json.load(f)
