# Security, Guardrails, and RBAC

**Exam skill:** Implement security, guardrails, and role-based access controls (RBAC).

## Core concept

For AI-103, think about security at **three different layers**:

> **Identity & permissions → AI guardrails → Network/data protection**

### 1. Identity and RBAC — *Who can access what?*

**Azure RBAC** controls what a user, group, service principal, or managed identity can do with an Azure resource.

Think:

**Who → can perform what action → on which resource**

Examples:

* Developer → manage an AI Foundry project
* Data scientist → use AI resources
* Application managed identity → read data from Azure Storage
* Administrator → manage the Azure AI resource

### Important distinction

**Authentication** = *Who are you?*

**Authorization** = *What are you allowed to do?*

**RBAC** = Azure's mechanism for authorization.

---

## 2. Guardrails — *What should the AI be allowed to produce/do?*

Guardrails constrain AI behavior.

Examples:

* Block harmful content
* Filter inappropriate prompts/responses
* Prevent sensitive information from being exposed
* Restrict what an agent can do
* Validate model outputs
* Require human approval for high-risk actions
* Detect prompt-injection attempts
* Limit tool access

For generative AI, **Azure AI Content Safety** is an important service to know.

It can help detect/filter categories such as:

* Hate
* Sexual content
* Violence
* Self-harm

### Exam clue

If the question says:

> "Prevent the model from generating harmful or inappropriate content."

Think:

**Content Safety / content filtering**

If it says:

> "Control which Azure resources a developer can manage."

Think:

**Azure RBAC**

Don't confuse the two.

---

## 3. Network security — *How can the resource be reached?*

For sensitive enterprise AI applications, you may need private connectivity.

Important concepts:

| Requirement                           | Think                       |
| ------------------------------------- | --------------------------- |
| Authenticate users                    | **Microsoft Entra ID**      |
| Give Azure resource permissions       | **Azure RBAC**              |
| Avoid credentials in application code | **Managed identity**        |
| Private access to Azure resource      | **Private Endpoint**        |
| Isolate network traffic               | **VNet/network controls**   |
| Store secrets securely                | **Azure Key Vault**         |
| Filter harmful AI content             | **Azure AI Content Safety** |

---

## 4. Least privilege

This is a **very important exam principle**.

Give an identity **only the permissions it actually needs**.

Bad:

> Application gets Owner access to the entire subscription.

Better:

> Application's managed identity gets only the required role on the specific resource.

### Memory trick

**"Minimum permission, maximum protection."**

If the question asks how to securely allow an application to access an Azure service:

**Managed identity + appropriate RBAC role**

is often the direction to consider.

---

# Guardrails vs RBAC

This distinction is extremely important:

| Scenario                                            | Correct concept                 |
| --------------------------------------------------- | ------------------------------- |
| Who can deploy a model?                             | **RBAC**                        |
| Who can access an Azure AI resource?                | **RBAC**                        |
| Application needs access without storing a password | **Managed identity**            |
| Block harmful model output                          | **Guardrails / Content Safety** |
| Prevent sensitive information from being exposed    | **Guardrails/data protection**  |
| Restrict an agent's tools                           | **Tool-access constraints**     |
| Require approval before an agent performs an action | **Human oversight**             |
| Keep an Azure service off the public internet       | **Private Endpoint**            |
| Store API keys/secrets                              | **Key Vault**                   |

---

# Exam scenario

### Scenario

You build an AI agent that can:

* Search company documents
* Create support tickets
* Issue refunds

The company requires:

* Employees can use the agent
* The application must not store Azure credentials
* Refunds above $1,000 require human approval
* Harmful content must be filtered
* The AI resources must be accessed privately

### Think layer by layer:

**Employee access**

→ Microsoft Entra ID + RBAC

**Application authentication**

→ Managed identity

**High-value refund**

→ Human oversight / approval

**Harmful content**

→ AI guardrails / Content Safety

**Private AI resource access**

→ Private Endpoint

This is exactly the kind of **multi-requirement scenario** where AI-103 can test whether you understand which security mechanism solves which problem.

---

# Memory trick

## **"WHO – WHAT – WHERE – HOW"**

**WHO** can access it?
→ **Entra ID + RBAC**

**WHAT can the AI say/do?**
→ **Guardrails + Content Safety**

**WHERE can it connect from?**
→ **Private Endpoint + VNet**

**HOW does the application authenticate?**
→ **Managed Identity**

### One-line exam rule

> **RBAC controls access to Azure resources; guardrails control AI behavior; managed identity secures application authentication; private endpoints secure network access.**
