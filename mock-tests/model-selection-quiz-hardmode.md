# Mock Test — Model Selection (HARD MODE)

20 questions | Single best answer | Target: Microsoft-style scenario reasoning
Belongs to: [../topics/domain-2-generative-agentic/model-selection.md](../topics/domain-2-generative-agentic/model-selection.md)
Framework used: [../frameworks/model-selection-decision-framework.md](../frameworks/model-selection-decision-framework.md)

> **Don't look for the keyword alone.** Focus on requirement, scale, modality, latency, and task complexity — this set is intentionally designed to expose the subtle distinctions Microsoft likes to test.

---

## Q1
A retail company receives 500,000 product reviews per day. Each review must be assigned one of five predefined sentiment categories. The categories rarely change. The company requires very low latency and wants to minimize inference cost.
- A. Large language model with few-shot prompting
- B. Small language model optimized for classification
- C. Multimodal language model
- D. Large language model with retrieval-augmented generation

<details><summary>Answer</summary>B — fixed categories, high volume, low latency/cost priority = SLM.</details>

---

## Q2
A legal application receives a 150-page contract. Users can ask arbitrary questions such as "What obligations does the supplier have if delivery is delayed?" The application must provide detailed answers grounded in the contract.
- A. Small language model performing classification
- B. Large language model combined with retrieval
- C. Azure AI Language sentiment analysis
- D. Azure AI Vision Image Analysis

<details><summary>Answer</summary>B — open-ended grounded Q&A over long text = LLM + retrieval.</details>

---

## Q3
A company needs to process scanned invoices from many different vendors and layouts, extracting vendor name, invoice number, date, line items, and totals.
- A. Azure AI Language
- B. Azure AI Search
- C. Azure AI Document Intelligence
- D. Small language model

<details><summary>Answer</summary>C — structured extraction from scanned/varied-layout documents is Document Intelligence's purpose-built job.</details>

---

## Q4
A customer-service app receives either text ("Why is my device not working?") or an image (photo of a damaged device: "What's wrong with this?"). It must reason about both and generate a natural-language response.
- A. Text-only LLM
- B. SLM
- C. Multimodal model
- D. Embedding model

<details><summary>Answer</summary>C — mixed text/image input requires multimodal support.</details>

---

## Q5
A company wants to summarize millions of short internal status messages (under 100 tokens each) into a fixed format with no complex reasoning required.
- A. Large reasoning model
- B. Small language model
- C. Multimodal model
- D. Document Intelligence

<details><summary>Answer</summary>B — short input, fixed format, high volume, low complexity = SLM.</details>

---

## Q6
A RAG application must find documents semantically related to a user's question even when exact words don't match.
- A. Speech recognition
- B. Embeddings and vector search
- C. Sentiment analysis
- D. OCR

<details><summary>Answer</summary>B — semantic (meaning-based) matching is what embeddings + vector search are for.</details>

---

## Q7
A hospital wants to analyze medical images and produce a natural-language description of findings for physician review.
- A. Text-only SLM
- B. Multimodal model capable of image understanding
- C. Text embedding model
- D. Azure AI Language key phrase extraction

<details><summary>Answer</summary>B — image input plus generated natural-language description = multimodal model.</details>

---

## Q8
A company has a fixed list of 20 document categories and classifies 10 million text-only documents per month. Accuracy matters more than explanations.
- A. LLM with a large prompt
- B. Multimodal LLM
- C. SLM or specialized classification model
- D. Speech model

<details><summary>Answer</summary>C — fixed categories, huge volume, no explanation needed = SLM/classification model, not a general LLM.</details>

---

## Q9
A developer needs to convert customer phone conversations into text, which is then passed to an LLM.
- A. Azure AI Language
- B. Azure AI Speech
- C. Azure AI Search
- D. Document Intelligence

<details><summary>Answer</summary>B — audio-to-text conversion is Azure AI Speech's job, upstream of the LLM.</details>

---

## Q10
An application must translate customer messages from Japanese to English in real time, with no reasoning or explanation needed.
- A. LLM
- B. Azure AI Translator
- C. Multimodal LLM
- D. Azure AI Search

<details><summary>Answer</summary>B — pure translation with no reasoning requirement is a purpose-built Translator task, not an LLM task.</details>

---

