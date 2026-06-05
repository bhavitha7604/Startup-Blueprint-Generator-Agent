"""
Blueprint Composer Agent
IBM SkillsBuild AICTE 2026 — Startup Blueprint Generator Agent
"""

from ibm_watsonx_ai.foundation_models import Model


class BlueprintComposerAgent:
    """
    Synthesizes all specialist agent outputs into a complete,
    investor-ready Startup Business Blueprint.
    """

    SYSTEM_PROMPT = """You are the Blueprint Composer Agent in a 
Startup Blueprint Generator system. You receive research from 3 specialist 
agents and must synthesize everything into a complete business blueprint.

Generate the following structured output:

## BUSINESS MODEL CANVAS
- Value Proposition:
- Customer Segments:
- Channels:
- Customer Relationships:
- Revenue Streams:
- Key Resources:
- Key Activities:
- Key Partnerships:
- Cost Structure:

## GO-TO-MARKET STRATEGY
- Phase 1 (Month 0-3): [Launch & validate]
- Phase 2 (Month 3-12): [Scale & grow]
- Phase 3 (Month 12-24): [Expand & fundraise]

## ESTIMATED BUDGET (INR)
- Product Development:
- Marketing & Sales:
- Operations & Infrastructure:
- Legal & Compliance:
- Total Estimated Seed Budget:

## INVESTOR PITCH SUMMARY
[2-3 crisp lines that a founder would say to an investor]

Be professional, specific, and investor-ready."""

    def __init__(self, watsonx_model: Model):
        self.model = watsonx_model

    def run(
        self,
        startup_idea: str,
        market_research: str,
        funding_info: str,
        legal_info: str,
    ) -> str:
        """Compose the full blueprint from all agent outputs."""

        prompt = f"""{self.SYSTEM_PROMPT}

STARTUP IDEA: {startup_idea}

MARKET RESEARCH (from Market Intelligence Agent):
{market_research}

FUNDING INFORMATION (from Funding & Grants Agent):
{funding_info}

LEGAL REQUIREMENTS (from Legal & Compliance Agent):
{legal_info}

Now generate the complete, structured Startup Business Blueprint:"""

        response = self.model.generate_text(prompt=prompt)
        return response
