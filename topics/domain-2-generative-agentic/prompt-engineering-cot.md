# Prompt Engineering, Reflection, and Chain-of-Thought Evaluation

**Exam skill:** Implement advanced prompt engineering, model reflection, and chain-of-thought evaluation loops.

## Core concept

For AI-103, think of this topic as:

> **PROMPT → GENERATE → REFLECT → EVALUATE → IMPROVE**

The goal isn't simply to make the model answer. It's to make the **output more reliable, accurate, consistent, and aligned with the task**.

---

# 1. Advanced prompt engineering

A good prompt gives the model enough information to understand:

* **Role** — what the model should act as
* **Task** — what it needs to accomplish
* **Context** — relevant information
* **Constraints** — what it must or must not do
* **Examples** — desired input/output patterns
* **Output format** — how the response should be structured

### Example

Instead of:

> "Summarize this document."

Use:

```text id="f0xj3a"
You are a technical analyst.

Summarize the document for a software engineering team.

Requirements:
- Identify the three most important findings.
- List risks separately.
- Do not invent information.
- Use only information contained in the document.
- Return the result as structured JSON.
```

The second prompt gives the model **role + task + constraints + output requirements**.

---

# 2. Zero-shot, few-shot, and one-shot prompting

### Zero-shot

No examples.

> "Classify this customer message as Billing, Sales, or Support."

### One-shot

Provide **one example**.

```text
Example:
"Where is my invoice?" → Billing

Now classify:
"Why hasn't my payment appeared?" →
```

### Few-shot

Provide **multiple examples**.

Useful when you want the model to learn a specific pattern or classification style.

### Exam shortcut

**No examples → zero-shot**

**One example → one-shot**

**Several examples → few-shot**

---

# 3. Prompt decomposition

For complicated tasks, don't necessarily ask the model to solve everything in one instruction.

Break the problem into stages.

```text id="zj0h4k"
Input
  ↓
Extract information
  ↓
Analyze
  ↓
Validate
  ↓
Generate final response
```

This can improve reliability because each stage has a clearer responsibility.

---

# 4. Reflection

**Reflection** means asking a model to examine its own generated result and identify potential problems before producing the final answer.

Basic pattern:

```text id="m7g3c8"
User request
      ↓
Generate answer
      ↓
Reflect / critique
      ↓
Identify errors
      ↓
Revise
      ↓
Final answer
```

### Example

The model generates:

> "The customer is eligible for a refund."

Then a reflection step asks:

> "Check whether this conclusion is supported by the provided policy. Identify any unsupported assumptions."

The model may discover:

> "The policy requires the purchase to be within 30 days, but the date wasn't provided."

The system can then revise the response.

### Exam clue

If the scenario says:

> **"Generate a response, review it for errors, then improve it."**

Think:

### **Reflection**

---

# 5. Critique-and-revise pattern

A common reflection loop is:

**Generate → Critique → Revise**

For example:

```text id="q9h0pk"
             ┌─────────────┐
             │   Generate  │
             └──────┬──────┘
                    ↓
             ┌─────────────┐
             │   Critique  │
             └──────┬──────┘
                    ↓
             ┌─────────────┐
             │    Revise   │
             └──────┬──────┘
                    │
                    └──────→ Final
```

This is useful for:

* Writing
* Code generation
* Reasoning
* Document analysis
* Planning
* Agent workflows

---

# 6. Chain-of-thought

**Chain-of-thought (CoT)** refers to intermediate reasoning steps used to solve a complex problem.

Conceptually:

```text
Problem
  ↓
Reasoning steps
  ↓
Conclusion
```

It can help with tasks requiring:

* Multi-step reasoning
* Mathematics
* Logic
* Planning
* Complex decision making

### Important exam distinction

You should distinguish:

**Reasoning capability**
from
**exposing the model's private chain-of-thought to the user**.

For production applications, you generally want the system to return a **concise explanation, evidence, or rationale** rather than unnecessarily exposing hidden internal reasoning.

---

# 7. Chain-of-thought evaluation

Evaluation asks:

> **Did the model arrive at a good answer for the right reasons?**

You can evaluate outputs using criteria such as:

* Correctness
* Relevance
* Groundedness
* Completeness
* Consistency
* Safety
* Format compliance

For RAG systems, you might evaluate:

**Question → Retrieved context → Answer**

and determine whether the answer is actually supported by the retrieved information.

---

# 8. Model-as-a-judge

A model can evaluate another model's output.

Example:

```text id="0y2k4e"
Model A
   ↓
Generates answer
   ↓
Model B
   ↓
Evaluates answer
   ↓
Score / feedback
```

The evaluator can be instructed to score:

* Accuracy
* Relevance
* Grounding
* Style
* Safety

### Example

> "Rate this answer from 1–5 for factual accuracy and explain which requirement was not satisfied."

This is often called **LLM-as-a-judge** or **model-as-a-judge**.

---

# 9. Reflection vs evaluation

This distinction is important.

### Reflection

The model asks:

> **"How can I improve my answer?"**

Usually part of the generation workflow.

### Evaluation

The system asks:

> **"How good was the answer?"**

Usually used to measure quality.

Think:

**Reflection → improve**

**Evaluation → measure**

They can be combined:

```text
Generate
   ↓
Evaluate
   ↓
Reflect
   ↓
Revise
   ↓
Evaluate again
```

---

# 10. Advanced evaluation loop

A production-quality workflow might look like:

```text id="6gk4fp"
                    ┌──────────────┐
                    │ User Request │
                    └──────┬───────┘
                           ↓
                    ┌──────────────┐
                    │    Prompt    │
                    └──────┬───────┘
                           ↓
                    ┌──────────────┐
                    │    Generate  │
                    └──────┬───────┘
                           ↓
                    ┌──────────────┐
                    │    Evaluate  │
                    └──────┬───────┘
                           ↓
                     Pass? ──── No ──→ Reflect
                       │                 ↓
                      Yes             Revise
                       │                 │
                       ↓                 └──→ Evaluate
                    Response
```

This is particularly useful when the system has **quality requirements** that must be consistently met.

---

# Exam decision framework

When you see a scenario, ask:

### **"What is the problem?"**

**Need better instructions?**
→ Prompt engineering

**Need examples to establish a pattern?**
→ Few-shot prompting

**Need to break a complex task into steps?**
→ Prompt decomposition

**Need the model to review and improve its own output?**
→ Reflection

**Need to measure output quality?**
→ Evaluation

**Need another model to score the response?**
→ Model-as-a-judge

**Need complex multi-step reasoning?**
→ Reasoning / CoT-style approach

**Need to prevent unsupported answers in RAG?**
→ Grounding/citation evaluation

---

# Memory trick

## **"P-G-R-E-I"**

**P** → Prompt
**G** → Generate
**R** → Reflect
**E** → Evaluate
**I** → Improve

And remember:

> **Reflection = "Fix it."**
> **Evaluation = "Score it."**

### One-line exam rule

> **Use structured prompts to guide generation, reflection to identify and correct weaknesses, and evaluation loops to measure whether the resulting output satisfies quality and grounding requirements.**
