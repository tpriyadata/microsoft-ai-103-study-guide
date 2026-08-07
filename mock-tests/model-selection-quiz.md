# Mock Test — Model Selection

10 questions | Target: Microsoft-style scenario reasoning
Belongs to: [../topics/domain-2-generative-agentic/model-selection.md](../topics/domain-2-generative-agentic/model-selection.md)
Framework used: [../frameworks/model-selection-decision-framework.md](../frameworks/model-selection-decision-framework.md)

---

## Q1
A retail company wants an agent that reads product photos uploaded by customers and identifies visible defects. Which model type should be used?
- A. LLM
- B. SLM
- C. Multimodal model
- D. Foundry code-interpreter tool

<details><summary>Answer</summary>C — the input is an image; no text-only model can process visual defect detection directly.</details>

---

## Q2
A manufacturing line needs real-time anomaly classification running on an edge device with no internet connectivity, using short structured sensor readings.
- A. LLM
- B. SLM
- C. Multimodal model
- D. Foundry file search tool

<details><summary>Answer</summary>B — on-device/offline + narrow, well-defined classification task = SLM.</details>

---

## Q3
A legal team needs a solution that answers questions grounded in the latest public web content, with citations, and doesn't want to build a custom web-scraping/retrieval pipeline.
- A. LLM alone
- B. SLM alone
- C. Multimodal model
- D. Foundry Bing grounding tool

<details><summary>Answer</summary>D — this is a pre-built Foundry Tool use case; don't hand-build web retrieval when the tool exists.</details>

---

## Q4
A support desk wants to summarize a 40-page policy document and answer open-ended, multi-step follow-up questions about it.
- A. LLM
- B. SLM
- C. Multimodal model
- D. Foundry computer-use tool

<details><summary>Answer</summary>A — long-context synthesis and open-ended multi-step reasoning favors an LLM.</details>

---

## Q5
A cost-sensitive startup needs to tag thousands of short customer reviews per day as positive/negative/neutral, on a tight budget.
- A. LLM
- B. SLM
- C. Multimodal model
- D. Foundry grounding tool

<details><summary>Answer</summary>B — narrow, high-volume, cost-constrained classification = SLM.</details>

---

## Q6
An agent must watch uploaded video clips and generate timestamped captions describing on-screen action.
- A. LLM
- B. SLM
- C. Multimodal model
- D. Foundry file search tool

<details><summary>Answer</summary>C — video input requires multimodal capability.</details>

---

## Q7
A developer wants an agent that can write and execute Python code to solve a user's data analysis question, returning computed results.
- A. LLM alone, prompted to "pretend" to run code
- B. SLM
- C. Multimodal model
- D. Foundry code interpreter tool

<details><summary>Answer</summary>D — actual code execution should use the managed Foundry code interpreter tool rather than relying on the model to simulate execution.</details>

---

## Q8
A scenario states the solution must run fully offline on a mobile device with strict latency under 200ms, performing simple intent classification.
- A. LLM
- B. SLM
- C. Multimodal model
- D. Foundry Tool

<details><summary>Answer</summary>B — offline + strict latency + narrow task is the textbook SLM trigger, even though "intent classification" sounds like it could use an LLM.</details>

---

## Q9
A scenario describes a task that is broad and ambiguous in scope, requiring the model to plan multiple steps, but includes no cost, latency, offline, or modality constraints.
- A. LLM
- B. SLM
- C. Multimodal model
- D. Foundry Tool

<details><summary>Answer</summary>A — absent any constraint, default to the model matching the reasoning complexity: LLM.</details>

---

## Q10
A distractor option offers "a more powerful LLM" for a task that requires reading a scanned image of a handwritten form. Why is this wrong?
- A. LLMs are always more expensive than multimodal models
- B. Modality mismatch — no LLM reasoning capability substitutes for the ability to process image input
- C. Foundry Tools are always required for scanned documents
- D. SLMs are cheaper so they're always preferred

<details><summary>Answer</summary>B — this is the "modality mismatch" trap called out in the decision framework: capability doesn't fix a model that can't accept the input type at all.</details>