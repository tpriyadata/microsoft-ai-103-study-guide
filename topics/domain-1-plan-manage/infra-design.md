# Design Azure Infrastructure for AI Apps and Agent-Based Solutions

**Exam skill:** Design Azure infrastructure for AI applications and agent-based solutions.
**Official domain:** Plan and manage an Azure AI solution (25–30%) — "Set up AI solutions in Foundry"

## Core concept

This skill is about the *shape* of your Foundry deployment before you write any application code — how projects, resources, and connections are organized, and why.

Key building blocks to know:

- **Foundry resource** — the top-level Azure resource (like an account). Holds shared settings: region, networking, managed identity.
- **Foundry project** — a workspace inside a Foundry resource. Projects can be **standalone** (isolated, single-team, own quota) or created under a **hub** (shared compute, shared connections, multiple projects/teams reusing the same infrastructure).
- **Connections** — how a project reaches external resources: Azure AI Search, storage accounts, Bing grounding, other Azure AI services. Defined once, reusable across projects under the same hub.
- **Compute/deployment shape** — serverless (pay-per-token, fastest to stand up, good for variable/bursty load) vs. provisioned throughput (reserved capacity, predictable cost and latency, good for steady high-volume production traffic).
- **Networking** — public endpoint (simplest, fastest to build) vs. private endpoint/VNet injection (required when the scenario states data must never traverse the public internet, or a "network isolation" / "no public access" requirement appears).

The exam tests whether you can read a scenario's team structure, compliance requirement, and traffic pattern, and infer the right combination of these pieces — not whether you can recite Azure networking trivia.

## Memory trick

> **"One team, one project. Many teams, one hub."**
> If the scenario describes a single isolated team/app with its own budget and no resource sharing → standalone project.
> If it describes multiple teams/departments that should share compute, connections, or governance → hub-based projects.
> Add: **"No internet, no public endpoint."** Any mention of data residency, regulatory isolation, or "must not be publicly accessible" is your private networking/VNet signal — don't need to know the port numbers, just recognize the trigger phrase.

## Related
- Framework: ../../frameworks/infra-design-decision-framework.md
- Practice (core): ../../mock-tests/infra-design-quiz.md
- Practice (hard mode): ../../mock-tests/infra-design-quiz-hardmode.md

## Referenced by
- mock-tests/infra-design-quiz.md
- mock-tests/infra-design-quiz-hardmode.md
- frameworks/infra-design-decision-framework.md