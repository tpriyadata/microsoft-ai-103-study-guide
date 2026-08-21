# Memory, Tool Schemas, and Knowledge Integration

**Exam skill:** Choose appropriate memory, tool schemas, and knowledge integration.

## Core concept

An AI agent needs three things to work effectively:

> **MEMORY → TOOLS → KNOWLEDGE**

They solve **different problems**.

| Component                 | Main question                                    | Purpose                                           |
| ------------------------- | ------------------------------------------------ | ------------------------------------------------- |
| **Memory**                | “What should the agent remember?”                | Preserve context/state across interactions        |
| **Tool schema**           | “How can the agent use a tool correctly?”        | Define available actions and their inputs/outputs |
| **Knowledge integration** | “Where does the agent get reliable information?” | Connect the agent to external data/knowledge      |

---

# 1. Memory

Memory allows an agent to maintain information beyond a single interaction or reasoning step.

### Short-term / conversation memory

Maintains context during an ongoing conversation.

Example:

> User: "My favorite language is Python."
> User later: "What language should I use for this project?"

The agent can use the earlier conversation context.

### Long-term memory

Persists information that should remain available across sessions.

Examples:

* User preferences
* Previous interactions
* Customer profile
* Important application state
* Historical tasks

### State vs. memory

For exam questions, don't automatically assume every piece of information requires a database.

**State** = information needed to continue the current workflow.

**Memory** = information intentionally retained for future interactions.

---

# 2. Tool schemas

A tool schema tells the agent **how to call a tool**.

Think of it as the tool's **contract**.

For example:

```text id="0e6x6c"
Tool: get_weather

Input:
  location: string
  units: string

Output:
  temperature: number
  conditions: string
```

The agent uses the schema to understand:

* Tool name
* What the tool does
* Required parameters
* Optional parameters
* Parameter data types
* Expected output

### Why schemas matter

Without a clear schema, an agent may:

* Call the wrong tool
* Provide incorrect parameters
* Omit required fields
* Use the wrong data type
* Misinterpret the result

### Exam clue

If the scenario says:

> "Ensure the agent supplies correctly structured parameters when calling an API."

Think:

### **Tool schema / structured tool definition**

---

# 3. Knowledge integration

Knowledge integration connects an agent to **external sources of information**.

The model's built-in knowledge may not contain:

* Your company's documents
* Current inventory
* Internal policies
* Customer records
* Newly created documents
* Frequently changing information

Instead, connect the agent to appropriate data sources.

### Common pattern

```text id="5v5j5p"
User
 ↓
Agent
 ↓
Knowledge retrieval
 ↓
Azure AI Search
 ↓
Documents / indexed data
 ↓
Relevant information
 ↓
Agent response
```

This is commonly associated with **RAG — Retrieval-Augmented Generation**.

---

# Memory vs. Knowledge

This is a **very important exam distinction**.

### Memory

> **"Remember what happened with this user."**

Example:

The customer prefers email communication.

### Knowledge

> **"Find the correct information about our product."**

Example:

Retrieve the company's current return policy from its documentation.

### Easy trick

> **Memory = ABOUT the user/conversation**
> **Knowledge = ABOUT the world/data**

---

# Tool vs. Knowledge

Another common exam distinction.

### Tool

Allows the agent to **perform an action or retrieve dynamic information**.

Examples:

* Create ticket
* Send email
* Query an API
* Check inventory
* Schedule appointment

### Knowledge source

Provides information the agent can **retrieve and use for reasoning**.

Examples:

* Company documentation
* PDFs
* Product manuals
* Indexed websites
* Knowledge bases

### Memory trick

> **Knowledge tells the agent.**
> **Tools let the agent do.**

---

# Putting all three together

Consider an HR agent.

### User asks:

> "What is my remaining vacation balance, and can you request vacation for next Friday?"

The agent may need:

**Memory**

→ Know the user's identity/context.

**Knowledge**

→ Retrieve company vacation policy.

**Tool**

→ Query the HR system for the actual vacation balance.

**Tool**

→ Submit the vacation request.

**HITL**

→ Potentially require manager approval before final submission.

Architecture:

```text
                 ┌─────────────┐
                 │   Memory    │
                 └──────┬──────┘
                        ↓
User → Agent ← Knowledge / RAG
          │
          ├── HR API → Vacation balance
          │
          └── Request tool → Vacation request
                              │
                              ↓
                         Human approval
```

This demonstrates how these concepts work together rather than being interchangeable.

---

# Exam decision framework

When reading a scenario, ask:

### **1. Does the agent need to remember something?**

→ **Memory**

### **2. Does the agent need factual information from external data?**

→ **Knowledge integration / RAG**

### **3. Does the agent need to perform an action?**

→ **Tool**

### **4. Does the tool require structured inputs?**

→ **Tool schema**

### **5. Does the action require human approval?**

→ **HITL**

---

# Memory trick

## **"Remember → Retrieve → Act"**

**Remember**
→ Memory

**Retrieve knowledge**
→ RAG / Azure AI Search / knowledge source

**Act**
→ Tool

And:

> **Schema = HOW to use the tool**

### One-line exam rule

> **Use memory for persistent context, knowledge integration for external information, and well-defined tool schemas for safe, structured agent actions.**
