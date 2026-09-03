# Microsoft AI-103 Study Guide: Azure AI Apps and Agents Developer

Open-source study repository for **Exam AI-103: Developing AI Apps and Agents on Azure**. It includes scenario-based practice questions, domain breakdowns aligned to the official Skills Measured outline, Python SDK implementations, and hands-on agentic workflows.

> Aligned to the official Skills Measured outline (updated April 16, 2026). Verify against the [official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103) before relying on any domain weight or topic below — Microsoft revises beta exams frequently.

---

## 🧭 Exam at a Glance

| Item | Detail |
|---|---|
| Exam | AI-103: Developing AI Apps and Agents on Azure |
| Certification | Azure AI Apps and Agents Developer Associate |
| Duration | 120 minutes |
| Questions | ~50 scored (MCQ, multi-select, code completion, case studies, yes/no scenario sets) |
| Passing score | 700 / 1000 (scaled) |
| Primary platform | Microsoft Foundry (projects, model deployments, agents, Foundry Tools) |

---

## 📊 Exam Blueprint & Progress Tracker

### Domain 1: Plan and Manage an Azure AI Solution (25–30%)
- [ ] Choose the appropriate Foundry services for generative AI and agents
  - [ ] Select models per task: LLMs, small language models, multimodal models, Foundry Tools
  - [ ] Select services for generation, grounding, vector search, agent workflows, multimodal processing
  - [ ] Choose retrieval and indexing methods
  - [ ] Choose memory, tool, and knowledge integration services for agents
- [ ] Set up AI solutions in Foundry
  - [ ] Design Azure infrastructure for AI apps and agent-based solutions
  - [ ] Choose deployment options; configure model and agent deployments
  - [ ] Integrate Foundry projects with CI/CD pipelines
- [ ] Manage, monitor, and secure AI systems
  - [ ] Manage quotas, scaling, rate limits, and cost
  - [ ] Monitor model performance, drift, safety events, grounding quality
  - [ ] Monitor ingestion quality, search index health, relevance
  - [ ] Configure security: managed identity, private networking, keyless credentials, role policies
- [ ] Implement responsible AI across generative and agentic systems
  - [ ] Safety filters, guardrails, risk detection, content moderation
  - [ ] Evaluators, safety evaluations, explanation tooling
  - [ ] Auditing via tracing (OpenTelemetry-based), provenance metadata, approval workflows
  - [ ] Govern agent behavior: oversight modes, constraints, tool-access controls

### Domain 2: Implement Generative AI and Agentic Solutions (30–35%)
- [ ] Build generative applications by using Foundry
  - [ ] Deploy and consume LLMs, small models, code models, multimodal models
  - [ ] Implement RAG in an application
  - [ ] Design workflows, tool-augmented flows, multistep reasoning pipelines
  - [ ] Evaluate models and apps: fabrications, relevance, quality, safety
  - [ ] Integrate via Foundry SDKs and connectors; connect an app to a Foundry project
- [ ] Build agents by using Foundry
  - [ ] Define agent roles, goals, conversation tracking, tool schemas
  - [ ] Integrate retrieval, function calling, conversation memory
  - [ ] Integrate tools: APIs, knowledge stores, search, Content Understanding, custom functions
  - [ ] Implement orchestrated multi-agent solutions (Connected Agents, Multi-Agent Workflows)
  - [ ] Build autonomous / semi-autonomous workflows with safeguards and approval controls
  - [ ] Monitor deployed agents, evaluate behavior, perform error analysis
- [ ] Optimize and operationalize generative AI systems
  - [ ] Prompt engineering and model parameter tuning
  - [ ] Model reflection, chain-of-thought evaluations, self-critique loops
  - [ ] Observability: tracing, token analytics, safety signals, latency breakdowns
  - [ ] Orchestrate multiple models, flows, or hybrid LLM + rules engines

### Domain 3: Implement Computer Vision Solutions (10–15%)
- [ ] Image and video generation
  - [ ] Generate images and videos from text prompts and reference media
  - [ ] Image editing: inpainting, mask-based edits, prompt-driven modifications
  - [ ] Edit generated videos; apply platform generation/editing controls
- [ ] Multimodal understanding workflows
  - [ ] Analyze visual context with multimodal models
  - [ ] Concise/detailed captions for single or multiple images
  - [ ] Visual question answering grounded in image evidence
  - [ ] Alt-text and extended descriptions aligned to accessibility guidelines
  - [ ] Azure Content Understanding for visual characteristics and video segment analysis
  - [ ] Single-task vs. pro-mode Content Understanding pipelines
  - [ ] Identify objects, components, or regions in images/video
- [ ] Responsible AI for multimodal content
  - [ ] Classify unsafe or disallowed visual content
  - [ ] Detect indirect prompt injection via embedded text in images
  - [ ] Enforce visual policy: watermarks, prohibited symbols, brand usage, inappropriate content

