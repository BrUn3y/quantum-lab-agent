"""
Quantum Operations Agent - Main Orchestrator

This agent is the main entry point that orchestrates communication
between the Developer, Status, and Computing agents via A2A protocol.

Model: mistralai/mistral-small-3-1-24b-instruct-2503 (Watsonx)
Port: 8000
Type: Main A2A Server + A2A Clients
"""

__version__ = "1.0.0"
__author__ = "Edgar Bruney"

from .tools import (
    QuantumDeveloperClient,
    QuantumStatusClient,
    QuantumComputingClient,
)

__all__ = [
    "QuantumDeveloperClient",
    "QuantumStatusClient",
    "QuantumComputingClient",
]