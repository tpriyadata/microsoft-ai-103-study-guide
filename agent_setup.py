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


# 2. DEFINE SYSTEM TOOL SCHEMAS
class DocumentExtractionTool(BaseModel):
    target_url: str = Field(description="The web URL or storage path of the document.")
    extract_fields: List[str] = Field(description="Specific terms or sections to parse out.")


# 3. DEFINE NODES

def content_safety_guardrail(state: AgentState):
    """Simulates Azure AI Content Safety Prompt Shields to catch jailbreaks."""
    print("\n🛡️  [Node: safety_guardrail] Evaluating user input safety...")

    messages = state.get("messages", [])
    user_input = ""
    if messages:
        # Works whether message is a tuple ("user", text) or a LangChain Message object
        last_msg = messages[-1]
        user_input = last_msg[1] if isinstance(last_msg, tuple) else getattr(last_msg, "content", "")

    banned_keywords = ["ignore instructions", "system override", "bypass restriction", "dump data"]

    if any(trigger in user_input.lower() for trigger in banned_keywords):
        print("🚨 [SECURITY TRIGGER] Azure Content Safety: Prompt Shield Blocked an Exploitation Attempt!")
        return {
            "current_action": "blocked_by_safety",
            "verification_passed": False,
        }

    print("✅ [SECURITY PASSED] Input clears Azure Content Safety Guardrail.")
    return {
        "current_action": "safety_cleared",
        "verification_passed": True,
    }


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
        messages=[{"role": "user", "content": f"Context: {chunks[0].content}"}],
    )
    print(f"🤖 LLM Structural Output: {response.choices[0].message.content}")

    # Hand off to the tool-execution branch for downstream extraction
    return {
        "current_action": "evaluating_document",
    }


def execute_tools(state: AgentState):
    """Simulates running the DocumentExtractionTool against the parsed content."""
    print("\n🔧 [Node: execute_tools] Executing extraction tool against parsed document...")

    tool_call = DocumentExtractionTool(
        target_url="https://example.com/report.pdf",
        extract_fields=["metrics", "cost_optimization"],
    )
    print(f"✓ Extracted fields requested: {tool_call.extract_fields}")

    return {
        "current_action": "tool_execution_complete",
    }


# 4. DEFINE ROUTING LOGIC

def route_after_safety(state: AgentState) -> str:
    return "agent_core" if state.get("verification_passed") else END


def route_after_agent(state: AgentState) -> str:
    if state.get("current_action") == "evaluating_document":
        return "execute_tools"
    return END


# 5. BUILD THE STATE GRAPH (single definition — no duplicates)
workflow = StateGraph(AgentState)

workflow.add_node("safety_guardrail", content_safety_guardrail)
workflow.add_node("agent_core", call_model)
workflow.add_node("execute_tools", execute_tools)

workflow.set_entry_point("safety_guardrail")

workflow.add_conditional_edges(
    "safety_guardrail",
    route_after_safety,
    {
        "agent_core": "agent_core",
        END: END,
    },
)

workflow.add_conditional_edges(
    "agent_core",
    route_after_agent,
    {
        "execute_tools": "execute_tools",  # <-- now actually routes to the tool node
        END: END,
    },
)

# execute_tools always terminates the graph after running
workflow.add_edge("execute_tools", END)

app = workflow.compile()


# 6. VALIDATION RUNNER (single entry point — no duplicate __main__ blocks)
if __name__ == "__main__":
    print("🚀 Running Ingestion & Routing Validation Runner...")

    test_tool = DocumentExtractionTool(
        target_url="https://example.com/report.pdf",
        extract_fields=["metrics", "cost_optimization"],
    )
    print("✓ Pydantic V2 schemas initialized successfully.")

    initial_state = {
        "messages": [("user", "Analyze the latest cloud spend report.")],
        "current_action": "init",
        "verification_passed": False,
    }

    output = asyncio.run(app.ainvoke(initial_state))
    print("✓ LangGraph compiled and executed state transition successfully.")
    print(f"🏁 Final Action State: {output['current_action']}")