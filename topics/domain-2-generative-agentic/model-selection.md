# Model Selection

**Exam skill:** Choose an appropriate model for each task, including large language models (LLMs), small language models (SLMs), multimodal models, and Foundry Tools.

## Core concept

Every AI-103 scenario question about model choice is really asking: *"Given this constraint, which category of model wastes the least money/time/compute while still meeting the requirement?"* The four categories to know:

- **LLM (large language model)** — best for open-ended reasoning, complex multi-step tasks, summarization across long context, or when the task requirements are broad/unclear. Highest cost and latency of the four.
- **SLM (small language model)** — best when the task is narrow and well-defined (classification, extraction, simple Q&A), and the constraint is cost, latency, or on-device/edge deployment. Trades some reasoning depth for speed and cheapness.
- **Multimodal model** — required whenever the input or output includes more than plain text: images, audio, video, or a mix. Not a "better" model, a *different-shaped* model — pick it when the task literally can't be done with a text-only model.
- **Foundry Tool** (pre-built capability in Microsoft Foundry — e.g., Bing grounding, code interpreter, file search, computer use) — required when the task matches something Microsoft already ships as a managed tool. The exam rewards recognizing "don't build this yourself" scenarios.

The decision is rarely "which model is smartest" — it's "which is the smallest/cheapest/most appropriate option that still satisfies the stated constraint."

## Memory trick

> **"Big brain, small task, many senses, ready tool."**
> - **Big brain** = LLM → complex reasoning, ambiguous scope
> - **Small task** = SLM → narrow, cheap, fast, edge-deployable
> - **Many senses** = Multimodal → image/audio/video in the loop
> - **Ready tool** = Foundry Tool → don't reinvent something Microsoft already built

## Related
- Framework: [../../frameworks/model-selection-decision-framework.md](../../frameworks/model-selection-decision-framework.md)
- Practice: [../../mock-tests/model-selection-quiz.md](../../mock-tests/model-selection-quiz.md)
- Pratice :[../../mock-tests\model-selection-quiz-hardmode.md](../../mock-tests\model-selection-quiz-hardmode.md)

## Referenced by
- mock-tests/model-selection-quiz.md (Q1–Q10)
