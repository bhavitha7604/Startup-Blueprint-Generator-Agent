# 🚀 Startup Blueprint Generator Agent

> **IBM SkillsBuild AICTE 2026 — Problem Statement No. 20**  
> *Transform any raw startup idea into a complete, investor-ready business blueprint using Multi-Agent AI, RAG, LangFlow, and IBM Granite.*

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Agent Pipeline](#-agent-pipeline)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [LangFlow Integration](#-langflow-integration)
- [Output Deliverables](#-output-deliverables)
- [Screenshots](#-screenshots)
- [Team](#-team)

---

## 🧠 Overview

The **Startup Blueprint Generator Agent** is an **Agentic AI system** that takes a raw startup idea in plain English and produces a complete, structured business blueprint — ready for investors, incubators, or accelerators.

It orchestrates **four specialized AI agents** powered by **IBM Granite 3.2 8B Instruct** on **IBM watsonx.ai**, enriched by a **RAG (Retrieval-Augmented Generation) pipeline** that draws from a curated knowledge base of startup ecosystems, MSME schemes, legal frameworks, and funding portals.

**Input:** *"I want to build a mobile app that connects local farmers with urban consumers."*

**Output:**
- ✅ Business Model Canvas (BMC)
- ✅ Go-to-Market (GTM) Strategy
- ✅ Estimated Year-1 Budget Plan
- ✅ Investor Pitch Summary

---

## ❗ Problem Statement

**IBM SkillsBuild AICTE 2026 — PS No. 20**

> *"Build an AI-powered agentic system that can take a startup idea as input and generate a comprehensive startup business blueprint including market analysis, funding options, legal requirements, and a structured business model — using IBM Granite models, LangFlow orchestration, and Retrieval-Augmented Generation (RAG)."*

**Domain:** Entrepreneurship / Startup Ecosystem / Agentic AI

---

## 🏗️ Architecture

```
User Input (Startup Idea)
        │
        ▼
┌───────────────────┐
│   Chat Input      │  ← LangFlow entry point
└────────┬──────────┘
         │
    ┌────┴────────────────────────────┐
    │         RAG Retriever           │
    │  (FAISS / Chroma Vector DB)     │
    │  Knowledge Base: MSME, Legal,   │
    │  Funding, Startup Policy docs   │
    └────┬────────────────────────────┘
         │ (enriched context)
    ┌────▼──────────────────────────────────────────────────┐
    │              IBM watsonx AI Agent (Orchestrator)       │
    │                                                        │
    │   ┌──────────────────┐  ┌──────────────────┐          │
    │   │ Market Intel.    │  │ Funding & Grants  │          │
    │   │ Agent            │  │ Agent             │          │
    │   └──────────────────┘  └──────────────────┘          │
    │   ┌──────────────────┐  ┌──────────────────┐          │
    │   │ Legal &          │  │ Blueprint         │          │
    │   │ Compliance Agent │  │ Composer Agent    │          │
    │   └──────────────────┘  └──────────────────┘          │
    │                                                        │
    │            IBM Granite 3.2 8B Instruct                 │
    └────────────────────────┬──────────────────────────────┘
                             │
                    ┌────────▼────────┐
                    │  Chat Output    │
                    │  (Blueprint)    │
                    └─────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **LLM** | IBM Granite 3.2 8B Instruct (`ibm/granite-3-2-8b-instruct`) |
| **AI Platform** | IBM watsonx.ai |
| **Cloud** | IBM Cloud Lite |
| **Orchestration** | LangFlow |
| **RAG Pipeline** | LangChain + FAISS / Chroma |
| **Embeddings** | IBM Slate 30M (`ibm/slate-30m-english-rtrvr`) |
| **Frontend** | Streamlit |
| **Language** | Python 3.11 |

---

## 🤖 Agent Pipeline

### 1. 🔍 Market Intelligence Agent
Retrieves and analyzes market data using RAG:
- Total Addressable Market (TAM / SAM / SOM)
- Industry trends and growth drivers
- Customer segments and personas
- Competitor landscape analysis
- Market opportunity gaps

### 2. 💰 Funding & Grants Agent
Identifies funding pathways:
- Government schemes (Startup India, MSME, SIDBI, NABARD, DST)
- Grants and competitions (AIM, BIRAC, state-level)
- Angel networks (Indian Angel Network, LetsVenture)
- Sector-relevant VCs (pre-seed to Series A)
- Incubators & accelerators (IIT/IIM, T-Hub, NASSCOM, YC)

### 3. ⚖️ Legal & Compliance Agent
Provides a legal roadmap:
- Business entity registration (Pvt Ltd, LLP, OPC)
- GST, income tax, and startup tax exemptions (Sec 80-IAC)
- IP filing (patents, trademarks, copyrights)
- Sector-specific licenses (FSSAI, RBI, TRAI, etc.)
- Data privacy under PDPB 2023 / IT Act
- Essential legal agreements

### 4. 📋 Blueprint Composer Agent
Synthesizes all outputs into:
- Business Model Canvas (BMC)
- Go-to-Market (GTM) Strategy with phases
- Year-1 Budget Plan
- Investor Pitch Summary (problem → solution → ask)

---

## 📁 Project Structure

```
startup-blueprint-agent/
│
├── app.json                          # IBM Cloud app manifest
├── main.py                           # Main orchestrator entry point
├── requirements.txt                  # Python dependencies
├── .env.example                      # Environment variable template
├── .gitignore
│
├── agents/                           # Four specialized AI agents
│   ├── __init__.py
│   ├── market_intelligence_agent.py
│   ├── funding_grants_agent.py
│   ├── legal_compliance_agent.py
│   └── blueprint_composer_agent.py
│
├── rag/                              # RAG pipeline
│   ├── __init__.py
│   └── rag_pipeline.py              # FAISS vector store + retrieval
│
├── knowledge_base/                   # Add your PDF/TXT docs here
│   └── README.md
│
├── flow/                             # LangFlow configuration
│   └── startup_blueprint_agent_flow.json
│
├── frontend/                         # Streamlit web app
│   └── app.py
│
└── docs/                             # Project documentation
    ├── startup_blueprint_agent.pdf
    └── Startup_Blueprint_Generator_Agent_Template.pptx
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- IBM Cloud account (Free Lite tier works)
- IBM watsonx.ai project with API access
- LangFlow installed locally or hosted

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/startup-blueprint-agent.git
cd startup-blueprint-agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
cp .env.example .env
# Edit .env with your IBM watsonx credentials
```

### 5. Add Knowledge Base Documents *(optional but recommended)*

Place startup-related PDFs/TXT files in `knowledge_base/`, then build the vector store:

```bash
python rag/rag_pipeline.py
```

### 6. Run the Streamlit App

```bash
streamlit run frontend/app.py
```

Visit `http://localhost:8501` in your browser.

### 7. Or Run via CLI

```bash
python main.py
```

---

## 🔑 Environment Variables

| Variable | Description | Required |
|---|---|---|
| `WATSONX_API_KEY` | Your IBM watsonx.ai API key | ✅ |
| `WATSONX_PROJECT_ID` | Your IBM watsonx.ai project ID | ✅ |
| `WATSONX_URL` | watsonx.ai endpoint URL | ✅ |
| `GRANITE_MODEL_ID` | Granite model identifier | ✅ |
| `LANGFLOW_API_KEY` | LangFlow API key (if using hosted) | Optional |
| `LANGFLOW_BASE_URL` | LangFlow server URL | Optional |

---

## 🔀 LangFlow Integration

The complete LangFlow pipeline is exported in:

```
flow/startup_blueprint_agent_flow.json
```

**To import into LangFlow:**

1. Open LangFlow (`http://localhost:7860`)
2. Click **Import** → select `startup_blueprint_agent_flow.json`
3. Add your IBM watsonx credentials in the model node
4. Click **▶ Run** and enter your startup idea in the Chat Input

**Flow Components:**

| Component | Role |
|---|---|
| Chat Input | User enters startup idea |
| Knowledge Base | Source documents for RAG |
| RAG Retriever | FAISS semantic search |
| Market Intelligence Prompt | Agent 1 prompt template |
| Funding & Grants Prompt | Agent 2 prompt template |
| Legal & Compliance Prompt | Agent 3 prompt template |
| IBM Granite Model | Core LLM for all agents |
| Blueprint Composer Prompt | Final synthesis prompt |
| IBM watsonx AI Agent | Orchestrator |
| Chat Output | Delivers final blueprint |

---

## 📦 Output Deliverables

Each run of the agent produces:

| Deliverable | Description |
|---|---|
| **Business Model Canvas** | 9-block Osterwalder canvas tailored to the idea |
| **GTM Strategy** | 3-phase launch plan with channels and KPIs |
| **Budget Plan** | Itemized Year-1 cost estimate (INR) |
| **Investor Pitch Summary** | Concise pitch covering problem → solution → ask |
| **Market Intelligence Report** | TAM/SAM/SOM, trends, competitors |
| **Funding & Grants Report** | Schemes, VCs, incubators |
| **Legal Compliance Checklist** | Registration, IP, licenses, agreements |

---

## 📸 Screenshots

> *Add screenshots of the Streamlit UI and LangFlow pipeline here after first run.*

---

## 👥 Team

| Field | Details |
|---|---|
| **Team Name** | `<Your Team Name>` |
| **College** | `<Your College Name>` |
| **Guide / Mentor** | `<Mentor Name>` |
| **Problem Statement** | IBM SkillsBuild AICTE 2026 — PS No. 20 |

| Name | Email | Mobile |
|---|---|---|
| `<Student Name 1>` | `<email1@example.com>` | `<+91-XXXXXXXXXX>` |

---

## 📄 License

This project is submitted as part of **IBM SkillsBuild AICTE 2026** and is intended for educational and competition purposes.

---

## 🙏 Acknowledgements

- **IBM watsonx.ai** for the Granite LLM and AI platform
- **LangFlow** for visual agent orchestration
- **LangChain** for RAG pipeline utilities
- **Startup India / DPIIT** for the startup policy knowledge base
- **AICTE & IBM SkillsBuild** for the problem statement and platform

---

> *Built with ❤️ using IBM Granite · LangFlow · FAISS · Streamlit*
