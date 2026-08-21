# Speech-to-Text / Text-to-Speech for Agents

**Exam skill:** Convert **speech-to-text (STT)** and **text-to-speech (TTS)** for interactive agents.

## Core concept

Voice-enabled agents need two fundamental capabilities:

> **SPEECH → TEXT → AI AGENT → TEXT → SPEECH**

### Speech-to-Text (STT)

Converts **spoken audio into text**.

### Text-to-Speech (TTS)

Converts **generated text into spoken audio**.

The agent sits between them.

```text id="8p3k2m"
      User speaks
          ↓
   Speech-to-Text
          ↓
      Text input
          ↓
      AI Agent / LLM
          ↓
     Text response
          ↓
    Text-to-Speech
          ↓
     Voice response
```

---

# 1. Speech-to-Text (STT)

STT is used when the user **speaks to the agent**.

Example:

> User: "What's my order status?"

STT converts:

```text
Audio
  ↓
"What's my order status?"
```

The text is then passed to the agent.

### Common use cases

* Voice assistants
* Customer-service agents
* Call-center automation
* Voice search
* Meeting transcription
* Accessibility applications

### Exam clue

> **"Convert spoken user input into text so an AI application can process it."**

→ **Speech-to-Text**

---

# 2. Text-to-Speech (TTS)

TTS is used when the agent needs to **speak its response**.

Example:

```text
Agent output:
"Your order will arrive tomorrow."

        ↓ TTS

Spoken audio
```

### Common use cases

* Voice assistants
* Conversational agents
* Accessibility
* Automated customer support
* Navigation systems
* Voice notifications

### Exam clue

> **"Convert generated text into natural-sounding speech."**

→ **Text-to-Speech**

---

# 3. Interactive voice-agent architecture

A production voice agent can look like:

```text id="n4q7tz"
┌──────────────┐
│ User speaks  │
└──────┬───────┘
       ↓
┌──────────────┐
│     STT      │
└──────┬───────┘
       ↓
┌──────────────┐
│ AI Agent/LLM │
└──────┬───────┘
       ↓
┌──────────────┐
│     TTS      │
└──────┬───────┘
       ↓
┌──────────────┐
│ User hears   │
└──────────────┘
```

The agent can also call tools:

```text id="b8x2qm"
                 ┌── Search
                 │
User → STT → Agent ──→ CRM
                 │
                 └── Order API
                       ↓
                    TTS
                       ↓
                     User
```

This is a key pattern for **agentic voice applications**.

---

# 4. Speech recognition considerations

When configuring STT, consider:

### Language

What language is being spoken?

### Accuracy

Does the application need highly accurate transcription?

### Noise

Is the environment noisy?

### Speaker characteristics

Accents, speaking speed, and pronunciation can affect recognition.

### Real-time vs. batch

**Real-time:**

> User speaks → immediate transcription

**Batch:**

> Record audio → process it afterward

### Exam clue

If the scenario emphasizes **live conversation**, think:

> **Real-time speech recognition**

---

# 5. Text-to-speech considerations

TTS can be configured based on:

* Voice
* Language
* Speaking style
* Pitch
* Speed
* Output format

For conversational agents, **naturalness and latency** are important.

A voice agent that takes several seconds to respond after every sentence will feel much less interactive.

---

# 6. Real-time conversation

A good voice agent should minimize the delay between:

**User stops speaking → Agent responds**

The pipeline may therefore use streaming:

```text id="c2r5vn"
User speech
    ↓
Streaming STT
    ↓
Agent processing
    ↓
Streaming LLM response
    ↓
Streaming TTS
    ↓
User hears response
```

This can improve perceived responsiveness.

---

# 7. STT vs. TTS

This is an easy exam question.

| Requirement                 | Capability            |
| --------------------------- | --------------------- |
| Speech → text               | **STT**               |
| Text → speech               | **TTS**               |
| Voice command → agent       | **STT → Agent**       |
| Agent response → voice      | **Agent → TTS**       |
| Voice conversation          | **STT + Agent + TTS** |
| Transcribe recorded meeting | **STT**               |
| Read generated answer aloud | **TTS**               |

---

# 8. Common exam scenarios

### Scenario 1

> A customer speaks to an AI customer-service agent.

Architecture:

**STT → Agent → TTS**

---

### Scenario 2

> A company needs to convert recorded interviews into searchable text.

→ **Speech-to-Text**

The text can then be indexed and searched.

---

### Scenario 3

> An accessibility application needs to read AI-generated responses aloud.

→ **Text-to-Speech**

---

### Scenario 4

> A voice assistant needs to understand spoken commands and respond verbally.

→ **STT + LLM/Agent + TTS**

---

### Scenario 5

> A call-center application needs to analyze conversations after calls finish.

→ **Batch STT → text analysis/LLM**

The agent doesn't necessarily need real-time speech processing if analysis happens after the call.

---

# 9. Voice agent + RAG

A voice agent can also use RAG.

Example:

> User: "What is the return policy for this product?"

```text id="k7m4qx"
Speech
  ↓
STT
  ↓
User question
  ↓
Azure AI Search / RAG
  ↓
LLM
  ↓
Answer
  ↓
TTS
  ↓
Spoken response
```

This combines several AI-103 skills:

**Speech + RAG + LLM + TTS**

---

# Exam decision framework

Ask:

### **1. Is the input audio containing speech?**

→ **STT**

### **2. Does the application need to respond with a voice?**

→ **TTS**

### **3. Is it an interactive conversation?**

→ **STT + Agent + TTS**

### **4. Does the response need external knowledge?**

→ Add **RAG**

### **5. Does the user expect immediate interaction?**

→ Consider **streaming/real-time processing and latency**

---

# Memory trick

## **"EAR → BRAIN → MOUTH"**

**EAR** 👂
→ **Speech-to-Text**

**BRAIN** 🧠
→ **LLM / Agent / Tools / RAG**

**MOUTH** 🗣️
→ **Text-to-Speech**

So remember:

> **Hear → Understand → Speak**

### One-line exam rule

> **Use STT to convert user speech into text for agent processing, and TTS to convert the agent's text response back into speech; combine both for interactive voice agents.**
