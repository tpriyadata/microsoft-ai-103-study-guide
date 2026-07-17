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
# ===================================================================== #
# 3. DEFINE THE ROUTING & EXECUTION GRAPH (Domain 2: Orchestration)     #
# ===================================================================== #
from langgraph.graph import StateGraph, END

def call_model(state: AgentState):
    """Simulates Azure OpenAI deciding to execute a tool or proceed."""
    return {
        "messages": state.get("messages", []),
        "current_action": "evaluating_document",
        "verification_passed": False
    }

def should_continue(state: AgentState) -> str:
    """Conditional routing logic for state transitions."""
    if state.get("current_action") == "evaluating_document":
        return "execute_tools"
    return END

# Initialize and compile the state graph
workflow = StateGraph(AgentState)
workflow.add_node("agent_core", call_model)
workflow.set_entry_point("agent_core")

workflow.add_conditional_edges(
    "agent_core",
    should_continue,
    {
        "execute_tools": END,  # Short-circuiting to END for this validation step
        END: END
    }
)

app = workflow.compile()

# ===================================================================== #
# 4. VALIDATION RUNNER                                                  #
# ===================================================================== #
if __name__ == "__main__":
    # 1. Validate Pydantic Schemas
    test_tool = DocumentExtractionTool(
        target_url="https://example.com/report.pdf", 
        extract_fields=["metrics", "cost_optimization"]
    )
    print("✓ Pydantic V2 schemas initialized successfully.")
    
    # 2. Validate LangGraph Compilation
    initial_state = {
        "messages": [("user", "Analyze the latest cloud spend report.")],
        "current_action": "init",
        "verification_passed": False
    }
    output = app.invoke(initial_state)
    print("✓ LangGraph compiled and executed state transition successfully.")
    print(f"Final Action State: {output['current_action']}")    

