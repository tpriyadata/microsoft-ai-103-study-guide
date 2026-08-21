# Observability: Tracing, Token Analytics, and Latency

**Exam skill:** Set up observability using **tracing, token analytics, and latency breakdowns**.

## Core concept

**Observability** means being able to understand **what your AI application is doing internally**, how well it is performing, how much it costs, and where problems occur.

For AI-103, think:

> **TRACE → TOKENS → LATENCY → DIAGNOSE → IMPROVE**

A production AI application should let you answer:

* What happened?
* Which component caused the problem?
* How many tokens were used?
* How long did each step take?
* Where is the bottleneck?
* Which model/tool call is expensive?
* Did retrieval or generation fail?

---

# 1. Tracing

**Tracing** follows a request through the different components of an AI application.

Example:

```text id="q4m7xs"
User request
     ↓
Agent
     ↓
Azure AI Search
     ↓
LLM
     ↓
Tool/API
     ↓
Final response
```

A trace allows you to see the entire execution path.

### Example

A user asks:

> "Find the status of my order."

The trace might show:

```text id="k3v8na"
Request
  ├── Agent planning       120 ms
  ├── Search                80 ms
  ├── Tool/API call        450 ms
  ├── LLM generation       900 ms
  └── Response              20 ms
```

Now you can immediately see that the **LLM generation** and **API call** are the major contributors to latency.

---

# 2. Spans

A trace is often divided into smaller operations called **spans**.

Think:

> **Trace = entire request**
> **Span = individual operation**

Example:

```text id="7k2pqm"
TRACE: Customer question
│
├── Span: Agent planning
├── Span: Search
├── Span: Retrieve documents
├── Span: LLM call
└── Span: Tool execution
```

This is especially valuable for **agentic applications**, where one user request may trigger many model and tool calls.

---

# 3. Token analytics

LLMs consume **tokens**.

Observability should track token usage because tokens affect:

* Cost
* Latency
* Model capacity
* Throughput
* Context-window usage

You may track:

* Input/prompt tokens
* Output/completion tokens
* Total tokens
* Tokens per request
* Tokens per user/session
* Token usage by model

### Example

```text id="m6n9qp"
Request:
Input tokens:      2,000
Output tokens:       500
Total:             2,500
```

If your application suddenly starts using:

**20,000 tokens/request**

you have a potential cost and performance problem.

---

# 4. Why token analytics matters

Suppose your application is slow.

You could discover:

```text id="v5r8cw"
Normal request:
1,500 tokens → 1.2 sec

Problem request:
15,000 tokens → 7.5 sec
```

The problem may not be the infrastructure.

It could be:

> **An unnecessarily large prompt/context.**

This is why token metrics are an important part of AI observability.

---

# 5. Latency

**Latency** measures how long an operation takes.

For an AI application:

```text id="t2q6yk"
Total latency
     ↓
┌───────────────────────────┐
│ Retrieval      200 ms     │
│ Prompt prep    100 ms     │
│ LLM call     1,200 ms     │
│ Tool call      400 ms     │
│ Post-process   100 ms     │
└───────────────────────────┘
Total          2,000 ms
```

This is a **latency breakdown**.

Instead of only knowing:

> "The application takes 2 seconds."

you know **why** it takes 2 seconds.

---

# 6. Time to first token vs. total response time

For streaming LLM applications, two useful latency measurements are:

### Time to First Token — TTFT

How long until the model begins producing output.

Useful for measuring **perceived responsiveness**.

### Total latency

How long until the complete response is generated.

Useful for measuring **overall completion time**.

Example:

```text id="z8x4qb"
Request
  ↓
800 ms
  ↓
First token appears
  ↓
1,700 ms more
  ↓
Complete response
```

**TTFT = 800 ms**

**Total latency = 2,500 ms**

---

# 7. Observability for RAG

RAG applications have additional components to trace.

Example:

```text id="p3m8vx"
User question
      ↓
Query transformation
      ↓
Azure AI Search
      ↓
Retrieved chunks
      ↓
Prompt construction
      ↓
LLM
      ↓
Answer
```

Tracing helps identify problems such as:

### Poor retrieval

The search returned irrelevant documents.

### Excessive context

Too many chunks were inserted into the prompt.

### Slow retrieval

The search operation is taking too long.

### Slow generation

The LLM takes too long to produce the response.

Without tracing, these problems can be difficult to distinguish.

---

# 8. Observability for agents

Agentic applications are even more important to trace because an agent may perform:

```text id="c5n7mw"
User
 ↓
Agent
 ├── LLM call
 ├── Search
 ├── Tool A
 ├── LLM call
 ├── Tool B
 └── LLM call
 ↓
Response
```

A trace can reveal:

* Which tool was called
* How many times it was called
* Which model calls occurred
* Tool execution time
* Token usage
* Errors
* Agent decisions/steps
* Overall latency

### Exam clue

If the question involves:

> **"Understand the sequence of agent operations."**

Think:

### **Tracing**

---

# 9. Errors + observability

Don't only monitor successful requests.

Capture:

* Exceptions
* Failed model calls
* Tool failures
* Authentication errors
* Timeouts
* Rate-limit errors
* Invalid outputs
* Retrieval failures

This lets you correlate:

**Error → trace → component → root cause**

---

# 10. What should you monitor?

For AI-103, remember these categories:

| Category     | What to measure                   |
| ------------ | --------------------------------- |
| **Requests** | Count, success/failure            |
| **Tracing**  | End-to-end execution path         |
| **Tokens**   | Input/output/total tokens         |
| **Latency**  | Total and component-level latency |
| **Models**   | Model calls and performance       |
| **Tools**    | Calls, failures, execution time   |
| **RAG**      | Retrieval quality and timing      |
| **Errors**   | Exceptions, timeouts, failures    |
| **Cost**     | Token/resource consumption        |

---

# Common exam scenarios

### Scenario 1

> You need to determine which component of an agent workflow caused a slow response.

→ **Distributed tracing / spans**

---

### Scenario 2

> Your application's Azure OpenAI costs unexpectedly increased.

First investigate:

→ **Token usage analytics**

Look for increases in prompt/output tokens or request volume.

---

### Scenario 3

> Users complain that responses take too long to start.

→ Monitor **Time to First Token (TTFT)**.

---

### Scenario 4

> RAG responses are slow and you need to determine whether retrieval or generation is responsible.

→ **Trace retrieval and LLM spans separately.**

---

### Scenario 5

> An agent occasionally fails after calling an external API.

→ Use **tracing + tool-call/error telemetry** to identify the failed operation.

---

# Exam decision framework

Ask:

### **"What do I need to understand?"**

**What happened across the workflow?**

→ **Tracing**

**How much model input/output was processed?**

→ **Token analytics**

**Why is the application slow?**

→ **Latency breakdown / spans**

**Why did the request fail?**

→ **Error telemetry + tracing**

**Why is RAG slow?**

→ Trace **retrieval + prompt construction + LLM generation**

**Why is the AI application expensive?**

→ Analyze **token usage + request volume + model usage**

---

# Memory trick

## **"TRACE – COUNT – TIME"**

**TRACE** → What happened?

**COUNT** → How many tokens did we use?

**TIME** → Where did we spend the time?

Then:

> **Trace finds the path.**
> **Tokens explain consumption/cost.**
> **Latency explains performance.**

### One-line exam rule

> **Use tracing to follow AI requests across models, retrieval, and tools; token analytics to understand model consumption and cost; and latency breakdowns to identify performance bottlenecks.**
