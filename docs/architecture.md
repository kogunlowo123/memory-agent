# Memory Agent Architecture

AI memory management agent that implements short-term, long-term, and episodic memory for conversational AI systems, with memory consolidation, retrieval, decay, and privacy-aware forgetting capabilities.

## Domain Tools

- **store_memory**: Store a memory with type classification and metadata
- **retrieve_memories**: Retrieve relevant memories for a given context
- **consolidate_memories**: Consolidate and compress related memories into summaries
- **forget_memories**: Remove memories matching privacy criteria or decay thresholds
- **get_memory_stats**: Get memory usage statistics and health metrics