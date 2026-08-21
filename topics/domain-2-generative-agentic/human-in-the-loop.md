# Autonomous / Semi-Autonomous Workflows with HITL

**Exam skill:** Build autonomous or semi-autonomous workflows with human-in-the-loop approval.

## Core concept

**Human-in-the-loop (HITL)** means an AI agent can perform work autonomously, but **pauses and asks a human for approval before a defined action**.

The key idea:

> **Let the agent automate low-risk work, but put a human checkpoint before high-risk or irreversible actions.**

### Autonomous vs. semi-autonomous

| Workflow             | Agent behavior                                                  | Human involvement                      |
| -------------------- | --------------------------------------------------------------- | -------------------------------------- |
| **Fully autonomous** | Agent plans and executes actions independently                  | No approval required                   |
| **Semi-autonomous**  | Agent performs routine steps but pauses at selected checkpoints | Approval required for specific actions |
| **HITL**             | Human explicitly reviews/approves/rejects an action             | Human is part of the execution loop    |

### Example

An AI purchasing agent:

```text
User request
     ↓
Agent analyzes requirement
     ↓
Agent searches suppliers
     ↓
Agent compares prices
     ↓
Agent creates purchase order
     ↓
   💡 HITL
Human reviews
   ↙     ↘
Approve  Reject
   ↓       ↓
Purchase  Stop
```

The agent is still doing most of the work autonomously, but the **purchase execution is gated by human approval**.

---

## When should you use HITL?

HITL is especially appropriate when an agent can:

* Spend money
* Delete or modify important data
* Send external communications
* Make consequential business decisions
* Approve transactions
* Change production systems
* Perform actions with legal/compliance implications
* Take an action that is difficult to reverse

### Exam clue

If you see:

> **"The agent must obtain approval before..."**

Think:

### **HITL**

---

## Approval patterns

### 1. Approve

Human reviews the proposed action and allows execution.

**Agent → Human → Approve → Tool execution**

### 2. Reject

Human rejects the proposed action.

**Agent → Human → Reject → Stop/modify**

### 3. Request changes

Human provides feedback.

**Agent → Human → Feedback → Agent revises → Human reviews again**

This creates an iterative workflow.

---

# HITL vs. Human-on-the-loop

This distinction can appear in scenarios.

### Human-in-the-loop

Human approval is **required before a specific action**.

> "A manager must approve every refund above $1,000."

→ **HITL**

### Human-on-the-loop

The agent operates independently while a human **monitors and can intervene**.

> "The agent processes support tickets automatically while supervisors monitor its activity and can intervene when necessary."

→ **Human-on-the-loop**

### Easy memory trick

> **IN = human is IN the decision.**
> **ON = human is ON the system, monitoring it.**

---

# HITL + tool constraints

HITL becomes especially powerful when combined with **tool-access restrictions**.

For example:

| Agent capability        | Control            |
| ----------------------- | ------------------ |
| Search documents        | Autonomous         |
| Generate recommendation | Autonomous         |
| Create draft email      | Autonomous         |
| Send email externally   | **Human approval** |
| Issue $50 refund        | Autonomous         |
| Issue $5,000 refund     | **Human approval** |
| Delete customer data    | **Human approval** |

This is a good production design because you don't unnecessarily slow down every action.

---

# Exam decision framework

When you see an agent workflow question, ask:

### **1. Is the action low risk?**

If yes → allow automation.

### **2. Is the action consequential or irreversible?**

If yes → consider **HITL**.

### **3. Does the human need to approve before execution?**

Yes → **HITL**

### **4. Does the human only monitor and intervene when necessary?**

Yes → **Human-on-the-loop**

### **5. Should the agent never have access to that capability?**

Then don't give it the tool/permission in the first place.

That's **tool-access restriction**, not HITL.

---

## Memory trick

### **"AUTOMATE → PAUSE → APPROVE → ACT"**

For semi-autonomous workflows:

**AUTOMATE** routine work
↓
**PAUSE** at a risky action
↓
**APPROVE** by human
↓
**ACT** using the tool

### One-line exam rule

> **Use autonomous execution for routine, low-risk tasks and introduce a human approval checkpoint before consequential, sensitive, or irreversible actions.**
