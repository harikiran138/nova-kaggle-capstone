# NOVA — Self-hosted AI Adaptive Learning Platform Implementation Plan

## Goal
Build a privacy-first, self-hosted AI tutor that converts content into personalized learning pathways.
**Target**: MVP with end-to-end ingestion, RAG, and offline-capable PWA.

## Tech Stack (MVP)
- **Infrastructure**: Docker Compose (Orchestration), MinIO (Storage), Redis (Cache), PostgreSQL (DB), Milvus (Vector DB).
- **Backend**: FastAPI (Python), Celery (Async Tasks), LangChain/LlamaIndex (RAG).
- **Frontend**: React + TypeScript + TailwindCSS + Vite (PWA).
- **AI/ML**: SentenceTransformers (Embeddings), vLLM/Ollama (Local LLM Inference).

## User Review Required
> [!IMPORTANT]
> **Hardware Requirements**: Running Milvus, MinIO, Postgres, Redis, and a Local LLM (e.g., Llama 3) requires significant RAM (16GB+ recommended) and Docker resources.
> **Clean Slate**: This plan assumes we are starting fresh or significantly restructuring the current repository. Old "Kaggle" files will be moved to an `archive/` folder to avoid confusion.

## Proposed Changes

### 1. Project Restructuring
- Move existing Kaggle capstone files to `archive/kaggle_version/`.
- Initialize new root structure:
  - `backend/`
  - `frontend/`
  - `infra/` (Docker configurations)
  - `scripts/`

### 2. Infrastructure (Docker Compose)
Create `docker-compose.yml` to spin up:
- **Postgres**: User data, course metadata.
- **Redis**: Celery broker, caching.
- **MinIO**: S3-compatible object storage for PDFs/images.
- **Milvus**: Vector database for embeddings.
- **Nova Backend**: FastAPI service.
- **Nova Worker**: Celery worker for ingestion tasks.
- **Nova Frontend**: Nginx/Vite dev server.

### 3. Backend Development (`backend/`)
- **Core**: FastAPI app setup, CORS, Database connection (SQLAlchemy + AsyncPG).
- **Auth**: JWT-based authentication (OAuth2PasswordBearer).
- **Models**: User, Course, Document, Quiz, Progress.
- **Ingestion Service**:
  - PDF parsing (PyMuPDF/OCR).
  - Chunking (RecursiveCharacterTextSplitter).
  - Embedding (HuggingFace local models).
  - Indexing into Milvus.
- **RAG Service**:
  - Retrieval chain setup.
  - Prompt engineering for "Tutor Mode".

### 4. Frontend Development (`frontend/`)
- **Setup**: Vite + React + TypeScript.
- **UI Lib**: TailwindCSS + Shadcn/UI (if requested) or Headless UI.
- **PWA**: Service Worker setup for offline caching (Workbox).
- **Pages**:
  - Landing/Login.
  - Dashboard (Student/Teacher).
  - Course Player (Video/Text/Quiz).
  - Upload/Admin Panel.

## Verification Plan

### Automated Tests
- **Backend**: Pytest for API endpoints (Auth, Ingestion trigger).
- **Frontend**: Vitest for component rendering.

### Manual Verification
1.  **Infrastructure Up**: Run `docker-compose up` and verify all containers are healthy.
2.  **Ingestion Loop**: Upload a sample PDF via API/UI -> Verify chunks in Milvus.
3.  **RAG Query**: Ask a question about the PDF -> Verify answer + citations.
4.  **Offline PWA**: Disconnect network -> Verify app loads and cached content is accessible.
