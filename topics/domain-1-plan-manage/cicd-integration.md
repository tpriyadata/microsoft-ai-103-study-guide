# Foundry + CI/CD integration

**Exam skill:** Integrate Foundry projects with CI/CD automation pipelines.

### Core concept

**Foundry + CI/CD** means automating the deployment and management of AI resources, configurations, and applications across environments such as **development → test → production**.

For Azure AI Foundry, CI/CD commonly involves:

* **Source control** — Store application code, prompts/configuration, evaluation assets, and infrastructure definitions in Git.
* **CI pipeline** — Automatically build, validate, test, and evaluate changes when code is committed.
* **CD pipeline** — Deploy validated changes to the target Azure environment.
* **Infrastructure as Code (IaC)** — Use **Bicep or ARM templates** to consistently provision Azure resources.
* **Authentication** — Use a service principal or managed identity rather than storing developer credentials in the pipeline.
* **Secrets/configuration** — Store sensitive values in **Azure Key Vault** and inject them into the pipeline/application.
* **Environment separation** — Keep development, testing, and production resources/configuration separated.
* **Evaluation gates** — For AI applications, run automated evaluations before production deployment and block deployment when quality or safety thresholds aren't met.

**Important exam distinction:** CI/CD is the **automation mechanism**. Foundry provides the AI development/project environment; your pipeline handles source control, validation, testing/evaluation, infrastructure deployment, and application deployment.

### Memory trick

**“Git → Test → Gate → Deploy”**

Think:

> **G**it → **T**est → **G**ate → **D**eploy

And for security:

> **Identity + Key Vault + IaC**

* **Identity** → Managed identity/service principal
* **Key Vault** → Secrets
* **IaC** → Repeatable Azure infrastructure

### Exam scenario pattern

If the question says:

> “Developers commit changes and the organization wants to automatically test the AI application and deploy only validated changes to production.”

Think:

**Git → CI tests/evaluation → approval/quality gate → CD deployment**

If it says:

> “Provision the same Foundry/Azure resources consistently across environments.”

Think:

**Bicep/ARM → CI/CD**

If it says:

> “The pipeline needs credentials/secrets.”

Think:

**Managed identity/service connection + Key Vault**, **not hard-coded secrets**.

If it says:

> “Prevent a model/application from reaching production when evaluation results are below the required threshold.”

Think:

**Automated evaluation as a CI/CD quality gate.**

### One-line exam memory

**Foundry develops AI; CI/CD validates and moves it safely between environments.**




