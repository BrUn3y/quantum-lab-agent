# ⚡ Quantum Operations Agent - Quick Start Guide

Get the Quantum Operations Agent running in 5 minutes! This is the main orchestrator that coordinates all specialized quantum agents.

## 🎯 What is This Agent?

The **Quantum Operations Agent** is the central coordinator that:
- 🎯 Routes requests to specialized agents (Developer, Status, Computing)
- 🔄 Combines multi-agent capabilities
- 🛠️ Provides unified interface for quantum computing tasks
- 📊 Manages complex quantum workflows

**Port**: 8000 (Main Orchestrator)

## 📋 Prerequisites

Before starting, ensure you have:

1. **Python 3.11+** installed
   ```bash
   python --version  # Should be 3.11 or higher
   ```

2. **uv package manager** installed
   ```bash
   # Install uv if you don't have it
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **IBM Watsonx API Key** (for LLM)
   - Get it from: https://cloud.ibm.com/

4. **IBM Quantum Token** (optional, for quantum operations)
   - Get it from: https://quantum.ibm.com/

5. **Specialized Agents Running** (recommended)
   - Developer Agent on port 8001
   - Status Agent on port 8002
   - Computing Agent on port 8003

## 🚀 Quick Setup (3 Steps)

### Step 1: Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit with your credentials
nano .env  # or use your preferred editor
```

**Minimum required configuration**:
```bash
# IBM Watsonx (Required)
WATSONX_API_KEY=your_watsonx_api_key_here
WATSONX_PROJECT_ID=your_project_id_here
WATSONX_URL=https://us-south.ml.cloud.ibm.com

# IBM Quantum (Optional)
IBM_QUANTUM_TOKEN=your_ibm_quantum_token_here

# Specialized Agent URLs (if running separately)
DEVELOPER_AGENT_URL=http://127.0.0.1:8001
STATUS_AGENT_URL=http://127.0.0.1:8002
COMPUTING_AGENT_URL=http://127.0.0.1:8003
```

### Step 2: Install Dependencies

```bash
# Install all dependencies with uv
uv sync
```

This will:
- ✅ Install all Python dependencies
- ✅ Set up the virtual environment
- ✅ Lock dependency versions

### Step 3: Start the Agent

**Option A: Using the start script** (Recommended)
```bash
chmod +x start.sh
./start.sh
```

**Option B: Using uv directly**
```bash
uv run server
```

**Option C: Using Docker**
```bash
docker build -t quantum-operations-agent .
docker run -p 8000:8000 --env-file .env quantum-operations-agent
```

## ✅ Verify It's Working

### Check Agent Health
```bash
curl http://127.0.0.1:8000/health
```

Expected response:
```json
{"status": "healthy"}
```

### Test Agent Communication
```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, what can you do?"}'
```

## 🎮 Basic Usage Examples

### Example 1: Complete Quantum Workflow
```
"Create a Bell state circuit, check available backends, and execute it"
```
The Operations Agent will:
1. Route to Developer Agent → Generate code
2. Route to Status Agent → Check backends
3. Route to Computing Agent → Execute circuit

### Example 2: Code Generation
```
"Generate a quantum teleportation circuit in QASM"
```
Routes to Developer Agent for code generation.

### Example 3: Status Check
```
"What quantum backends are available right now?"
```
Routes to Status Agent for backend information.

### Example 4: Circuit Execution
```
"Run this circuit on a simulator: [QASM code]"
```
Routes to Computing Agent for execution.

## 🏃 Running the Complete System

For full functionality, run all agents:

### Terminal 1: Developer Agent
```bash
cd ../quantum-developer-agent
./start.sh
```

### Terminal 2: Status Agent
```bash
cd ../quantum-status-agent
./start.sh
```

### Terminal 3: Computing Agent
```bash
cd ../quantum-computing-agent
./start.sh
```

### Terminal 4: Operations Agent (This Agent)
```bash
cd ../quantum-operations-agent
./start.sh
```

