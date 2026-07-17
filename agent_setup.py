from typing import Annotated, List
from pydantic import BaseModel, Field
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END

# Import your zero-cost mock environment modules
from config_loader import initialize_azure_clients
from document_processor import IngestionPipeline

# Initialize the zero-cost pipeline globally for the nodes
settings, openai_client = initialize_azure_clients()
pipeline = IngestionPipeline(index_name=settings.azure_ai_search_index_name)

# 1. DEFINE AGENT STATE
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    current_action: str
    verification_passed: bool

# 2. DEFINE SYSTEM TOOL SCHEMAS
class DocumentExtractionTool(BaseModel):
    target_url: str = Field(description="The web URL or storage path of the document.")
    extract_fields: List[str] = Field(description="Specific terms or sections to parse out.")

# 3. DEFINE THE ROUTING & EXECUTION GRAPH
def call_model(state: AgentState):
    """Simulates the core agent node pulling and processing context."""
    print("\n[Node: agent_core] Processing state workflow...")
    
    # 1. Simulate document intelligence layout parsing
    parsed_markdown = pipeline.simulate_document_intelligence_layout("report.pdf")
    
    # 2. Simulate chunking behavior
    chunks = pipeline.chunk_document(parsed_markdown)
    
    # 3. Simulate calling your zero-cost mock OpenAI client
    response = openai_client.chat.completions.create(
        model=settings.azure_openai_deployment_name,
        messages=[{"role": "user", "content": f"Context: {chunks[0].content}"}]
    )
    print(f"🤖 LLM Structural Output: {response.choices[0].message.content}")
    
    return {
        "messages": state.get("messages", []),
        "current_action": "evaluating_document",
        "verification_passed": True
    }

def should_continue(state: AgentState) -> str:
    if state.get("current_action") == "evaluating_document":
        return "execute_tools"
    return END

# Initialize and compile the state graph
workflow = StateGraph(AgentState)
workflow.add_node("agent_core", call_model)
workflow.set_entry_point("agent_core")
workflow.add_conditional_edges("agent_core", should_continue, {
    "execute_tools": END,  
    END: END
})
app = workflow.compile()

# 4. VALIDATION RUNNER
if __name__ == "__main__":
    print("🚀 Running Ingestion & Routing Validation Runner...")
    test_tool = DocumentExtractionTool(
        target_url="https://example.com/report.pdf", 
        extract_fields=["metrics", "cost_optimization"]
    )
    print("✓ Pydantic V2 schemas initialized successfully.")
    
    initial_state = {
        "messages": [("user", "Analyze the latest cloud spend report.")],
        "current_action": "init",
        "verification_passed": False
    }
    
    output = app.invoke(initial_state)
    print("✓ LangGraph compiled and executed state transition successfully.")
    print(f"Final Action State: {output['current_action']}")
