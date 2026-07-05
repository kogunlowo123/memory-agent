"""Memory Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_store_memory():
    """Test Store a memory with type classification and metadata."""
    tools = AgentTools()
    result = await tools.store_memory(content="test", memory_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_retrieve_memories():
    """Test Retrieve relevant memories for a given context."""
    tools = AgentTools()
    result = await tools.retrieve_memories(query="test", user_id="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_consolidate_memories():
    """Test Consolidate and compress related memories into summaries."""
    tools = AgentTools()
    result = await tools.consolidate_memories(user_id="test", time_window="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_forget_memories():
    """Test Remove memories matching privacy criteria or decay thresholds."""
    tools = AgentTools()
    result = await tools.forget_memories(user_id="test", criteria="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.memory_agent_agent import MemoryAgentAgent
    agent = MemoryAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
