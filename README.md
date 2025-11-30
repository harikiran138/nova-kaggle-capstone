# NOVA — Self-hosted AI Adaptive Learning Platform

NOVA is a privacy-first, self-hosted AI tutor that converts textbooks into personalized learning pathways.

## Tech Stack
- **Frontend**: React, TypeScript, TailwindCSS, Vite
- **Backend**: FastAPI, Python 3.11
- **Database**: PostgreSQL
- **Vector DB**: Milvus
- **Storage**: MinIO
- **Cache**: Redis
- **Infrastructure**: Docker Compose

## Prerequisites
- Docker & Docker Compose
- Node.js 18+ (for local frontend dev if not using Docker)
- 16GB+ RAM recommended

## Quick Start

1. **Start the Infrastructure**
   ```bash
   docker-compose up --build
   ```
   This will start all services:
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000/docs
   - MinIO Console: http://localhost:9001
   - Milvus: http://localhost:19530

2. **Development**
   - **Backend**: The `backend/` directory is mounted, so changes will auto-reload.
   - **Frontend**: The `frontend/` directory is mounted.

## Directory Structure
```
nova-learning-platform/
├── backend/            # FastAPI Application
├── frontend/           # React Application
├── infra/              # Infrastructure Configs
├── archive/            # Archived Kaggle Project
└── docker-compose.yml  # Main Orchestration
```

## Features (MVP)
- [x] Docker Infrastructure Setup
- [x] FastAPI Backend Skeleton
- [x] React Frontend Skeleton
- [ ] PDF Ingestion Pipeline
- [ ] RAG Q/A Service
- [ ] Offline PWA Mode
