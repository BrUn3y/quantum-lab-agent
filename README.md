# 🎯 Quantum Operations Agent

**Main Orchestrator for Quantum Computing Multi-Agent System**

The Quantum Operations Agent is the central coordinator that orchestrates communication between three specialized quantum computing agents. It acts as the main entry point for users, intelligently routing requests to the appropriate specialized agent and combining their capabilities to provide comprehensive quantum computing solutions.

The orchestrator uses Granite 4 Small H locally through Ollama (`ollama:granite4:small-h`).

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                  Quantum Operations Agent                    │
│                    (Port 8000 - Main)                        │
│                                                              │
│  🎯 Main Orchestrator & Coordinator                         │
│  • Routes requests to specialized agents                     │
│  • Combines multi-agent responses                           │
│  • Manages complex quantum workflows                        │
└──────────────────┬──────────────────┬──────────────────────┘
                   │                  │
        ┌──────────┴────────┐  ┌─────┴──────────┐
        │                   │  │                 │
┌───────▼────────┐  ┌──────▼──────┐  ┌─────────▼────────┐
│   Developer    │  │   Status    │  │    Computing     │
│     Agent      │  │    Agent    │  │      Agent       │
│  (Port 8001)   │  │ (Port 8002) │  │   (Port 8003)    │
│                │  │             │  │                  │
│ 💻 Code Gen    │  │ 📊 Status   │  │ ⚛️  Execution   │
│ • QASM/Qiskit  │  │ • Backends  │  │ • Run Circuits  │
│ • Explanations │  │ • Jobs      │  │ • Real Hardware │
│ • Algorithms   │  │ • Results   │  │ • Simulators    │
└────────────────┘  └─────────────┘  └──────────────────┘
```

## 🌟 Key Features

### 🎯 Intelligent Request Routing
- Automatically determines which specialized agent to invoke
- Routes quantum code generation to Developer Agent
- Routes status queries to Status Agent
- Routes circuit execution to Computing Agent

### 🔄 Multi-Agent Coordination
- Combines capabilities of all three specialized agents
- Manages complex workflows requiring multiple agents
- Provides unified interface for quantum computing tasks

### 🛠️ A2A Communication
- Uses Agent-to-Agent (A2A) protocol for inter-agent messaging
- Maintains separate client tools for each specialized agent
- Handles agent discovery and communication

### 📊 Comprehensive Capabilities
Through its specialized agents, provides:
- **Code Generation**: QASM, Qiskit, quantum algorithms
- **Status Monitoring**: Backend availability, job tracking
- **Circuit Execution**: Real quantum hardware and simulators
- **Result Analysis**: Job results, histograms, visualizations


## 📦 Project Dependencies

### Main Dependencies (pyproject.toml)

```toml
[project]
requires-python = ">=3.11,<4.0"
dependencies = [
    "agentstack-sdk==0.4.0rc1",      # Framework for creating agents
    "beeai_framework[a2a]>=0.1.76",  # BeeAI Framework with A2A support
    "python-dotenv>=1.0.0",           # Environment variable management
    "grpcio>=1.60.0",                 # gRPC for A2A communication
    "grpcio-tools>=1.60.0",           # gRPC tools
]
```

**Important note**: This agent uses `beeai_framework[a2a]` which includes the necessary dependencies for Agent-to-Agent (A2A) communication via gRPC.

### System Dependencies

1. **Python 3.11+**
   ```bash
   python --version  # Must be 3.11 or higher
   ```

2. **uv** (Package Manager - Recommended)
   ```bash
   # Install uv
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # Verify installation
   uv --version
   ```

3. **IBM Watsonx** (Credentials required)
   - Watsonx API Key
   - Watsonx Project ID
   - Get them at: https://cloud.ibm.com/

4. **Specialized Agents** (Must be running)
   - Developer Agent on port 8001
   - Status Agent on port 8002
   - Computing Agent on port 8003

## 🎯 Specific Purpose

This agent is the **main orchestrator** of the quantum computing multi-agent system:

**Responsibilities:**
- ✅ Receive user requests
- ✅ Analyze intent and determine which agent(s) to invoke
- ✅ Coordinate communication between specialized agents via A2A
- ✅ Combine responses from multiple agents
- ✅ Manage complex workflows
- ✅ Provide unified interface to the user
- ✅ **ENSURE that Job ID is always included in execution responses**

**Agents it coordinates:**
1. **Developer Agent** (8001) - QASM/Qiskit code generation
2. **Status Agent** (8002) - Status queries and results
3. **Computing Agent** (8003) - Circuit execution

**Typical workflows:**
- User asks "create and execute" → Developer + Computing
- User asks "execute code" → Computing
- User asks "job status" → Status
- User asks "available backends" → Status

**Communication:**
- Main entry point of the system (port 8000)
- Uses A2A clients to invoke specialized agents
- Combines and formats responses for the user
- Maintains conversation context

**Available A2A tools:**
1. `quantum_developer_client` - Invokes Developer Agent
2. `quantum_status_client` - Invokes Status Agent
3. `quantum_computing_client` - Invokes Computing Agent

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- [uv](https://github.com/astral-sh/uv) package manager
- IBM Quantum account (for quantum operations)
- IBM Watsonx API key (for LLM)

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd quantum-operations-agent
```

2. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your credentials
```

Required environment variables:
```bash
# IBM Watsonx Configuration
WATSONX_API_KEY=your_watsonx_api_key
WATSONX_PROJECT_ID=your_project_id
WATSONX_URL=https://us-south.ml.cloud.ibm.com

# IBM Quantum Configuration (optional for operations agent)
IBM_QUANTUM_TOKEN=your_ibm_quantum_token

# Agent URLs (if running specialized agents separately)
DEVELOPER_AGENT_URL=http://127.0.0.1:8001
STATUS_AGENT_URL=http://127.0.0.1:8002
COMPUTING_AGENT_URL=http://127.0.0.1:8003
```

3. **Install dependencies**
```bash
uv sync
```

### Running the Agent

#### Option 1: Using the start script (Recommended)
```bash
chmod +x start.sh
./start.sh
```

#### Option 2: Using uv directly
```bash
uv run server
```

#### Option 3: Using Docker
```bash
# Build the image
docker build -t quantum-operations-agent .

# Run the container
docker run -p 8000:8000 --env-file .env quantum-operations-agent
```

The agent will start on `http://127.0.0.1:8000`

## 📋 Usage Examples

### Example 1: Complete Quantum Workflow
```
User: "Create a Bell state circuit, check available backends, and execute it"

Operations Agent:
1. Routes to Developer Agent → Generates Bell state QASM code
2. Routes to Status Agent → Lists available backends
3. Routes to Computing Agent → Executes circuit on selected backend
4. Returns combined results
```

### Example 2: Code Generation + Execution
```
User: "Generate a quantum teleportation circuit and run it on a simulator"

Operations Agent:
1. Developer Agent generates the circuit code
2. Computing Agent executes on simulator
3. Returns code and execution results
```

### Example 3: Status Monitoring + Analysis
```
User: "Check the status of my recent quantum jobs and show results"

Operations Agent:
1. Status Agent retrieves job list
2. Status Agent fetches job results
3. Returns formatted job information with histograms
```

## 🔧 Configuration

### Agent Configuration
The agent uses the following configuration in `pyproject.toml`:

```toml
[project.scripts]
server = "quantum_operations_agent:run_server"

[tool.agentstack]
agent_port = 8000
model = "ollama:granite4:small-h"
```

### Specialized Agent URLs
Configure the URLs for specialized agents in `.env`:
```bash
DEVELOPER_AGENT_URL=http://127.0.0.1:8001
STATUS_AGENT_URL=http://127.0.0.1:8002
COMPUTING_AGENT_URL=http://127.0.0.1:8003
```

## 🛠️ Tools

The Operations Agent uses three A2A client tools:

### 1. Quantum Developer Client
- **Purpose**: Communicate with Developer Agent
- **Capabilities**: Code generation, explanations, algorithms
- **Port**: 8001

### 2. Quantum Status Client
- **Purpose**: Communicate with Status Agent
- **Capabilities**: Backend status, job tracking, results
- **Port**: 8002

### 3. Quantum Computing Client
- **Purpose**: Communicate with Computing Agent
- **Capabilities**: Circuit execution, hardware/simulator access
- **Port**: 8003

## 🏃 Running the Complete System

To run the full multi-agent system:

1. **Start all specialized agents first**:
```bash
# Terminal 1 - Developer Agent
cd ../quantum-developer-agent
./start.sh

# Terminal 2 - Status Agent
cd ../quantum-status-agent
./start.sh

# Terminal 3 - Computing Agent
cd ../quantum-computing-agent
./start.sh
```

2. **Start the Operations Agent**:
```bash
# Terminal 4 - Operations Agent
cd ../quantum-operations-agent
./start.sh
```

3. **Verify all agents are running**:
```bash
curl http://127.0.0.1:8001/health  # Developer
curl http://127.0.0.1:8002/health  # Status
curl http://127.0.0.1:8003/health  # Computing
curl http://127.0.0.1:8000/health  # Operations
```

## 🐳 Docker Deployment

### Build and Run
```bash
# Build the image
docker build -t quantum-operations-agent .

# Run with environment file
docker run -p 8000:8000 --env-file .env quantum-operations-agent

# Run with inline environment variables
docker run -p 8000:8000 \
  -e WATSONX_API_KEY=your_key \
  -e WATSONX_PROJECT_ID=your_project \
  -e IBM_QUANTUM_TOKEN=your_token \
  quantum-operations-agent
```

