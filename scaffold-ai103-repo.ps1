#Requires -Version 5.1
# Scaffolds topics/, frameworks/, mock-tests/ for microsoft-ai-103-study-guide
# Run from the root of the repo in PowerShell:
#   .\scaffold-ai103-repo.ps1
# If PowerShell blocks script execution, run once (in an elevated prompt):
#   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

function New-TopicStub {
    param(
        [string]$Path,
        [string]$Title,
        [string]$Skill
    )
    $dir = Split-Path -Path $Path -Parent
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
    if (Test-Path $Path) {
        Write-Host "skip (exists): $Path"
        return
    }
    $slug = [System.IO.Path]::GetFileNameWithoutExtension($Path)
    $content = @"
# $Title

**Exam skill:** $Skill

## Core concept
_TODO_

## Memory trick
_TODO_

## Related
- Framework: ../../frameworks/$slug-decision-framework.md
- Practice: ../../mock-tests/$slug-quiz.md

## Referenced by
_none yet_
"@
    Set-Content -Path $Path -Value $content -Encoding UTF8
    Write-Host "created: $Path"
}

# ---------- Domain 1: Plan and Manage an Azure AI Solution (25-30%) ----------
$D1 = "topics/domain-1-plan-manage"
New-TopicStub "$D1/infra-design.md" "Design Azure infrastructure for AI apps and agents" `
    "Design Azure infrastructure for AI applications and agent-based solutions."
New-TopicStub "$D1/foundry-deployments.md" "Configure model, tool, and agent deployments" `
    "Configure model, tool, and agent deployments in Microsoft Foundry."
New-TopicStub "$D1/rbac-guardrails.md" "Security, guardrails, and RBAC" `
    "Implement security, guardrails, and role-based access controls (RBAC)."
New-TopicStub "$D1/cicd-integration.md" "Foundry + CI/CD integration" `
    "Integrate Foundry projects with CI/CD automation pipelines."

# ---------- Domain 2: Implement Generative AI and Agentic Solutions (30-35%) ----------
$D2 = "topics/domain-2-generative-agentic"
New-TopicStub "$D2/model-selection.md" "Model Selection" `
    "Choose an appropriate model for each task, including LLMs, small language models, multimodal models, and Foundry Tools."
New-TopicStub "$D2/memory-tool-schemas.md" "Memory, tool schemas, and knowledge integration" `
    "Choose appropriate memory, tool schemas, and knowledge integration."
New-TopicStub "$D2/agent-oversight.md" "Agent oversight and tool-access constraints" `
    "Govern agent behavior using oversight modes and tool-access constraints."
New-TopicStub "$D2/human-in-the-loop.md" "Autonomous / semi-autonomous workflows with HITL" `
    "Build autonomous or semi-autonomous workflows with human-in-the-loop approval."
New-TopicStub "$D2/prompt-engineering-cot.md" "Prompt engineering, reflection, chain-of-thought eval" `
    "Implement advanced prompt engineering, model reflection, and chain-of-thought evaluation loops."

# ---------- Domain 3: Implement Computer Vision Solutions (10-15%) ----------
$D3 = "topics/domain-3-computer-vision"
New-TopicStub "$D3/image-video-generation.md" "Image/video generation from prompts or reference media" `
    "Build solutions that generate images and videos via text prompts or reference media."
New-TopicStub "$D3/image-editing-inpainting.md" "Image-editing workflows (inpainting, mask-based)" `
    "Configure image-editing workflows (inpainting, mask-based edits)."
New-TopicStub "$D3/video-segment-processing.md" "Processing and interpreting video segments" `
    "Process and interpret video segments for downstream workflows."
New-TopicStub "$D3/multimodal-grounding.md" "Visual context analytics / grounded QA" `
    "Configure visual context analytics using multimodal models (grounded question-answering)."

# ---------- Domain 4: Implement Text Analysis and Information Extraction (20-30%) ----------
$D4 = "topics/domain-4-text-analysis"
New-TopicStub "$D4/speech-text.md" "Speech-to-text / text-to-speech for agents" `
    "Convert speech-to-text / text-to-speech for interactive agents."
New-TopicStub "$D4/llm-rag-pipelines.md" "LLM-first text analysis and RAG pipelines" `
    "Build Large Language Model-first text analysis and information extraction pipelines (RAG)."
New-TopicStub "$D4/observability-tracing.md" "Observability: tracing, token analytics, latency" `
    "Set up observability using tracing, token analytics, and latency breakdowns."

New-Item -ItemType Directory -Path "frameworks" -Force | Out-Null
New-Item -ItemType Directory -Path "mock-tests" -Force | Out-Null

if (-not (Test-Path "mnemonics.md")) {
    $mnemonics = @"
# Mnemonics Cheat Sheet
One line per trick. Link to the full topic file for context.

- **Model selection** — "Big brain, small task, many senses, ready tool" -> topics/domain-2-generative-agentic/model-selection.md
"@
    Set-Content -Path "mnemonics.md" -Value $mnemonics -Encoding UTF8
    Write-Host "created: mnemonics.md"
}

Write-Host ""
Write-Host "Done. 16 topic stubs created under topics/, plus frameworks/, mock-tests/, mnemonics.md"