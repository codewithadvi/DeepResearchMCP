# ResearchLens

AI-powered research assistant that automatically finds gaps in academic literature. Instead of manually reading 50+ papers to understand a research field, ResearchLens uses a specialized team of AI agents to conduct literature reviews and identify research opportunities in minutes.

---

## Key Features

- **4-Agent AI System** - Specialized agents for searching, analyzing, and synthesizing research
- **Intelligent Paper Search** - Searches millions of academic papers via LinkUp API
- **Automatic Gap Detection** - Identifies unexplored combinations and research opportunities
- **Methodology Analysis** - Creates comparison matrices across different approaches
- **Publication-Ready Reports** - State-of-the-art summaries, gaps, and future directions
- **Multi-Format Export** - JSON, Markdown, and PDF outputs
- **Dual Deployment** - Run locally for best quality or deploy to cloud for easy sharing
- **IDE Integration** - Optional MCP support for Cursor and Claude Desktop
- **Completely Free** - Uses free tiers of all APIs, no credit card required

---

## How It Works

ResearchLens uses four specialized AI agents that work together:

```
User Input: "Efficient attention mechanisms in transformers"
    |
    +-> Agent 1: Literature Reviewer
    |   - Searches LinkUp API for 50-100 relevant papers
    |   - Extracts methodologies, datasets, benchmarks
    |
    +-> Agent 2: Methodology Analyst
    |   - Creates comparison matrix of approaches
    |   - Identifies which techniques appear together
    |   - Extracts performance metrics
    |
    +-> Agent 3: Gap Analyst
    |   - Finds unexplored combinations
    |   - Identifies contradictions between papers
    |   - Spots emerging opportunities
    |
    +-> Agent 4: Report Writer
    |   - Synthesizes findings into structured report
    |   - Generates SOTA summary
    |   - Documents gaps and future work
    |
Result: Complete research analysis in 2 minutes
```

### Example Output

**Input:** "Efficient attention mechanisms in transformer models"

**Output includes:**

State-of-the-Art Summary:
- Flash Attention (2022) - 10x faster inference
- Multi-Query Attention (2023) - Reduces KV cache
- Sparse Attention - 50% parameter reduction

Research Gaps Identified:
- No attention method optimizes both speed AND memory simultaneously
- Sparse attention not benchmarked on large language models
- Cross-domain attention transfer not studied

Future Work Recommendations:
- Hybrid Flash + Sparse Attention approach
- Domain-aware attention pattern optimization
- Hardware-aware kernel design

**Time to completion:** 2 minutes (vs 2 weeks manually)

---

## Deployment Options

### Local Development (Best Quality)

Run on your computer with DeepSeek-R1 7B for highest quality reasoning.

**Best for:**
- Development and experimentation
- Best AI reasoning quality
- Complete data privacy

**Requirements:**
- Python 3.10+
- 8GB RAM minimum (16GB recommended)
- Ollama installed

**Setup time:** 10 minutes

**Performance:**
- With GPU: 1.5-2 minutes per query
- Without GPU: 2-5 minutes per query

---

### Cloud Deployment (Easiest)

Deploy to Streamlit Cloud for a public URL anyone can access.

**Best for:**
- Sharing research with colleagues
- Public demonstrations
- No local installation required

**Setup time:** 5 minutes

**Performance:** 1.5 minutes per query (Groq optimization)

**Cost:** Free (uses Groq and LinkUp free tiers)

---

## Quick Start

### Option 1: Local Setup

```bash
# 1. Install Ollama from https://ollama.ai
# 2. Download the model
ollama pull deepseek-r1:7b

# 3. Clone repository
git clone https://github.com/codewithadvi/DeepResearchMCP.git
cd DeepResearchMCP/local-ollama-version

# 4. Setup Python environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# 5. Install dependencies
pip install -r requirements.txt

# 6. Get API key from https://linkup.so
# Create .env file with: LINKUP_API_KEY=your_key

# 7. Run application
streamlit run app.py
```

Opens at http://localhost:8501

---

### Option 2: Cloud Deployment

```bash
# 1. Get free API keys
#    - LinkUp: https://linkup.so (sign up for free)
#    - Groq: https://console.groq.com (no credit card)

# 2. Fork repository on GitHub
#    github.com/codewithadvi/DeepResearchMCP

# 3. Deploy to Streamlit Cloud
#    - Visit https://share.streamlit.io
#    - New app -> Select your fork
#    - Main file: groq-cloud-version/app.py

# 4. Add secrets in Streamlit dashboard
#    Settings -> Secrets
#    LINKUP_API_KEY=your_key
#    GROQ_API_KEY=your_key

# Your app is now live at: https://yourname-researchlens.streamlit.app
```

