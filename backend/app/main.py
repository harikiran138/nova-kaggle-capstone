from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="NOVA Learning Platform API", version="0.1.0")

# CORS Configuration
origins = [
    "http://localhost:5173",  # Vite Frontend
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to NOVA Learning Platform API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Agent Integration
from app.agents.supervisor import Supervisor
from app.agents.coder import Coder
from app.agents.researcher import Researcher
from app.agents.fixer import Fixer
from pydantic import BaseModel

class TaskRequest(BaseModel):
    task: str

@app.post("/api/run-task")
async def run_task(request: TaskRequest):
    supervisor = Supervisor()
    agent_type = supervisor.route_task(request.task)
    
    response = {"agent": agent_type, "status": "completed", "output": ""}
    
    if agent_type == "Coder":
        agent = Coder()
        response["output"] = agent.execute(request.task)
    elif agent_type == "Fixer":
        agent = Fixer()
        response["output"] = agent.execute(request.task)
    else: # Default to Researcher
        agent = Researcher()
        response["output"] = agent.execute(request.task)
        
    return response
