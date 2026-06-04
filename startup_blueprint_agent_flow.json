{
  "id": "startup-blueprint-generator-agent",
  "name": "Startup Blueprint Generator Agent",
  "description": "IBM SkillsBuild AICTE 2026 - PS No. 20 | Multi-agent RAG pipeline that transforms a startup idea into a complete business blueprint using IBM Granite + LangFlow.",
  "version": "1.0",
  "last_tested_version": "1.1.0",

  "data": {
    "nodes": [

      {
        "id": "ChatInput-1",
        "type": "ChatInput",
        "display_name": "Chat Input",
        "description": "User enters their startup idea in natural language",
        "position": { "x": 50, "y": 300 },
        "data": {
          "node": {
            "template": {
              "input_value": {
                "value": "I want to build a mobile app that connects local farmers directly with urban consumers to reduce food waste and increase farmer income.",
                "type": "str",
                "display_name": "Startup Idea"
              },
              "sender_name": {
                "value": "Entrepreneur",
                "type": "str"
              }
            }
          }
        }
      },

      {
        "id": "Prompt-MarketAgent",
        "type": "PromptTemplate",
        "display_name": "Market Intelligence Prompt",
        "description": "Prompt for Market Intelligence Agent to research market size, trends, competitors",
        "position": { "x": 350, "y": 100 },
        "data": {
          "node": {
            "template": {
              "template": {
                "value": "You are a Market Intelligence Agent. Given this startup idea: {startup_idea}\n\nUsing the retrieved market data, provide:\n1. Market Size & TAM (Total Addressable Market)\n2. Key Market Trends (2024-2026)\n3. Top 3-5 Competitors with their strengths/weaknesses\n4. Market Gap this startup can fill\n5. Target Customer Segment\n\nBe specific, data-driven, and concise.",
                "type": "str"
              }
            }
          }
        }
      },

      {
        "id": "Prompt-FundingAgent",
        "type": "PromptTemplate",
        "display_name": "Funding & Grants Prompt",
        "description": "Prompt for Funding Agent to find MSME schemes, VCs, angel investors",
        "position": { "x": 350, "y": 300 },
        "data": {
          "node": {
            "template": {
              "template": {
                "value": "You are a Funding & Grants Agent. Given this startup idea: {startup_idea}\n\nUsing retrieved funding data, provide:\n1. Relevant Government Schemes (MSME, Startup India, DPIIT etc.)\n2. Top Angel Investors / VCs for this domain\n3. Estimated Seed Funding Range\n4. Grants & Competitions to apply for\n5. Step-by-step funding roadmap (Pre-seed → Seed → Series A)\n\nBe specific to the Indian startup ecosystem.",
                "type": "str"
              }
            }
          }
        }
      },

      {
        "id": "Prompt-LegalAgent",
        "type": "PromptTemplate",
        "display_name": "Legal & Compliance Prompt",
        "description": "Prompt for Legal Agent to identify registration, IP, compliance needs",
        "position": { "x": 350, "y": 500 },
        "data": {
          "node": {
            "template": {
              "template": {
                "value": "You are a Legal & Compliance Agent. Given this startup idea: {startup_idea}\n\nProvide:\n1. Recommended Business Structure (Pvt Ltd / LLP / OPC)\n2. Step-by-step Registration Process (MCA, GST, MSME)\n3. Required Licenses & Permits for this domain\n4. IP Protection strategy (Patent / Trademark / Copyright)\n5. Key Legal Risks and how to mitigate them\n\nFocus on Indian legal requirements.",
                "type": "str"
              }
            }
          }
        }
      },

      {
        "id": "WatsonxModel-1",
        "type": "WatsonxAIModel",
        "display_name": "IBM Granite Model",
        "description": "IBM Granite 3.2 8B Instruct - Core LLM for all agent reasoning and blueprint generation",
        "position": { "x": 650, "y": 300 },
        "data": {
          "node": {
            "template": {
              "model_id": {
                "value": "ibm/granite-3-2-8b-instruct",
                "type": "str",
                "display_name": "Model ID"
              },
              "url": {
                "value": "https://us-south.ml.cloud.ibm.com",
                "type": "str"
              },
              "project_id": {
                "value": "{WATSONX_PROJECT_ID}",
                "type": "str"
              },
              "apikey": {
                "value": "{WATSONX_API_KEY}",
                "type": "str",
                "password": true
              },
              "max_new_tokens": {
                "value": 1024,
                "type": "int"
              },
              "temperature": {
                "value": 0.3,
                "type": "float"
              },
              "top_p": {
                "value": 0.9,
                "type": "float"
              },
              "decoding_method": {
                "value": "greedy",
                "type": "str"
              }
            }
          }
        }
      },

      {
        "id": "RAGRetriever-1",
        "type": "VectorStoreRetriever",
        "display_name": "RAG Retriever",
        "description": "Fetches relevant documents from vector DB - startup portals, MSME schemes, policy docs",
        "position": { "x": 650, "y": 100 },
        "data": {
          "node": {
            "template": {
              "search_type": {
                "value": "similarity",
                "type": "str"
              },
              "search_kwargs": {
                "value": { "k": 5 },
                "type": "dict"
              }
            }
          }
        }
      },

      {
        "id": "FileComponent-1",
        "type": "File",
        "display_name": "Knowledge Base",
        "description": "Stores startup knowledge: MSME policies, incubator databases, funding portals, legal docs",
        "position": { "x": 350, "y": 700 },
        "data": {
          "node": {
            "template": {
              "path": {
                "value": "./knowledge_base/",
                "type": "str",
                "display_name": "Knowledge Base Path"
              },
              "file_types": {
                "value": ["pdf", "txt", "json", "csv"],
                "type": "list"
              }
            }
          }
        }
      },

      {
        "id": "Prompt-ComposerAgent",
        "type": "PromptTemplate",
        "display_name": "Blueprint Composer Prompt",
        "description": "Synthesizes all agent outputs into the final business blueprint",
        "position": { "x": 950, "y": 300 },
        "data": {
          "node": {
            "template": {
              "template": {
                "value": "You are a Blueprint Composer Agent. You have the following research from specialist agents:\n\nSTARTUP IDEA: {startup_idea}\nMARKET RESEARCH: {market_research}\nFUNDING INFO: {funding_info}\nLEGAL REQUIREMENTS: {legal_info}\n\nNow generate a complete, structured Startup Business Blueprint:\n\n## 1. BUSINESS MODEL CANVAS\n- Value Proposition:\n- Customer Segments:\n- Channels:\n- Customer Relationships:\n- Revenue Streams:\n- Key Resources:\n- Key Activities:\n- Key Partnerships:\n- Cost Structure:\n\n## 2. GO-TO-MARKET STRATEGY\n- Phase 1 (0-3 months):\n- Phase 2 (3-12 months):\n- Phase 3 (12-24 months):\n\n## 3. ESTIMATED BUDGET (INR)\n- Development:\n- Marketing:\n- Operations:\n- Legal & Compliance:\n- Total Estimated Seed Budget:\n\n## 4. INVESTOR PITCH SUMMARY (3 lines)\n\nMake it professional, specific, and investor-ready.",
                "type": "str"
              }
            }
          }
        }
      },

      {
        "id": "WatsonxAgent-1",
        "type": "WatsonxAIAgent",
        "display_name": "IBM watsonx AI Agent",
        "description": "Main orchestrator - coordinates all sub-agents, manages context, routes tasks",
        "position": { "x": 950, "y": 100 },
        "data": {
          "node": {
            "template": {
              "system_prompt": {
                "value": "You are the Startup Blueprint Generator Agent orchestrator. Your job is to:\n1. Parse the user's startup idea\n2. Route tasks to specialist sub-agents (Market, Funding, Legal)\n3. Collect their outputs\n4. Pass everything to the Blueprint Composer\n5. Return a clean, structured business blueprint\n\nAlways be specific, data-driven, and entrepreneur-friendly.",
                "type": "str"
              },
              "max_iterations": {
                "value": 5,
                "type": "int"
              }
            }
          }
        }
      },

      {
        "id": "ChatOutput-1",
        "type": "ChatOutput",
        "display_name": "Blueprint Output",
        "description": "Delivers the final structured business blueprint to the user",
        "position": { "x": 1250, "y": 300 },
        "data": {
          "node": {
            "template": {
              "sender_name": {
                "value": "Startup Blueprint Agent",
                "type": "str"
              },
              "data_template": {
                "value": "{text}",
                "type": "str"
              }
            }
          }
        }
      }

    ],

    "edges": [
      { "id": "e1", "source": "ChatInput-1", "target": "Prompt-MarketAgent", "sourceHandle": "message", "targetHandle": "startup_idea" },
      { "id": "e2", "source": "ChatInput-1", "target": "Prompt-FundingAgent", "sourceHandle": "message", "targetHandle": "startup_idea" },
      { "id": "e3", "source": "ChatInput-1", "target": "Prompt-LegalAgent", "sourceHandle": "message", "targetHandle": "startup_idea" },
      { "id": "e4", "source": "RAGRetriever-1", "target": "Prompt-MarketAgent", "sourceHandle": "documents", "targetHandle": "context" },
      { "id": "e5", "source": "FileComponent-1", "target": "RAGRetriever-1", "sourceHandle": "data", "targetHandle": "input" },
      { "id": "e6", "source": "Prompt-MarketAgent", "target": "WatsonxModel-1", "sourceHandle": "prompt", "targetHandle": "input" },
      { "id": "e7", "source": "Prompt-FundingAgent", "target": "WatsonxModel-1", "sourceHandle": "prompt", "targetHandle": "input" },
      { "id": "e8", "source": "Prompt-LegalAgent", "target": "WatsonxModel-1", "sourceHandle": "prompt", "targetHandle": "input" },
      { "id": "e9", "source": "WatsonxModel-1", "target": "Prompt-ComposerAgent", "sourceHandle": "text", "targetHandle": "agent_outputs" },
      { "id": "e10", "source": "Prompt-ComposerAgent", "target": "WatsonxAgent-1", "sourceHandle": "prompt", "targetHandle": "input" },
      { "id": "e11", "source": "WatsonxAgent-1", "target": "ChatOutput-1", "sourceHandle": "message", "targetHandle": "input_value" }
    ]
  },

  "metadata": {
    "project": "IBM SkillsBuild AICTE 2026",
    "problem_statement_no": 20,
    "title": "Startup Blueprint Generator Agent",
    "domain": "Entrepreneurship / Agentic AI",
    "mandatory_tech": ["IBM Cloud Lite", "IBM Granite Models"],
    "team": "<Your Team Name>",
    "college": "<Your College>",
    "guide": "<Mentor Name>"
  }
}
