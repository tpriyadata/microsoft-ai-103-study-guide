# AI-103 Decision Framework — Model Selection

Belongs to: [../topics/domain-2-generative-agentic/model-selection.md](../topics/domain-2-generative-agentic/model-selection.md)

## Decision tree

Ask these questions in order — the first "yes" gives you the answer.

1. **Does the input or output include image, audio, or video?**
   → Yes: **Multimodal model**. Stop here regardless of anything else in the scenario.

2. **Does a Foundry Tool already do exactly this?** (web grounding, code execution, file/document search, computer-use automation)
   → Yes: **Use the Foundry Tool**. Don't hand-build retrieval, browsing, or code execution logic when Microsoft ships a managed version.

3. **Does the scenario name a hard constraint** — on-device, offline, sub-second latency, strict cost ceiling, or a narrow single-purpose task (e.g., sentiment tagging, PII detection)?
   → Yes: **SLM**.

4. **Otherwise** — the task needs multi-step reasoning, open-ended generation, long-context synthesis, or the scope is broad/ambiguous:
   → **LLM**.

## Quick-reference: requirement → service

The decision tree above picks the *category*. Once you know the category, this table maps common exam scenario phrasing to the specific Azure/Foundry service — this is the level of detail AI-103 actually tests at.

| Requirement                               | Best choice                          |
| ------------------------------------------ | ------------------------------------- |
| Complex reasoning / generation             | **LLM**                               |
| Simple, repetitive, high-volume text task  | **SLM**                               |
| Text + image/video/audio understanding     | **Multimodal model**                  |
| Speech → text                              | **Azure AI Speech**                   |
| Text sentiment                             | **Azure AI Language**                 |
| Entities in text                           | **Azure AI Language**                 |
| OCR / forms / tables / document structure  | **Document Intelligence**             |
| Image-specific analysis                    | **Azure AI Vision / Image Analysis**  |
| Search / retrieval                         | **Azure AI Search**                   |
| Generate embeddings                        | **Embedding model**                   |

## Most important exam trick

Microsoft's wrong-answer options almost always dangle a bigger, more "capable-sounding" model as the tempting choice. Whenever the scenario states a **cost, latency, privacy, or on-device constraint**, that constraint overrides capability — the correct answer is the *smallest* model or tool that satisfies it, not the most powerful one.

A second common trap: a scenario clearly needs image or video handling but the wrong answer offers "a more powerful LLM" as a distractor. Modality mismatch is disqualifying — no amount of LLM reasoning capability substitutes for multimodal input support.

A third trap: scenarios that sound like they need a general LLM but actually name a specific, narrower Azure service capability (sentiment, entity extraction, OCR, embeddings) — in those cases the purpose-built service beats a general model, even a capable one. Use the quick-reference table above to catch this.

## Related
- Topic: [../topics/domain-2-generative-agentic/model-selection.md](../topics/domain-2-generative-agentic/model-selection.md)
- Practice: [../mock-tests/model-selection-quiz.md](../mock-tests/model-selection-quiz.md)
## Related
- Framework: ../../frameworks/model-selection-decision-framework.md
- Practice (core): ../../mock-tests/model-selection-quiz.md
- Practice (hard mode): ../../mock-tests/model-selection-quiz-hardmode.md