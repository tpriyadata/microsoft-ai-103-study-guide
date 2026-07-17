from typing import Annotated, List
from pydantic import BaseModel, Field
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END
import asyncio

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

def content_safety_guardrail(state: AgentState):
    """Simulates Azure AI Content Safety Prompt Shields to catch jailbreaks."""
    print("\n🛡️ [Node: safety_guardrail] Evaluating user input safety...")
    
    # Extract text from the last message in the state
    messages = state.get("messages", [])
    user_input = ""
    if messages:
        # Works whether message is a tuple ("user", text) or a LangChain Message object
        last_msg = messages[-1]
        user_input = last_msg[1] if isinstance(last_msg, tuple) else getattr(last_msg, "content", "")
    
    banned_keywords = ["ignore instructions", "system override", "bypass restriction", "dump data"]
    
    # Catch jailbreak signatures or injection attempts
    if any(trigger in user_input.lower() for trigger in banned_keywords):
        print("🚨 [SECURITY TRIGGER] Azure Content Safety: Prompt Shield Blocked an Exploitation Attempt!")
        return {
            "current_action": "blocked_by_safety",
            "verification_passed": False
        }
    
    print("✅ [SECURITY PASSED] Input clears Azure Content Safety Guardrail.")
    return {
        "current_action": "safety_cleared",
        "verification_passed": True
    }

# 2. DEFINE SYSTEM TOOL SCHEMAS
class DocumentExtractionTool(BaseModel):
    target_url: str = Field(description="The web URL or storage path of the document.")
    extract_fields: List[str] = Field(description="Specific terms or sections to parse out.")

# 3. DEFINE THE ROUTING & EXECUTION GRAPH
async def call_model(state: AgentState):
    """Simulates the core agent node pulling and processing context."""
    print("\n[Node: agent_core] Processing state workflow...")
    
    # 1. Simulate document intelligence layout parsing
    parsed_markdown = await pipeline.simulate_document_intelligence_layout("report.pdf")
    
    # 2. Simulate chunking behavior
    chunks = await pipeline.chunk_document(parsed_markdown)
    
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

# Your current edge definition:
workflow.add_conditional_edges(
    "agent_core",
    should_continue,
    {
        "execute_tools": END,  # <--- Note this mapping
        "end": END
    }
)

# Initialize and compile the state graph
workflow = StateGraph(AgentState)

workflow.add_node("safety_guardrail", content_safety_guardrail)
workflow.add_node("agent_core", call_model)

workflow.set_entry_point("safety_guardrail")

workflow.add_conditional_edges(
    "safety_guardrail",
    lambda state: "agent_core" if state.get("verification_passed") else END,
    {
        "agent_core": "agent_core",
        END: END
    }
)

workflow.add_conditional_edges(
    "agent_core", 
    should_continue, 
    {
        "execute_tools": END,  
        END: END
    }
)

app = workflow.compile()

# CLEANED RUNNER: Keeps the module importable by test suites
if __name__ == "__main__":
    print("🚀 Graph compiled successfully. Run 'python test_suite.py' to evaluate variants.")
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
    
    output = asyncio.run(app.invoke(initial_state))
    print("✓ LangGraph compiled and executed state transition successfully.")
    print(f"Final Action State: {output['current_action']}")

    
