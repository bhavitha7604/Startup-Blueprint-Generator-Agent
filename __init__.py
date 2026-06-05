"""
Market Intelligence Agent
IBM SkillsBuild AICTE 2026 — Startup Blueprint Generator Agent
"""

from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams


class MarketIntelligenceAgent:
    """
    Retrieves and summarizes market size, trends, and competitor
    data using RAG + IBM Granite model.
    """

    SYSTEM_PROMPT = """You are the Market Intelligence Agent in a 
Startup Blueprint Generator system. Your job is to analyze a startup idea 
and provide structured market research including:
1. Market Size & TAM (Total Addressable Market) — India-specific
2. Key Market Trends (2024-2026)
3. Top 3-5 Competitors with strengths and weaknesses
4. Market Gap this startup can fill
5. Target Customer Segment (demographics + psychographics)

Be specific, data-driven, and concise. Format with clear numbered sections."""

    def __init__(self, watsonx_model: Model, retriever=None):
        self.model = watsonx_model
        self.retriever = retriever

    def run(self, startup_idea: str) -> str:
        """Run the Market Intelligence Agent on a startup idea."""
        context = ""
        if self.retriever:
            docs = self.retriever.get_relevant_documents(startup_idea)
            context = "\n".join([d.page_content for d in docs[:3]])

        prompt = f"""{self.SYSTEM_PROMPT}

Relevant market context (from knowledge base):
{context if context else "No external data retrieved — use general knowledge."}

Startup Idea: {startup_idea}

Provide detailed market intelligence:"""

        response = self.model.generate_text(prompt=prompt)
        return response
