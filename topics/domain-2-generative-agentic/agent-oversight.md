# Agent oversight and tool-access constraints

**Exam skill:** Govern agent behavior using oversight modes and tool-access constraints.


**Agent oversight** means controlling **how much freedom an AI agent has to act on its own** and **which tools/resources it is allowed to use**.

For AI-103, think about two separate controls:

### 1. Oversight modes — *How much human control?*

| Mode                  | Agent behavior                                                      | Human involvement |
| --------------------- | ------------------------------------------------------------------- | ----------------- |
| **Autonomous**        | Agent plans and executes actions independently                      | Minimal           |
| **Supervised**        | Agent can act, but important actions require human review/approval  | Moderate          |
| **Human-in-the-loop** | Agent pauses and asks a person before performing designated actions | High              |
| **Human-on-the-loop** | Agent operates independently while humans monitor and can intervene | Monitoring        |

**Exam clue:**
If the scenario says **"require approval before sending an email / making a purchase / deleting data"** → choose an oversight mechanism that requires **human approval before that action**.

---

### 2. Tool-access constraints — *What is the agent allowed to do?*

An agent should **not automatically have unrestricted access to every tool**.

You can constrain:

* **Which tools** the agent can call
* **Which operations** it can perform
* **Which data/resources** it can access
* **When** a tool can be used
* **Which actions require approval**
* **Permissions/roles** associated with the tool

For example:

> Customer-support agent → can search customer records and create a support ticket → **cannot issue refunds without approval**.

The important distinction is:

**Oversight = control the agent's actions.**
**Tool constraints = limit the agent's capabilities.**

---

### Scenario example

A company builds an AI purchasing agent.

The agent should:

1. Search approved suppliers ✅
2. Compare prices ✅
3. Create a purchase recommendation ✅
4. Purchase items under $500 automatically ✅
5. Require manager approval for purchases over $500 🔐

The correct design combines:

**Tool access constraints** → restrict the agent to approved purchasing tools.

**Oversight** → require human approval for high-risk/high-value purchases.

---

## Memory trick

### **"WHO controls WHAT?"**

**WHO controls the agent? → Oversight**

**WHAT can the agent access/do? → Tool constraints**

Or remember:

> **Oversight = Freedom**
> **Tool constraints = Permissions**

### Exam shortcut

If you see:

* **"human approval"** → Oversight
* **"restrict tool access"** → Tool constraint
* **"only approved tools"** → Tool constraint
* **"agent can act independently"** → Autonomous operation
* **"review before action"** → Human-in-the-loop
* **"monitor and intervene"** → Human-on-the-loop

---

## Related concepts

This topic connects closely to:

**Agent → Planning → Tool selection → Tool execution → Oversight → Validation**

A production agent should follow the principle:

> **Give the agent the minimum permissions it needs, and require human approval for consequential actions.**

That is essentially **least privilege + appropriate human oversight**.
