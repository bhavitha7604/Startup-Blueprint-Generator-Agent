"""
Funding & Grants Agent
IBM SkillsBuild AICTE 2026 — Startup Blueprint Generator Agent
"""

from ibm_watsonx_ai.foundation_models import Model


class FundingGrantsAgent:
    """
    Retrieves MSME schemes, angel networks, VCs, and government
    grants relevant to the startup's domain and stage.
    """

    SYSTEM_PROMPT = """You are the Funding & Grants Agent in a 
Startup Blueprint Generator system. Your job is to identify funding 
opportunities for a startup idea including:
1. Relevant Government Schemes (Startup India, MSME, DPIIT, iStart, etc.)
2. Top Angel Investors / VCs for this domain in India
3. Estimated Seed Funding Range (in INR)
4. Grants & Competitions to apply for
5. Step-by-step Funding Roadmap: Pre-seed → Seed → Series A

Focus on the Indian startup ecosystem. Be specific and actionable."""

    def __init__(self, watsonx_model: Model, retriever=None):
        self.model = watsonx_model
        self.retriever = retriever

    def run(self, startup_idea: str) -> str:
        """Run the Funding & Grants Agent on a startup idea."""
        context = ""
        if self.retriever:
            docs = self.retriever.get_relevant_documents(
                startup_idea + " funding grants MSME schemes India"
            )
            context = "\n".join([d.page_content for d in docs[:3]])

        prompt = f"""{self.SYSTEM_PROMPT}

Relevant funding context (from knowledge base):
{context if context else "No external data retrieved — use general knowledge."}

Startup Idea: {startup_idea}

Provide detailed funding and grants information:"""

        response = self.model.generate_text(prompt=prompt)
        return response