### Domain 4: Implement Text Analysis Solutions (10–15%)
- [ ] Language model text analysis
  - [ ] Extract entities, topics, summaries, structured JSON via generative prompting and Foundry Tools
  - [ ] Detect sentiment, tone, safety issues, sensitive content
  - [ ] Translate text with Azure Translator or LLM-powered flows
  - [ ] Customize outputs for domain tasks (compliance summarization, domain extraction)
- [ ] Speech solutions
  - [ ] Speech-to-text and text-to-speech for agentic interactions
  - [ ] Speech as an agent modality, including custom speech models
  - [ ] Multimodal reasoning from audio inputs
  - [ ] Speech translation via language models and Foundry Tools

### Domain 5: Implement Information Extraction Solutions (10–15%)
- [ ] Retrieval and grounding pipelines
  - [ ] Ingest and index documents, images, audio, video
  - [ ] Configure semantic, hybrid, and vector search for grounding
  - [ ] Enrichment via custom or built-in skills (text, images, layout)
  - [ ] RAG ingestion flow, including OCR
  - [ ] Connect retrieval pipelines to workflows and agent tools
- [ ] Extract content from documents
  - [ ] Multimodal pipelines combining OCR, layout analysis, field extraction
  - [ ] Clean, grounded representations for agents and RAG via Content Understanding
  - [ ] Content Understanding analyzers producing structured or markdown output

---

## 🗂️ Practice Materials in This Repo

| File | Description |
|---|---|
| `AI-103_Knowledge_Check_50.html` | 50-question knowledge check with domain filtering and immediate feedback |
| `AI-103_Mock_Exam_60.html` | 60-question timed mock (90 min, feedback on submission only) |
| `AI-103_Practice_Hard_250.html` | 250-question hard-mode bank with confusable near-miss distractors |
| `AI-103_Gap_Topics_Study_Guide.docx` | Nine-section guide covering gaps in the official learning path |
| `AI-103_Exam_Booklet.docx` | Consolidated exam reference booklet |
| `AI103_Exam_Prep_Tracker.xlsx` | Study tracker by domain and topic |

All HTML tools are self-contained (no build step, no dependencies) — open directly in a browser. Question banks are weighted to mirror the official domain distribution.

---

## ⚠️ Known Exam Gotchas
- **Content Understanding pro mode** is preview-only and document-only — not GA.
- **Prompt Shields**: know the *annotate* vs. *block* distinction.
- **Image editing**: inpainting is signaled by mask/region language, not plain generation; `gpt-image-1` returns base64, not a URL.
- **Terminology**: "Manager-Worker orchestration" and "Trace Logging" are not Microsoft terms. Use *Connected Agents*, *Multi-Agent Workflows*, and *OpenTelemetry-based tracing*. Treat non-official aggregated sources with caution.
- **Document Intelligence vs. Content Understanding**: know which service the scenario is actually describing.

---

## 🏗️ Reference Architectures

### Azure AI Foundry
[![Azure AI Foundry](images/foundry/foundry-architecture.png)](https://azure.microsoft.com/en-us/products/ai-foundry)

### Azure AI Search Pipeline
[![Azure AI Search](images/ai-search/azure-ai-search-pipeline.png)](https://azure.microsoft.com/en-us/products/ai-services/ai-search)

### RAG
[![RAG](images/rag/rag-overview.png)](https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation)

---

## 📚 Key Study Resources
- [Official AI-103 Certification Page](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-apps-and-agents-developer-associate/)
- [Official AI-103 Study Guide (Skills Measured)](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103)
- [Microsoft Practice Assessments](https://learn.microsoft.com/en-us/credentials/certifications/practice-assessments-for-microsoft-certifications)
- [Official Exam Sandbox](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-apps-and-agents-developer-associate/#exam-prepare-options)
- [AI-103T00 Learning Path](https://learn.microsoft.com/en-us/training/) (covers roughly 75% of exam content; see the gap guide for the rest)

---

## ⚖️ Disclaimer & Legal Notice

### 1. No Affiliation with Microsoft
This repository is an independent study project developed for educational and portfolio demonstration purposes. It is **not** affiliated with, endorsed by, sponsored by, or associated with Microsoft Corporation. "Microsoft", "Azure", and "AI-103" are trademarks of the Microsoft group of companies.

### 2. Educational Use Only
This repository aligns with the topics covered in the official [Study guide for Exam AI-103](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103). Use of this material does not guarantee a passing score on any official certification assessment.

### 3. Limitation of Liability
This software is provided "as-is" under the MIT License. In no event shall the authors or copyright holders be liable for any claims, damages, or liabilities arising from the use of this material, including but not limited to local execution errors, downstream cloud configuration issues, or modifications made by third parties.
