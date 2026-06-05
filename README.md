# 🚀 Startup Blueprint Generator Agent

> **IBM SkillsBuild for University Engagements — AICTE 2026**
> Problem Statement No. 20 | Agentic AI + RAG

---

## 📌 Project Overview

The **Startup Blueprint Generator Agent** is a multi-agent AI system that transforms any raw startup idea (typed in plain language) into a **complete, investor-ready business blueprint** — including a Business Model Canvas, Go-to-Market strategy, funding roadmap, legal checklist, and budget estimate.

Built using **LangFlow**, **IBM Granite models**, **IBM watsonx.ai**, and a **RAG (Retrieval-Augmented Generation)** pipeline on **IBM Cloud Lite**.

---

## 🧠 How It Works

```
User Idea (Chat Input)
        │
        ▼
IBM watsonx AI Agent (Orchestrator)
        │
        ├──► RAG Retriever ◄── File Component (Knowledge Base)
        │         │
        ▼         ▼
┌─────────────────────────────────────────────┐
│  Market      Funding    Legal      Composer  │
│  Agent       Agent      Agent      Agent     │
└─────────────────────────────────────────────┘
        │
        ▼
IBM Granite Model (ibm-granite-3-2-8b-instruct)
        │
        ▼
Chat Output → Business Blueprint
(BMC + GTM + Budget + Legal + Pitch Summary)
```

---

## 🤖 4 Specialist Agents

| Agent | Role |
|---|---|
| **Market Intelligence Agent** | Retrieves market size, trends, competitor analysis using RAG |
| **Funding & Grants Agent** | Retrieves MSME schemes, angel investors, VCs, government grants |
| **Legal & Compliance Agent** | Identifies business registration, IP filing, GST, licenses |
| **Blueprint Composer Agent** | Synthesizes all outputs into Business Model Canvas + full plan |

---

## 🛠️ Tech Stack

| Component | Tool |
|---|---|
| Agent Orchestration | LangFlow |
| LLM (Mandatory) | IBM Granite — `ibm-granite-3-2-8b-instruct` |
| AI Platform (Mandatory) | IBM watsonx.ai |
| Cloud (Mandatory) | IBM Cloud Lite |
| RAG Pipeline | Retrieval-Augmented Generation |
| Vector Database | FAISS / Chroma |
| Frontend Demo | Streamlit |
| Language | Python 3.10+ |

---

## 📂 Project Structure

```
startup-blueprint-generator-agent/
│
├── README.md                          ← This file
├── app.json                           ← IBM Cloud deployment config
├── requirements.txt                   ← Python dependencies
├── .env.example                       ← Environment variable template
│
├── app.py                             ← Main Streamlit app (run this!)
├── agents/
│   ├── market_agent.py                ← Market Intelligence Agent
│   ├── funding_agent.py               ← Funding & Grants Agent
│   ├── legal_agent.py                 ← Legal & Compliance Agent
│   └── composer_agent.py              ← Blueprint Composer Agent
│
├── rag/
│   ├── embeddings.py                  ← Document embedding pipeline
│   ├── retriever.py                   ← Vector store retriever (FAISS)
│   └── knowledge_base/               ← Upload your PDFs here
│       └── .gitkeep
│
├── langflow/
│   └── startup_blueprint_agent_flow.json  ← Import this into LangFlow
│
└── docs/
    ├── startup_blueprint_agent.pdf    ← Problem statement document
    └── project_presentation.pptx     ← Submission presentation
```

---

## ⚙️ Setup & Run

### Step 1 — Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/startup-blueprint-generator-agent.git
cd startup-blueprint-generator-agent
```

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Set environment variables
```bash
cp .env.example .env
# Open .env and fill in your IBM watsonx credentials
```

### Step 4 — Run the app
```bash
streamlit run app.py
```

### Step 5 — Open in browser
```
http://localhost:8501
```

---

## 🌐 LangFlow Setup (Optional)

1. Install LangFlow: `pip install langflow`
2. Run: `langflow run`
3. Open `http://localhost:7860`
4. Import `langflow/startup_blueprint_agent_flow.json`
5. Add your IBM watsonx API key in the Granite model node
6. Click **Run**

---

## 🔑 Environment Variables

```env
WATSONX_API_KEY=your_ibm_watsonx_api_key
WATSONX_PROJECT_ID=your_ibm_watsonx_project_id
WATSONX_URL=https://us-south.ml.cloud.ibm.com
GRANITE_MODEL_ID=ibm/granite-3-2-8b-instruct
```

Get your credentials at: https://cloud.ibm.com → watsonx.ai → Manage → API Keys

---

## 📤 Output — What You Get

After entering your startup idea, the agent generates:

- ✅ **Business Model Canvas (BMC)** — all 9 blocks filled
- ✅ **Go-to-Market Strategy** — 3 phase launch plan
- ✅ **Estimated Budget** — in INR, broken down by category
- ✅ **Funding Roadmap** — MSME schemes, VCs, angel investors
- ✅ **Legal Checklist** — registration, GST, IP, licenses
- ✅ **Investor Pitch Summary** — 3-line ready-to-present pitch

---

## 👥 Team

| Field | Details |
|---|---|
| **Team Name** | [Your Team Name] |
| **College** | [Your College Name] |
| **Guide / Mentor** | [Mentor Name] |
| **Program** | IBM SkillsBuild AICTE 2026 via Edunet Foundation |

---

## 📜 License

This project is submitted as part of the IBM SkillsBuild AICTE 2026 University Engagement Program.

---

*Built with ❤️ using IBM Granite + LangFlow + Agentic AI*
