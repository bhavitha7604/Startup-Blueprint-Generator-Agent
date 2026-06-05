"""
Startup Blueprint Generator Agent — Main App
IBM SkillsBuild AICTE 2026 | Problem Statement No. 20
Run: streamlit run app.py
"""

import os
import concurrent.futures
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Startup Blueprint Generator Agent",
    page_icon="🚀",
    layout="wide",
)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("## 🚀 Startup Blueprint Generator Agent")
st.markdown(
    "**IBM SkillsBuild AICTE 2026 — PS No. 20** &nbsp;·&nbsp; "
    "Agentic AI + RAG + IBM Granite"
)
st.divider()

# ── Sidebar — credentials ─────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🔑 IBM watsonx Credentials")
    api_key = st.text_input(
        "watsonx API Key",
        value=os.getenv("WATSONX_API_KEY", ""),
        type="password",
    )
    project_id = st.text_input(
        "watsonx Project ID",
        value=os.getenv("WATSONX_PROJECT_ID", ""),
        type="password",
    )
    url = st.text_input(
        "watsonx URL",
        value=os.getenv("WATSONX_URL", "https://us-south.ml.cloud.ibm.com"),
    )
    model_id = st.text_input(
        "Granite Model ID",
        value=os.getenv("GRANITE_MODEL_ID", "ibm/granite-3-2-8b-instruct"),
    )
    st.divider()
    st.markdown("**Pipeline Steps:**")
    st.markdown("1. Chat Input\n2. Orchestrator\n3. RAG Retriever\n4. 4 Agents\n5. Granite Model\n6. Blueprint Output")
    st.divider()
    st.caption("IBM SkillsBuild AICTE 2026 | Edunet Foundation")

# ── Main input ────────────────────────────────────────────────────────────────
idea = st.text_area(
    "💡 Describe your startup idea",
    placeholder="e.g. An app that connects local farmers directly with urban consumers to reduce food waste and increase farmer income",
    height=100,
)

col1, col2 = st.columns([1, 5])
with col1:
    run_btn = st.button("▶ Run Agents", type="primary", use_container_width=True)

# ── Pipeline visualization ─────────────────────────────────────────────────────
pipeline_steps = ["Chat Input", "Orchestrator", "RAG Retriever", "4 Agents", "Granite Model", "Blueprint Output"]
step_cols = st.columns(len(pipeline_steps))

def render_pipeline(active_idx=-1, done_idx=-1):
    for i, (col, step) in enumerate(zip(step_cols, pipeline_steps)):
        if i <= done_idx:
            col.success(f"✅ {step}")
        elif i == active_idx:
            col.warning(f"⏳ {step}")
        else:
            col.info(f"○ {step}")

render_pipeline()

# ── Run ───────────────────────────────────────────────────────────────────────
if run_btn:
    if not idea.strip():
        st.error("Please enter your startup idea first!")
        st.stop()
    if not api_key or not project_id:
        st.error("Please enter your IBM watsonx API Key and Project ID in the sidebar!")
        st.stop()

    try:
        from ibm_watsonx_ai import APIClient, Credentials
        from ibm_watsonx_ai.foundation_models import Model
        from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

        # Init model
        credentials = Credentials(url=url, api_key=api_key)
        client = APIClient(credentials=credentials, project_id=project_id)

        params = {
            GenParams.MAX_NEW_TOKENS: 800,
            GenParams.TEMPERATURE: 0.3,
            GenParams.TOP_P: 0.9,
        }
        model = Model(model_id=model_id, params=params, credentials=credentials, project_id=project_id)

    except Exception as e:
        st.error(f"❌ Failed to connect to IBM watsonx.ai: {e}")
        st.info("Make sure your API Key and Project ID are correct.")
        st.stop()

    # Import agents
    from agents import (
        MarketIntelligenceAgent,
        FundingGrantsAgent,
        LegalComplianceAgent,
        BlueprintComposerAgent,
    )
    from rag.retriever import load_retriever

    # Step 1: Chat Input
    render_pipeline(active_idx=0)
    st.toast("📥 Startup idea received!")

    # Step 2: Orchestrator
    render_pipeline(done_idx=0, active_idx=1)
    st.toast("🧠 Orchestrator parsing idea...")

    # Step 3: RAG
    render_pipeline(done_idx=1, active_idx=2)
    with st.spinner("Loading RAG knowledge base..."):
        retriever = load_retriever()
    st.toast("📚 RAG retriever ready!")

    # Step 4: 4 Agents run in parallel
    render_pipeline(done_idx=2, active_idx=3)
    st.toast("🤖 All 4 agents running in parallel...")

    agent_status = st.columns(4)
    agent_status[0].info("⏳ Market Agent")
    agent_status[1].info("⏳ Funding Agent")
    agent_status[2].info("⏳ Legal Agent")
    agent_status[3].info("⏳ Composer Agent")

    market_agent   = MarketIntelligenceAgent(model, retriever)
    funding_agent  = FundingGrantsAgent(model, retriever)
    legal_agent    = LegalComplianceAgent(model, retriever)
    composer_agent = BlueprintComposerAgent(model)

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        market_fut  = executor.submit(market_agent.run, idea)
        funding_fut = executor.submit(funding_agent.run, idea)
        legal_fut   = executor.submit(legal_agent.run, idea)

        market_res  = market_fut.result()
        agent_status[0].success("✅ Market Agent")

        funding_res = funding_fut.result()
        agent_status[1].success("✅ Funding Agent")

        legal_res   = legal_fut.result()
        agent_status[2].success("✅ Legal Agent")

    # Step 5: Granite synthesis
    render_pipeline(done_idx=3, active_idx=4)
    st.toast("✨ IBM Granite composing blueprint...")
    agent_status[3].info("⏳ Composer Agent")

    blueprint = composer_agent.run(idea, market_res, funding_res, legal_res)
    agent_status[3].success("✅ Composer Agent")

    # Step 6: Output
    render_pipeline(done_idx=5)
    st.toast("🎉 Blueprint ready!")
    st.balloons()

    # ── Display results ──
    st.divider()
    st.markdown("## 📊 Your Startup Business Blueprint")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["📈 Market Research", "💰 Funding & Grants", "⚖️ Legal & Compliance", "📋 Full Blueprint"]
    )
    with tab1:
        st.markdown("### Market Intelligence Report")
        st.markdown(market_res)
    with tab2:
        st.markdown("### Funding & Grants Report")
        st.markdown(funding_res)
    with tab3:
        st.markdown("### Legal & Compliance Report")
        st.markdown(legal_res)
    with tab4:
        st.markdown("### Complete Startup Business Blueprint")
        st.markdown(blueprint)
        st.download_button(
            "⬇️ Download Blueprint",
            data=blueprint,
            file_name="startup_blueprint.txt",
            mime="text/plain",
        )