### Verify All Agents
```bash
# Check all agents are running
curl http://127.0.0.1:8001/health  # Developer
curl http://127.0.0.1:8002/health  # Status
curl http://127.0.0.1:8003/health  # Computing
curl http://127.0.0.1:8000/health  # Operations
```

## 🐳 Docker Quick Start

### Single Agent
```bash
# Build
docker build -t quantum-operations-agent .

# Run
docker run -p 8000:8000 \
  -e WATSONX_API_KEY=your_key \
  -e WATSONX_PROJECT_ID=your_project \
  -e IBM_QUANTUM_TOKEN=your_token \
  quantum-operations-agent
```

### All Agents with Docker Compose
Create `docker-compose.yml`:
```yaml
version: '3.8'
services:
  developer:
    build: ../quantum-developer-agent
    ports: ["8001:8001"]
    env_file: ../quantum-developer-agent/.env
  
  status:
    build: ../quantum-status-agent
    ports: ["8002:8002"]
    env_file: ../quantum-status-agent/.env
  
  computing:
    build: ../quantum-computing-agent
    ports: ["8003:8003"]
    env_file: ../quantum-computing-agent/.env
  
  operations:
    build: .
    ports: ["8000:8000"]
    env_file: .env
    depends_on: [developer, status, computing]
```

Run:
```bash
docker-compose up
```

## 🔧 Troubleshooting

### Issue: Port 8000 already in use
```bash
# Find what's using the port
lsof -i :8000

# Kill the process
kill -9 <PID>
```

### Issue: Can't reach specialized agents
**Solution**: Ensure all specialized agents are running:
```bash
# Check each agent
curl http://127.0.0.1:8001/health  # Developer
curl http://127.0.0.1:8002/health  # Status
curl http://127.0.0.1:8003/health  # Computing
```

### Issue: Authentication errors
**Solution**: Verify your `.env` file has correct credentials:
```bash
# Check your .env file
cat .env | grep -E "WATSONX_API_KEY|IBM_QUANTUM_TOKEN"
```

### Issue: Module not found errors
**Solution**: Reinstall dependencies:
```bash
rm -rf .venv
uv sync
```

### Issue: Agent not responding
**Solution**: Check logs and restart:
```bash
# If using start.sh, check terminal output
# If using Docker:
docker logs <container-id>

# Restart the agent
./start.sh
```

## 📊 Agent Architecture

```
┌─────────────────────────────────┐
│   Quantum Operations Agent      │
│        (Port 8000)              │
│   🎯 Main Orchestrator          │
└────────┬────────────────────────┘
         │
    ┌────┴────┬────────┬──────────┐
    │         │        │          │
┌───▼───┐ ┌──▼───┐ ┌──▼────┐    │
│ Dev   │ │Status│ │Compute│    │
│ 8001  │ │ 8002 │ │ 8003  │    │
└───────┘ └──────┘ └───────┘    │
                                 │
                            User Request
```

## 📚 Next Steps

1. **Read the full README.md** for detailed documentation
2. **Explore specialized agents**:
   - [Developer Agent](../quantum-developer-agent/QUICKSTART.md)
   - [Status Agent](../quantum-status-agent/QUICKSTART.md)
   - [Computing Agent](../quantum-computing-agent/QUICKSTART.md)
3. **Try complex workflows** combining multiple agents
4. **Customize** the agent for your specific needs

## 💡 Tips

- **Start specialized agents first** before starting Operations Agent
- **Use Docker Compose** for easy multi-agent deployment
- **Check logs** if something doesn't work as expected
- **Verify ports** are not in use before starting agents
- **Keep credentials secure** - never commit `.env` files

## 🆘 Need Help?

- 📖 Check the [full README.md](README.md)
- 🐛 Open an issue on GitHub
- 💬 Review specialized agent documentation
- 🔍 Check agent logs for error messages

---
