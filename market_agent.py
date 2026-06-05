"""
Legal & Compliance Agent
IBM SkillsBuild AICTE 2026 — Startup Blueprint Generator Agent
"""

from ibm_watsonx_ai.foundation_models import Model


class LegalComplianceAgent:
    """
    Identifies business registration steps, IP filing requirements,
    licenses, and regulatory compliance needs — India-specific.
    """

    SYSTEM_PROMPT = """You are the Legal & Compliance Agent in a 
Startup Blueprint Generator system. Your job is to provide legal 
guidance for a startup idea including:
1. Recommended Business Structure (Pvt Ltd / LLP / OPC — with reasons)
2. Step-by-step Registration Process (MCA, GST, MSME/Udyam, PAN, TAN)
3. Required Licenses & Permits specific to this domain
4. IP Protection Strategy (Patent / Trademark / Copyright)
5. Key Legal Risks and mitigation strategies

Focus on Indian legal requirements. Be practical and step-by-step."""

    def __init__(self, watsonx_model: Model, retriever=None):
        self.model = watsonx_model
        self.retriever = retriever

    def run(self, startup_idea: str) -> str:
        """Run the Legal & Compliance Agent on a startup idea."""
        context = ""
        if self.retriever:
            docs = self.retriever.get_relevant_documents(
                startup_idea + " legal registration compliance India"
            )
            context = "\n".join([d.page_content for d in docs[:3]])

        prompt = f"""{self.SYSTEM_PROMPT}

Relevant legal context (from knowledge base):
{context if context else "No external data retrieved — use general knowledge."}

Startup Idea: {startup_idea}

Provide detailed legal and compliance guidance:"""

        response = self.model.generate_text(prompt=prompt)
        return response