### Docker Compose (All Agents)
Create a `docker-compose.yml` to run all agents together:

```yaml
version: '3.8'

services:
  developer-agent:
    build: ../quantum-developer-agent
    ports:
      - "8001:8001"
    env_file:
      - ../quantum-developer-agent/.env

  status-agent:
    build: ../quantum-status-agent
    ports:
      - "8002:8002"
    env_file:
      - ../quantum-status-agent/.env

  computing-agent:
    build: ../quantum-computing-agent
    ports:
      - "8003:8003"
    env_file:
      - ../quantum-computing-agent/.env

  operations-agent:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - developer-agent
      - status-agent
      - computing-agent
```

Run with:
```bash
docker-compose up
```

## 📊 Agent Coordination Patterns

### Pattern 1: Sequential Workflow
```
User Request → Developer (code) → Computing (execute) → Status (results)
```

### Pattern 2: Parallel Query
```
User Request → [Developer + Status + Computing] → Combine Results
```

### Pattern 3: Conditional Routing
```
User Request → Analyze Intent → Route to Appropriate Agent(s)
```

## 🔍 Monitoring and Debugging

### Check Agent Health
```bash
# Operations Agent
curl http://127.0.0.1:8000/health

# All specialized agents
curl http://127.0.0.1:8001/health  # Developer
curl http://127.0.0.1:8002/health  # Status
curl http://127.0.0.1:8003/health  # Computing
```

### View Logs
```bash
# If running with start.sh, logs appear in terminal
# If running with Docker:
docker logs <container-id>
```

### Common Issues

**Issue**: Operations Agent can't reach specialized agents
- **Solution**: Ensure all specialized agents are running on correct ports
- **Check**: Verify URLs in `.env` match running agents

**Issue**: Authentication errors
- **Solution**: Verify WATSONX_API_KEY and IBM_QUANTUM_TOKEN in `.env`

**Issue**: Port already in use
- **Solution**: Check if another process is using port 8000
```bash
lsof -i :8000
```

## 🧪 Development

### Project Structure
```
quantum-operations-agent/
├── src/
│   └── quantum_operations_agent/
│       ├── __init__.py          # Agent initialization
│       ├── agent.py             # Main agent logic
│       └── tools/               # A2A client tools
│           ├── __init__.py
│           ├── quantum_developer_client.py
│           ├── quantum_status_client.py
│           └── quantum_computing_client.py
├── pyproject.toml               # Project configuration
├── uv.lock                      # Dependency lock file
├── Dockerfile                   # Container definition
├── start.sh                     # Startup script
├── .env.example                 # Environment template
├── .gitignore                   # Git ignore rules
├── README.md                    # This file
└── QUICKSTART.md               # Quick setup guide
```

### Adding New Capabilities

To add new specialized agents:

1. Create a new A2A client tool in `tools/`
2. Register the tool in `agent.py`
3. Update the agent's system prompt to include new capabilities
4. Add the agent URL to `.env.example`

### Testing

```bash
# Run tests (if available)
uv run pytest

# Test agent communication
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Generate a Bell state circuit"}'
```

## 🔗 Related Repositories

This agent is part of the Quantum Computing Multi-Agent System. Here are the related repositories:

- **[Quantum Computing Agent](https://github.ibm.com/Edgar-Castaneda/quantum-computing-agent)** - Circuit execution specialist
- **[Quantum Status Agent](https://github.ibm.com/Edgar-Castaneda/quantum-status-agent)** - Status monitoring and job tracking
- **[Quantum Developer Agent](https://github.ibm.com/Edgar-Castaneda/quantum-developer-agent)** - Code generation and algorithm implementation
- **[Quantum Operations Agent](https://github.ibm.com/Edgar-Castaneda/quantum-lab-agent)** - Main orchestrator coordinating all agents (this repository)

## 📚 Related Agents

- **[Quantum Developer Agent](../quantum-developer-agent/)**: Code generation specialist
- **[Quantum Status Agent](../quantum-status-agent/)**: Status monitoring specialist
- **[Quantum Computing Agent](../quantum-computing-agent/)**: Execution specialist

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

[Your License Here]

## 🙏 Acknowledgments

- Built with [BeeAI Framework](https://github.com/i-am-bee/bee-agent-framework)
- Powered by [IBM Watsonx](https://www.ibm.com/watsonx)
- Quantum computing via [IBM Quantum](https://quantum.ibm.com/)
- Package management by [uv](https://github.com/astral-sh/uv)

## 📞 Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Check the [QUICKSTART.md](QUICKSTART.md) for common setup issues
- Review specialized agent documentation for specific capabilities

---

**Made with ❤️ using BeeAI and IBM Watsonx** | *Main Orchestrator for Quantum Computing*