## Q11
A company wants an AI assistant that understands a complex request, determines what information it needs, calls multiple tools, reasons over results, and generates a final response.
- A. Simple SLM classifier
- B. Large language model with tool/function-calling capabilities
- C. OCR model
- D. Sentiment analysis model

<details><summary>Answer</summary>B — multi-step planning, tool orchestration, and reasoning is core LLM agentic capability.</details>

---

## Q12
An application receives a photo of a restaurant menu and the user asks "Which dishes contain mushrooms?"
- A. Text-only LLM
- B. Multimodal model
- C. SLM classifier
- D. Text embedding model

<details><summary>Answer</summary>B — reading and reasoning over an image requires multimodal capability.</details>

---

## Q13
A company wants to detect person names, locations, organizations, and dates in millions of customer messages, with no generated responses needed.
- A. Large language model
- B. Azure AI Language named entity recognition
- C. Multimodal model
- D. Azure AI Speech

<details><summary>Answer</summary>B — named entity recognition is a purpose-built Azure AI Language capability, not a generation task.</details>

---

## Q14
A developer needs to extract text characters from photos of street signs and product labels, with no need to understand meaning.
- A. OCR
- B. LLM reasoning
- C. Sentiment analysis
- D. Embeddings

<details><summary>Answer</summary>A — pure character extraction from images is OCR, not a reasoning task.</details>

---

## Q15
A startup is building a technical support chatbot. Users describe problems many different ways; the system must reason through troubleshooting and produce customized explanations. Traffic is low and answer quality is prioritized over cost.
- A. SLM
- B. LLM
- C. Traditional classifier
- D. OCR model

<details><summary>Answer</summary>B — open-ended reasoning, variable phrasing, and quality-over-cost priority all point to LLM.</details>

---

## Q16
A financial organization processes millions of documents and needs a yes/no check for whether each contains a specific known phrase.
- A. Large language model
- B. Multimodal model
- C. Traditional text processing/search or lightweight model
- D. Large reasoning model with chain-of-thought prompting

<details><summary>Answer</summary>C — exact-phrase matching at scale doesn't need reasoning at all; a lightweight/search-based approach is most cost-efficient.</details>

---

## Q17
A developer building an image Q&A app discovers the selected text-only model cannot accept image input.
- A. Convert the image directly into an embedding and send it to the text-only model
- B. Select a multimodal model that supports image input
- C. Increase the model's context window
- D. Use a larger system prompt

<details><summary>Answer</summary>B — this is the modality-mismatch trap: no prompt or context-window trick fixes a model that can't accept the input type.</details>

---

## Q18
A company wants to search 5 million internal documents and generate answers based on retrieved content.
- A. LLM alone
- B. Azure AI Search + embeddings/vector or hybrid retrieval + LLM
- C. SLM alone
- D. Azure AI Speech + LLM

<details><summary>Answer</summary>B — large-scale grounded retrieval-augmented generation needs the full search + retrieval + LLM stack.</details>

---

## Q19
A developer needs to determine whether text violates a company's content policy, using a specialized Azure AI capability rather than a general-purpose LLM judgment call.
- A. Azure AI Content Safety
- B. Azure AI Speech
- C. Azure AI Search
- D. Azure AI Document Intelligence

<details><summary>Answer</summary>A — content moderation has a dedicated, purpose-built service: Azure AI Content Safety.</details>

---

## Q20 — EXAM TRAP
A company reads incoming customer emails and produces a structured JSON object (category, priority, customer_issue, recommended_action) from a fixed set of 8 categories and predefined actions. Millions of emails monthly; cost minimization and consistent output are priorities.
- A. Use the largest available multimodal model for every email
- B. Use an SLM or specialized classification/extraction model with structured output
- C. Use OCR followed by a multimodal model
- D. Use Azure AI Speech followed by an LLM

<details><summary>Answer</summary>B — fixed categories/actions, high volume, cost priority, consistent structured output = SLM/specialized extraction model, not a large multimodal model (the "bigger model" trap from the framework's exam-trick notes).</details>

---

## Answer key (quick scan)
1B · 2B · 3C · 4C · 5B · 6B · 7B · 8C · 9B · 10B · 11B · 12B · 13B · 14A · 15B · 16C · 17B · 18B · 19A · 20B