# Mock Test — Azure AI Infrastructure Design

10 questions | Target: Microsoft-style scenario reasoning
Belongs to: [../topics/domain-1-plan-manage/infra-design.md](../topics/domain-1-plan-manage/infra-design.md)
Framework used: [../frameworks/infra-design-decision-framework.md](../frameworks/infra-design-decision-framework.md)

---

## Q1
A company has five departments building separate AI agents. Leadership wants all departments to share the same Azure AI Search connection and the same compute pool, with central governance.
- A. Five standalone Foundry projects
- B. One hub with five projects underneath
- C. One project shared by all five departments with no separation
- D. Five separate Foundry resources in different regions

<details><summary>Answer</summary>B — shared connections/compute across teams with central governance is the textbook hub scenario.</details>

---

## Q2
A healthcare startup building a single, isolated clinical assistant app states the solution must never be publicly reachable from the internet.
- A. Standalone project, public endpoint
- B. Standalone project, private endpoint/VNet injection
- C. Hub-based project, public endpoint by default
- D. Any project type, since networking doesn't affect reachability

<details><summary>Answer</summary>B — single isolated app = standalone project; "must never be publicly reachable" = private endpoint/VNet injection.</details>

---

## Q3
A retail company expects highly variable, bursty traffic on its new chatbot — heavy during sales events, near-zero overnight — and wants to avoid paying for unused reserved capacity.
- A. Provisioned throughput
- B. Serverless / pay-per-token deployment
- C. On-premises deployment
- D. A dedicated hub for the chatbot alone

<details><summary>Answer</summary>B — bursty/variable load with a cost-avoidance goal points to serverless, not reserved capacity.</details>

---

## Q4
A financial services company runs a production agent with steady, predictable high-volume traffic and needs guaranteed low-latency responses at a fixed monthly cost.
- A. Serverless / pay-per-token deployment
- B. Provisioned throughput (reserved capacity)
- C. Standalone project with public endpoint
- D. No deployment needed — use the free tier

<details><summary>Answer</summary>B — steady, predictable, high-volume + cost predictability is the reserved-capacity trigger.</details>

---

## Q5
A single small internal tool, built and owned by one team, needs its own dedicated quota so other teams' workloads can't affect its performance.
- A. Hub-based project sharing quota with other teams
- B. Standalone Foundry project
- C. A shared public endpoint with no isolation
- D. Multiple hubs for redundancy

<details><summary>Answer</summary>B — single team + isolated dedicated quota, even though it sounds like it could involve sharing, points to standalone.</details>

---

## Q6
A scenario states that connections to Azure AI Search and Bing grounding should be defined once and reused by multiple project teams without duplicating configuration.
- A. Each team configures its own separate connection
- B. Connections are defined at the hub level and inherited by projects underneath
- C. Connections must be hardcoded into application code
- D. Connections aren't reusable across projects

<details><summary>Answer</summary>B — reusable, centrally defined connections shared across projects is a hub-level concern.</details>

---

## Q7
A company operating in a regulated industry must ensure AI workload data never traverses the public internet and must use identity-based access instead of stored secrets.
- A. Public endpoint with API key authentication
- B. Private endpoint/VNet injection with managed identity and keyless credentials
- C. Public endpoint with managed identity only
- D. Private endpoint with hardcoded connection strings

<details><summary>Answer</summary>B — both requirements (no public internet, no stored secrets) together point to private networking plus managed identity/keyless credentials.</details>

---

## Q8
A scenario describes multiple teams that each want isolated budgets and quotas, but still want to share the same underlying compute infrastructure for cost efficiency.
- A. Fully separate Foundry resources per team, no sharing at all
- B. Hub-based projects with per-project quota controls
- C. One project with no per-team separation
- D. Standalone projects with no relationship to each other

<details><summary>Answer</summary>B — this is the "sharing infrastructure" + "isolating cost/quota" combination the framework calls out: hub-based projects support per-project quota while still sharing the underlying hub compute.</details>

---

## Q9
A startup is prototyping quickly, has no compliance requirements, and wants the fastest possible path to a working demo.
- A. Private endpoint, provisioned throughput, hub-based project
- B. Public endpoint, serverless deployment, standalone project
- C. VNet injection required by default
- D. Multi-region hub deployment

<details><summary>Answer</summary>B — no stated constraints means default to the simplest/fastest option: public endpoint, serverless, standalone.</details>

---

## Q10 — EXAM TRAP
A scenario mentions both "multiple departments will use this platform" and "each department must have a strictly isolated budget with no shared quota whatsoever."
- A. Single hub, shared quota pool across all departments
- B. Standalone projects per department, but they can still share some centrally-governed connections via policy
- C. One shared project with manual cost tracking
- D. No infrastructure planning needed since departments are separate companies

<details><summary>Answer</summary>B — "multiple departments" alone would suggest a hub, but "strictly isolated budget, no shared quota" overrides that and points to standalone projects per department — the trap is picking hub based on the team-count phrase alone without weighing the isolation requirement.</details>