from fastapi.testclient import TestClient
from app.main import app
import sys
import os
from unittest.mock import MagicMock, patch

client = TestClient(app)

# Mock the entire google.generativeai module since it might be an old version in this env
mock_genai = MagicMock()
mock_model_class = MagicMock()
mock_genai.GenerativeModel = mock_model_class

# Patch the module in sys.modules
@patch.dict(sys.modules, {'google.generativeai': mock_genai})
def test_run_task_coder():
    # Setup mock
    mock_model = MagicMock()
    mock_model.generate_content.return_value.text = "```python\nprint('Hello World')\n```"
    mock_model_class.return_value = mock_model
    
    # We need to reload the agents to pick up the mocked genai if they were already imported
    # But since we are patching sys.modules, if we patch before import it works.
    # However, app.main is already imported.
    # So we should patch where it is used.
    # Mock Supervisor routing to Coder
    with patch("app.agents.coder.genai", mock_genai), \
         patch("app.agents.supervisor.genai", mock_genai), \
         patch("app.agents.supervisor.Supervisor.route_task", return_value="Coder"), \
         patch.dict(os.environ, {"GOOGLE_API_KEY": "dummy"}):
        
        response = client.post("/api/run-task", json={"task": "Write a hello world script"})
        
    assert response.status_code == 200
    data = response.json()
    assert data["agent"] == "Coder"
    assert "print('Hello World')" in data["output"]

@patch.dict(sys.modules, {'google.generativeai': mock_genai})
def test_run_task_researcher():
    # Setup mock
    mock_model = MagicMock()
    mock_model.generate_content.return_value.text = "Python is a programming language."
    mock_model_class.return_value = mock_model
    
    with patch("app.agents.researcher.genai", mock_genai), \
         patch("app.agents.supervisor.genai", mock_genai), \
         patch("app.agents.supervisor.Supervisor.route_task", return_value="Researcher"), \
         patch.dict(os.environ, {"GOOGLE_API_KEY": "dummy"}):
        
        response = client.post("/api/run-task", json={"task": "What is Python?"})
        
    assert response.status_code == 200
    data = response.json()
    assert data["agent"] == "Researcher"
    assert "Python is a programming language" in data["output"]
