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
