# Model Selection

**Exam skill:** Choose an appropriate model for each task, including **large language models (LLMs), small language models (SLMs), multimodal models, and Foundry Tools**.

## Core concept

For AI-103, don't choose a model simply because it is the **most powerful**.

Choose based on:

> **TASK → INPUT → COMPLEXITY → PERFORMANCE → COST**

The key question is:

**“What is the simplest appropriate model/service that can reliably solve this task?”**

---

# 1. Large Language Models — LLMs

LLMs are appropriate when the task requires **complex reasoning, broad knowledge, sophisticated language generation, or multi-step agent behavior**.

### Good use cases

* Complex reasoning
* Multi-step planning
* Agentic workflows
* Code generation
* Complex document analysis
* Sophisticated summarization
* Complex question answering
* Tool/function calling
* Conversational applications

### Example

> An enterprise agent must analyze a complex customer request, reason over several documents, choose appropriate tools, and formulate a detailed response.

→ **LLM**

### Exam clue

Words such as:

**complex reasoning, sophisticated, multi-step, planning, agentic**

→ Think **LLM**.

---

# 2. Small Language Models — SLMs

SLMs are smaller and generally require fewer computational resources.

They're useful when you need:

* Lower latency
* Lower cost
* High-volume inference
* Simpler tasks
* Specialized/narrow tasks
* Deployment where resources are constrained

### Good use cases

* Classification
* Simple extraction
* Routing
* Intent detection
* Basic summarization
* Simple text transformation
* High-volume repetitive processing

### Example

A company receives **millions of customer messages** and only needs to classify each as:

```text
Billing
Technical Support
Sales
Other
```

You probably don't need your largest model.

→ **SLM**

### Exam clue

**Simple + high volume + low latency + cost-sensitive**

→ Think **SLM**.

---

# 3. Multimodal models

Multimodal models handle **more than one type of input/output**, such as:

* Text
* Images
* Audio
* Video

Use them when the task requires understanding multiple modalities.

### Example

> A user uploads an image of a damaged machine and asks the AI to identify the visible problem.

Input:

**Image + text**

→ **Multimodal model**

Another example:

> Analyze a scanned document containing text, tables, and images.

→ **Multimodal capability**

### Exam clue

If the scenario contains:

**image + text, audio + text, video + text**

→ Think **multimodal model**.

---

# 4. Foundry Tools

This is an important distinction.

**You don't always need to select an LLM.**

Azure AI Foundry provides specialized AI capabilities/tools for specific tasks.

Use a specialized tool when the task is fundamentally a **specific AI capability**, rather than open-ended reasoning.

Examples include capabilities for:

* Speech
* Vision
* Document processing
* Content Safety
* Language
* Search/retrieval
* Other specialized AI workloads

### Example

> Extract structured fields such as invoice number, vendor, date, and total from thousands of invoices.

Instead of asking a general-purpose LLM to do everything:

→ Consider a **document-processing capability/tool** designed for extraction.

### Exam clue

If the requirement is:

> **"Use a specialized Azure AI capability to perform X."**

→ Consider **Foundry Tools / specialized AI service** before choosing a general-purpose LLM.

---

# LLM vs SLM vs Multimodal vs Foundry Tool

| Requirement                     | Best direction   |
| ------------------------------- | ---------------- |
| Complex reasoning               | **LLM**          |
| Multi-step agent                | **LLM**          |
| Sophisticated generation        | **LLM**          |
| Simple classification           | **SLM**          |
| High-volume simple processing   | **SLM**          |
| Low latency/cost                | **SLM**          |
| Image + text understanding      | **Multimodal**   |
| Audio + text                    | **Multimodal**   |
| Video/image analysis            | **Multimodal**   |
| Specialized document extraction | **Foundry Tool** |
| Speech recognition/synthesis    | **Foundry Tool** |
| Content moderation/safety       | **Foundry Tool** |
| Specialized AI capability       | **Foundry Tool** |

---

# Scenario-based exam examples

### Scenario 1

> A chatbot must reason through complex customer issues and call multiple APIs to resolve them.

**Answer: LLM**

Why?

Complex reasoning + agentic tool use.

---

### Scenario 2

> Classify 10 million short customer messages into five predefined categories at minimal cost.

**Answer: SLM**

Why?

Simple, repetitive, high-volume classification.

---

### Scenario 3

> Analyze a photograph of a damaged product and explain the problem in natural language.

**Answer: Multimodal model**

Why?

The model needs to understand an image and generate text.

---

### Scenario 4

> Extract fields from thousands of standardized business documents.

**Answer: Specialized Foundry/AI document capability**

Why?

This is a specialized document-processing task rather than open-ended reasoning.

---

### Scenario 5

> An agent needs to understand a complex user request, retrieve company documentation, decide which tool to call, and explain the result.

**Answer: LLM + knowledge retrieval + tools**

Don't think of model selection as always being **one model**. A production AI system may combine multiple capabilities.

---

# Cost vs capability

A useful exam principle:

```text
                 Higher capability
                       ↑
                       │
                ┌─────────────┐
                │     LLM     │
                └─────────────┘
                       │
             Multimodal when
             multiple modalities
                       │
                ┌─────────────┐
                │     SLM     │
                └─────────────┘
                       │
                Simple tasks
                       ↓
                 Lower cost
```

But **multimodal isn't simply "between" LLM and SLM**. Multimodal describes the **types of information the model can process**, while LLM/SLM describes model scale/capability.

That's an important conceptual distinction.

---

# The AI-103 decision framework

When you get a model-selection question, ask these five questions:

### **1. How complex is the task?**

Complex reasoning → **LLM**

Simple task → **SLM**

### **2. What type of input is provided?**

Text only → language model

Image/audio/video involved → **multimodal capability**

### **3. Is it a specialized AI task?**

Yes → consider **Foundry Tool**

### **4. What are the performance requirements?**

High volume + low latency + cost-sensitive → **SLM/smaller model**

### **5. Does the agent need reasoning and tool use?**

Yes → **capable LLM**

---

# Memory trick

## **"BIG – SMALL – MANY – SPECIAL"**

**BIG problem → LLM**
Complex reasoning, planning, agents

**SMALL problem → SLM**
Classification, routing, simple extraction

**MANY modalities → Multimodal**
Text + image + audio + video

**SPECIAL task → Foundry Tool**
Speech, documents, safety, vision, etc.

### One-line exam rule

> **Use the smallest model or specialized AI capability that reliably meets the task's reasoning, modality, latency, scale, and accuracy requirements.**
