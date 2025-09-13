# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PQC Inspector is an AI-based system for detecting non-quantum-resistant cryptography (Non-PQC) usage in source code, binaries, configuration files, and parameters. The system helps organizations transition to post-quantum cryptography (PQC).

The system uses a multi-agent architecture:
- **Orchestrator Controller**: Classifies uploaded files and routes them to appropriate specialized agents
- **Specialized Agents**: Analyze different file types (source code, binaries, parameters, logs/configs)
- **External API Client**: Communicates with external APIs for data storage and retrieval
- **Background Processing**: Analysis runs asynchronously with task ID tracking

## Development Commands

### Running the Application

**Local Development on MacBook Pro M4 24GB**:
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server with auto-reload
uvicorn main:app --reload
```

**Direct Python execution**:
```bash
python main.py
```

### Environment Setup

Create a `.env` file in the project root with configuration:
```
LOG_LEVEL=INFO
EXTERNAL_API_BASE_URL="https://api.example.com/v1"
EXTERNAL_API_KEY="your-api-key-here"
```

### Ollama Model Setup

This project uses Ollama for AI model inference on MacBook Pro M4 24GB. Required models:
- **Orchestrator**: `gemma:7b`
- **Source Code & Binary Agents**: `codellama:7b`
- **Parameter & Log Agents**: `gemma:7b`

Install models with Ollama:
```bash
ollama pull gemma:7b
ollama pull codellama:7b
```

### API Endpoints

- `GET /`: Health check endpoint
- `POST /api/v1/analyze`: Submit file for analysis (returns task_id)
- `GET /api/v1/report/{task_id}`: Get analysis results by task ID
- Interactive API docs: `http://localhost:8000/docs`

## Architecture Details

### Core Components

**main.py**: FastAPI application entry point with router registration
- Creates FastAPI app with Korean description
- Registers API routes under `/api/v1` prefix
- Includes health check endpoint

**pqc_inspector_server/orchestrator/controller.py**: Central orchestration logic
- `OrchestratorController` manages file classification and agent delegation
- File type classification based on extensions (source_code, binary, parameter, log_conf)
- Coordinates with external API client for result storage
- Uses dependency injection for API client

**pqc_inspector_server/api/endpoints.py**: HTTP API layer
- Async file upload handling with background task processing
- Returns task IDs immediately while analysis runs in background
- Result retrieval by task ID

**pqc_inspector_server/core/config.py**: Configuration management
- Uses Pydantic BaseSettings for environment variable handling
- Cached settings instance with `@lru_cache`
- External API configuration

### Agent System

The system includes specialized agents in `pqc_inspector_server/agents/`:
- `source_code.py`: Analyzes programming language files (uses CodeLlama 7B)
- `binary.py`: Analyzes binary executables (uses CodeLlama 7B)
- `parameter.py`: Analyzes configuration files (uses Gemma 7B)
- `log_conf.py`: Analyzes log and configuration files (uses Gemma 7B)

### File Type Classification

File extensions mapped to agent types:
- Source code: `.py`, `.c`, `.java`, `.go`
- Parameters: `.json`, `.yaml`, `.yml`, `.xml`
- Logs/Config: `.log`, `.conf`, `.ini`
- Binary: All other file types (default)

### External API Integration

- External API client for storing and retrieving analysis results
- `pqc_inspector_server/db/db_client.py`: API client (needs renaming to api_client.py)
- Async HTTP operations with proper dependency injection
- Results stored with task IDs for later retrieval
- Mock/test API endpoints for development

## Development Notes

- Project uses Korean comments and documentation extensively
- FastAPI with async/await pattern throughout
- Background task processing for file analysis
- Ollama integration optimized for MacBook Pro M4 24GB
- Requirements.txt needs proper dependencies: fastapi, uvicorn, pydantic-settings, httpx, ollama
- Fine-tuning data available in `data/fine_tuning_data/`
- RAG knowledge base structure in `data/rag_knowledge_base/`
- External API integration replaces direct database access