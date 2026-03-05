#!/bin/bash

echo "=========================================="
echo "🚀 Starting Quantum Operations Agent"
echo "=========================================="
echo ""
echo "📋 Agent Information:"
echo "  🔹 Name: Quantum Operations Agent"
echo "  🔹 Port: 8000"
echo "  🔹 Model: Mistral Small"
echo "  🔹 Role: Main Orchestrator"
echo ""
echo "=========================================="
echo ""

# Function to check if a port is in use
check_port() {
    if lsof -Pi :$1 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
        echo "⚠️  Warning: Port $1 is already in use"
        return 1
    fi
    return 0
}

# Check port before starting
echo "🔍 Checking port 8000..."
check_port 8000
echo ""

# Check if specialized agents are running
echo "🔍 Checking specialized agents..."
check_port 8001 && echo "⚠️  Developer Agent (8001) not detected" || echo "✅ Developer Agent (8001) running"
check_port 8002 && echo "⚠️  Status Agent (8002) not detected" || echo "✅ Status Agent (8002) running"
check_port 8003 && echo "⚠️  Computing Agent (8003) not detected" || echo "✅ Computing Agent (8003) running"
echo ""

# Start Operations Agent
echo "🚀 Starting Quantum Operations Agent on port 8000..."
echo "📦 Using uv to run the agent..."
echo ""
uv run server

echo ""
echo "=========================================="
echo "✅ Quantum Operations Agent started!"
echo "=========================================="
echo ""
echo "📊 Agent Details:"
echo "  🔹 URL: http://127.0.0.1:8000"
echo "  🔹 Model: Mistral Small"
echo "  🔹 Specialty: Main Orchestrator"
echo ""
echo "=========================================="
echo ""
echo "💡 Tips:"
echo "  - This agent orchestrates 3 specialized agents"
echo "  - Make sure all agents are running (8001, 8002, 8003)"
echo "  - Press Ctrl+C to stop the agent"
echo ""
echo "=========================================="