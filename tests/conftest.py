"""Test configuration for Memory Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "memory-agent", "category": "AI Engineering"}
