# Design Azure Infrastructure for AI Apps and Agent-Based Solutions

**Exam skill:** Design Azure infrastructure for AI applications and agent-based solutions.
# Design Azure Infrastructure for AI Apps and Agent-Based Solutions

**Exam skill:** Design Azure infrastructure for AI applications and agent-based solutions.
**Official domain:** Plan and manage an Azure AI solution (25–30%) — **“Set up AI solutions in Foundry”**

## Core concept

Design the Azure infrastructure based on **what the AI application needs to do, how it will be deployed, and what security/networking requirements apply**.

For AI-103, think in terms of this architecture:

**User/Application → Azure AI Foundry Project → Model/Agent → Tools & Data → Security/Networking → Monitoring**

### 1. Azure AI Foundry

**Azure AI Foundry** is the primary environment for building and managing AI applications and agents.

Know the distinction:

| Component            | Purpose                                                                                   |
| -------------------- | ----------------------------------------------------------------------------------------- |
| **Foundry resource** | Azure resource that provides the AI development/service environment                       |
| **Foundry project**  | Workspace for organizing models, agents, connections, evaluations, and application assets |
| **Hub**              | Shared organizational foundation for projects, governance, security, and resources        |
| **Model deployment** | Makes a selected model available for inference                                            |
| **Agent**            | AI application that can reason, use instructions, tools, and data                         |

### 2. Choose the right model deployment

A major exam decision is **how the model should be hosted/deployed**.

Think:

**Serverless / pay-as-you-go → flexibility and simpler deployment**

**Provisioned throughput → predictable capacity and performance**

If the scenario emphasizes:

* Variable workload → **serverless/pay-as-you-go**
* Predictable high-volume production traffic → **provisioned throughput**
* Strict performance/capacity requirements → consider **dedicated/provisioned capacity**

---

### 3. Data and knowledge infrastructure

Agentic AI applications often need external data.

Typical architecture:

**Azure AI Search → indexes → vector/hybrid search → agent/RAG**

Use Azure AI Search when the application needs:

* Document retrieval
* Vector search
* Keyword search
* Hybrid search
* Semantic ranking
* RAG

For structured application data, consider services such as:

* Azure SQL
* Azure Cosmos DB
* Azure Storage
* PostgreSQL

The important exam question is usually:

> **Where should the agent get its knowledge from?**

Not every problem requires putting everything into the model's prompt.

---

### 4. Networking and security

For enterprise AI applications, infrastructure design must account for network isolation.

Key concepts:

**Public endpoint**

→ Easier access
→ Less network isolation

**Private endpoint**

→ Private connectivity through Azure Virtual Network
→ Useful when resources shouldn't be publicly exposed

**Managed identity**

→ Allows Azure resources/applications to authenticate to other Azure services without embedding secrets.

**RBAC**

→ Controls **who can access what**.

Think:

> **Private Endpoint = network path**
> **Managed Identity = identity**
> **RBAC = permissions**

These three are easy to confuse on the exam.

---

### 5. Agent infrastructure

An agent-based application can look like:

```text
User
  ↓
Application / API
  ↓
AI Foundry Agent
  ↓
 ┌───────────────┬───────────────┬───────────────┐
 ↓               ↓               ↓
LLM           AI Search       External Tools
                  ↓               ↓
              Documents       APIs / Functions
```

The agent should have access **only to the tools and data it needs**.

For sensitive operations:

**Agent → approval → tool execution**

rather than:

**Agent → unrestricted tool execution**

This connects directly to the **agent oversight and tool-access constraints** topic you just studied.

---

## Infrastructure decision framework

When you see an architecture scenario, ask these questions in order:

### **1. WHAT are you building?**

* Generative AI application?
* RAG application?
* AI agent?
* Multi-agent system?
* Computer vision application?
* Speech application?

### **2. WHERE should it run?**

* Azure AI Foundry
* Azure AI services
* Azure compute/container services
* Serverless application hosting
* Other Azure services

### **3. WHICH model deployment?**

* Serverless/pay-per-token
* Provisioned throughput/dedicated capacity

### **4. WHERE is the data?**

* Azure AI Search
* Storage
* SQL
* Cosmos DB
* PostgreSQL
* External system

### **5. HOW is it secured?**

* Microsoft Entra ID
* Managed identity
* RBAC
* Private endpoint
* VNet/network controls
* Key Vault/secrets where needed

### **6. HOW is it monitored?**

* Application Insights
* Azure Monitor
* Foundry evaluation/monitoring capabilities
* Logging/tracing

---

## Memory trick

### **"MODEL → DATA → TOOLS → NETWORK → IDENTITY → MONITOR"**

For an AI infrastructure question, mentally walk through:

**M** → Which **Model**?
**D** → Which **Data**?
**T** → Which **Tools**?
**N** → Which **Network**?
**I** → Which **Identity/permissions**?
**M** → How do you **Monitor**?

### Fast exam associations

| If the question says...           | Think...                                 |
| --------------------------------- | ---------------------------------------- |
| Build/manage AI apps and agents   | **Azure AI Foundry**                     |
| Organize AI project assets        | **Foundry project**                      |
| Shared governance across projects | **Hub**                                  |
| RAG/document retrieval            | **Azure AI Search**                      |
| Private Azure connectivity        | **Private Endpoint**                     |
| Avoid storing credentials in code | **Managed Identity**                     |
| Control resource permissions      | **RBAC**                                 |
| Predictable model capacity        | **Provisioned throughput**               |
| Variable/unpredictable workload   | **Serverless/pay-as-you-go**             |
| Monitor application performance   | **Azure Monitor / Application Insights** |
| Agent needs external capability   | **Tool/function/API connection**         |
| High-impact action needs approval | **Human oversight**                      |

### One-line exam rule

> **Design the smallest secure Azure architecture that gives the AI application the model, data, tools, connectivity, identity, and monitoring it actually needs.**
md

## Referenced by
- mock-tests/infra-design-quiz.md
- mock-tests/infra-design-quiz-hardmode.md
- frameworks/infra-design-decision-framework.md
