# Configure model, tool, and agent deployments

**Exam skill:** Configure model, tool, and agent deployments in Microsoft Foundry.

## Core concept

A **deployment** makes an AI model or capability available for an application to use in Microsoft Foundry.

Think in **3 deployment categories**:

* **Model deployment** → Deploy a selected model to an Azure AI Foundry resource/project so applications can send inference requests to it.
* **Tool deployment/configuration** → Make tools and capabilities available to an agent, such as **web search, file search, code interpreter, or other connected tools**.
* **Agent deployment** → Publish/deploy an agent so applications can interact with the agent through an endpoint or supported interface.

### Model deployment

When configuring a model deployment, pay attention to:

* **Model** — Which model/version are you deploying?
* **Deployment type** — For example, standard/serverless or provisioned options where supported.
* **Region** — The model must be available in the selected region.
* **Capacity/quotas** — Determines how much traffic the deployment can handle.
* **Authentication** — Applications need the appropriate credentials/identity to invoke the deployment.

**Exam clue:**
If the question asks **“Which model should the application send the request to?”**, think **deployment name/endpoint** rather than simply the model catalog name.

### Tool configuration

Tools extend an agent beyond basic model generation.

Examples include:

* **Web search** → Retrieve current information.
* **File search/retrieval** → Ground responses in uploaded or indexed data.
* **Code interpreter** → Execute code and perform calculations/data analysis.
* **Custom tools/functions** → Allow the agent to call application APIs or business logic.

The important distinction is:

> **Model = reasoning/generation**
> **Tool = capability/action**
> **Agent = orchestrates the model + instructions + tools**

### Agent deployment

An agent combines:

**Instructions + Model + Tools + Conversation/State**

The agent determines **how** the model should behave and **when** it should use available tools.

For production scenarios, consider:

* Identity and authentication
* Tool permissions
* Environment separation
* Monitoring/evaluation
* Versioning
* Deployment configuration

### Exam decision pattern

| Scenario                                            | Think                           |
| --------------------------------------------------- | ------------------------------- |
| Need text/image generation                          | **Model deployment**            |
| Need current web information                        | **Web search tool**             |
| Need answers grounded in files                      | **File search/retrieval**       |
| Need calculations/code execution                    | **Code interpreter**            |
| Need an AI assistant that decides when to use tools | **Agent**                       |
| Need to expose the agent to an application          | **Agent deployment/publishing** |

## Memory trick

### **M → T → A**

**Model → Tool → Agent**

> **Model = Think**
> **Tool = Do**
> **Agent = Coordinate**

Or remember:

**“Model thinks, Tool acts, Agent orchestrates.”**

### High-value AI-103 trap

Don't confuse **model**, **deployment**, and **agent**:

**Model** = the AI model itself
↓
**Deployment** = an accessible instance/configuration of that model
↓
**Agent** = an application-level AI system that uses a model plus instructions and tools.

So when you see **“configure model, tool, and agent deployments”**, first identify **what the application actually needs** before choosing the deployment/configuration option.
