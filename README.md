# Memory Agent

[![CI](https://github.com/kogunlowo123/memory-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/memory-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: AI Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

AI memory management agent that implements short-term, long-term, and episodic memory for conversational AI systems, with memory consolidation, retrieval, decay, and privacy-aware forgetting capabilities.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `store_memory` | Store a memory with type classification and metadata |
| `retrieve_memories` | Retrieve relevant memories for a given context |
| `consolidate_memories` | Consolidate and compress related memories into summaries |
| `forget_memories` | Remove memories matching privacy criteria or decay thresholds |
| `get_memory_stats` | Get memory usage statistics and health metrics |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/memory/store` | Store a memory |
| `POST` | `/api/v1/memory/retrieve` | Retrieve memories |
| `POST` | `/api/v1/memory/consolidate` | Consolidate memories |
| `POST` | `/api/v1/memory/forget` | Forget memories |
| `GET` | `/api/v1/memory/stats` | Get memory statistics |

## Features

- Short Term Memory
- Long Term Memory
- Episodic Memory
- Memory Consolidation
- Privacy Forgetting

## Integrations

- Pinecone
- Neo4J
- Redis
- Weaviate
- Qdrant

## Architecture

```
memory-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── memory_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Vector Databases + Graph Databases + LLM**

---

Built as part of the Enterprise AI Agent Platform.
