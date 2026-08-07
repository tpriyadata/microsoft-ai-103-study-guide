# AI-103 Decision Framework — Azure AI Infrastructure Design

Belongs to: [../topics/domain-1-plan-manage/infra-design.md](../topics/domain-1-plan-manage/infra-design.md)

## Decision tree

1. **Does the scenario describe multiple teams/departments sharing compute, connections, or governance?**
   → Yes: **Hub-based projects** (one hub, multiple projects underneath).
   → No (single isolated team/app): **Standalone Foundry project**.

2. **Does the scenario mention data residency, "must not be publicly accessible," regulated industry compliance, or VNet requirements?**
   → Yes: **Private endpoint / VNet injection**, managed identity, keyless credentials.
   → No: Public endpoint is acceptable — pick it for simplicity/speed unless told otherwise.

3. **Is traffic described as steady/high-volume/production-critical, with cost predictability required?**
   → Yes: **Provisioned throughput** (reserved capacity).
   → No (bursty, variable, early-stage, or unpredictable): **Serverless / pay-per-token deployment**.

4. **Does the scenario mention CI/CD, automated promotion between environments, or repeatable deployments across dev/test/prod?**
   → Yes: This crosses into **Foundry + CI/CD integration** (a separate topic) — infra design should still separate environments (e.g., dev vs. prod projects/resources) to support it.

## Most important exam trick

Watch for scenarios that describe **multiple teams needing isolated budgets** — that's a trap for "hub" even though hubs are about *shared* resources. Isolated budget/quota per team, even under a shared governance umbrella, often still points to **standalone projects** with centrally managed policies, not a single hub where everyone draws from the same pool. Read whether the constraint is about **sharing infrastructure** (→ hub) or **isolating cost/quota** (→ standalone), because those two requirements can appear in the same paragraph and pull in opposite directions.

## Related
- Topic: [../topics/domain-1-plan-manage/infra-design.md](../topics/domain-1-plan-manage/infra-design.md)
- Practice: [../mock-tests/infra-design-quiz.md](../mock-tests/infra-design-quiz.md)