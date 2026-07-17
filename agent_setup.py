from typing import Annotated, List
from pydantic import BaseModel, Field
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

# =====================================================================
# 1. DEFINE AGENT STATE (Domain 2: Memory & Context tracking)
# =====================================================================
class AgentState(TypedDict):
    """Tracks the conversational state and execution path of the agent."""
    messages: Annotated[list, add_messages]
    current_action: str
    verification_passed: bool

# =====================================================================
# 2. DEFINE SYSTEM TOOL SCHEMAS (Domain 2: Structured Tool Inputs)
# =====================================================================
class DocumentExtractionTool(BaseModel):
    """
    Schema for scraping and parsing unstructured text documents 
    to extract validated data fields.
    """
    target_url: str = Field(description="The web URL or storage path of the document.")
    extract_fields: List[str] = Field(description="Specific terms or sections to parse out.")

class HumanOversightApproval(BaseModel):
    """Schema for forcing an explicit human-in-the-loop sign-off state."""
    justification: str = Field(description="Reasoning provided by the agent for requiring approval.")
    estimated_token_impact: int = Field(description="Projected computational resource usage.")

if __name__ == "__main__":
    # Self-test validation block to ensure schemas match Pydantic v2 specs
    test_tool = DocumentExtractionTool(
        target_url="https://example.com/report.pdf", 
        extract_fields=["metrics", "cost_optimization"]
    )
    print("Schema initialization verified successfully:")
    print(test_tool.model_dump_json(indent=2))