---

## Architecture

### System Design

```
User Interface (Streamlit)
    |
    v
Orchestration (CrewAI)
    |
    +-- AI Model Layer
    |   - Local: DeepSeek-R1 (via Ollama)
    |   - Cloud: Mixtral 8x7B (via Groq)
    |
    +-- Data Access Layer
    |   - LinkUp API (academic paper search)
    |   - 100+ million papers indexed
    |
    v
Agent Workflow Pipeline
    - Literature Reviewer -> Methodology Analyst -> Gap Analyst -> Report Writer
    - Data flows automatically between agents
    - Each agent builds on previous agent's output
```

---

## System Requirements

### Local Development

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python | 3.10 | 3.11+ |
| RAM | 8GB | 16GB+ |
| Disk Space | 20GB | 30GB+ |
| GPU | Optional | NVIDIA/AMD (optional) |

### Cloud Deployment

| Component | Streamlit Cloud |
|-----------|-----------------|
| RAM | Shared (1-4GB) |
| CPU | Shared |
| GPU | Not needed |
| Cost | Free |

---

## Costs

Completely free using free tiers:

| Service | Cost | Details |
|---------|------|---------|
| LinkUp API | Free | 100 searches/month |
| Groq API | Free | 120 requests/min, unlimited |
| Ollama | Free | Download once, use locally |
| Streamlit Cloud | Free | Unlimited hosting |
| **Total** | **$0/month** | Completely free |

---

## Use Cases

**PhD Student:** Start a research project on "transformer efficiency"
- Manual approach: Read 50+ papers over 2-3 weeks
- ResearchLens: Get SOTA summary, 5 identified gaps, future directions in 2 minutes

**Research Engineer:** Find unexplored areas in "vision-language models"
- See comparison of all VLM approaches
- Identify: "No VLM trained on 3D video"
- Result: Novel research direction identified

**Research Manager:** Understand state-of-field in "efficient inference"
- Get SOTA technologies, limitations, and investment opportunities
- All in one structured report

---

## Advanced: MCP Integration (Optional)

Model Context Protocol (MCP) allows AI coding assistants like Cursor and Claude Desktop to call ResearchLens automatically.

**Use case:** Your AI can research topics while you code without leaving your IDE.

**Example:**
```
In Cursor: "Research quantum error correction approaches before we start"
Cursor AI: Automatically calls ResearchLens -> gets summary -> suggests implementation
```

### Setup with Cursor

1. Install Cursor from https://cursor.sh
2. Add to Cursor settings:
```json
{
  "mcpServers": {
    "research": {
      "command": "python",
      "args": ["/absolute/path/to/server.py"],
      "env": {
        "LINKUP_API_KEY": "your_key",
        "GROQ_API_KEY": "your_key"
      }
    }
  }
}
```
3. Restart Cursor

Your AI assistant can now research topics on demand.

---

## Project Structure

```
deep-research-mcp/
├── local-ollama-version/
│   ├── app.py                 # Streamlit web interface
│   ├── agents.py              # CrewAI agent system
│   ├── requirements.txt
│   └── .env.example
│
├── groq-cloud-version/
│   ├── app.py                 # Streamlit web interface
│   ├── agents.py              # Groq-only setup
│   ├── requirements.txt
│   └── .env.example
│
├── server.py                  # MCP server (optional)
├── README.md                  # This file
└── .gitignore                 # Protects secrets
```

Key difference:
- Local version: Ollama + Groq fallback (best quality)
- Cloud version: Groq only (optimized for cloud, faster startup)

---

## Troubleshooting

**Local version not starting:**
```bash
# Ensure Ollama is running
ollama serve

# In another terminal
streamlit run app.py
```

**Cloud version showing errors:**
- Verify API keys are added in Streamlit Secrets (not .env)
- Check keys haven't expired
- Restart the app in Streamlit dashboard

**MCP not working:**
- Use absolute file paths (not relative)
- Verify Python is in system PATH
- Check .env file contains valid API keys
- Restart your IDE

---

## Getting Started

1. Choose your deployment:
   - **Local:** Best quality reasoning
   - **Cloud:** Easiest to share

2. Get free API keys:
   - LinkUp: https://linkup.so
   - Groq: https://console.groq.com

3. Follow the Quick Start section above

4. Enter a research topic and get results in 2 minutes

For questions or issues, open a GitHub discussion or issue.
