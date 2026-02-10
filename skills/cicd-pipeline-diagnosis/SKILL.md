---
name: cicd-pipeline-diagnosis
description: Diagnose CI/CD pipeline failures, analyze code for common failure vectors, and generate a comprehensive remediation plan and deployment strategy. Use when a user reports CI/CD issues, build failures, or needs to establish a robust, sovereign deployment pipeline from scratch.
---

# CI/CD Pipeline Diagnosis & Remediation

This skill provides a systematic workflow for diagnosing and resolving CI/CD pipeline failures, culminating in a comprehensive remediation strategy and the delivery of foundational pipeline artifacts. It is designed to transform a failing or non-existent CI/CD process into a robust, evidence-based deployment architecture.

## Core Workflow

Follow these steps to diagnose failures and build a remediation plan:

1.  **Triage & Reconnaissance:** Analyze user-provided context and run an automated scan to identify immediate failure vectors.
2.  **Synthesize Findings & Propose Architecture:** Consolidate findings, design a target CI/CD architecture, and visualize it.
3.  **Formulate Remediation Plan:** Draft a detailed, prioritized remediation plan using established patterns.
4.  **Deliver Strategy & Artifacts:** Package the final strategy document, architecture diagram, and implementation artifacts for the user.

---

### Step 1: Triage & Reconnaissance

The first step is to gather data. Analyze any code, logs, or plans provided by the user. Then, run the automated scanner to get a baseline report of common failure patterns.

```bash
# Run the scanner on the project directory
python /home/ubuntu/skills/cicd-pipeline-diagnosis/scripts/scan_pipeline_failures.py <path_to_project_dir> --output /home/ubuntu/pipeline_scan_report.json
```

Review the generated `pipeline_scan_report.json`. This report will provide a prioritized list of findings, starting with P0 pipeline blockers.

### Step 2: Synthesize Findings & Propose Architecture

Based on the scanner report and your analysis of the user's context, synthesize the root causes of the failures. Design a target CI/CD pipeline architecture that addresses these weaknesses.

Use the provided Mermaid template to create a visualization of the proposed pipeline. This diagram is a critical communication tool.

```bash
# Create a Mermaid diagram of the proposed architecture
manus-render-diagram <path_to_diagram.mmd> <path_to_output.png>
```

For a robust, 6-stage architecture pattern, consult the `remediation-patterns.md` reference file.

### Step 3: Formulate Remediation Plan

Draft a comprehensive remediation plan in a Markdown file. The plan must be clear, actionable, and prioritized.

1.  **Consult Priority Classification:** Use `/home/ubuntu/skills/cicd-pipeline-diagnosis/references/priority-classification.md` to correctly classify each finding (P0, P1, P2, P3).
2.  **Apply Remediation Patterns:** Use `/home/ubuntu/skills/cicd-pipeline-diagnosis/references/remediation-patterns.md` to find standard solutions for common failures.
3.  **Structure the Report:** Follow the report structure outlined in the `remediation-patterns.md` file to ensure clarity and completeness.

### Step 4: Deliver Strategy & Artifacts

Package all deliverables for the user. The final message should include the main strategy document, the architecture diagram, and any generated pipeline artifacts.

**Key Artifacts to Deliver:**

*   The main remediation strategy document (Markdown).
*   The rendered pipeline architecture diagram (PNG).
*   A boilerplate GitHub Actions workflow (from `templates/github-actions-workflow.yml`).
*   A boilerplate Dockerfile for containerized testing (from `templates/Dockerfile`).

---

## Bundled Resources

This skill includes the following resources to accelerate the diagnosis and remediation process:

| Path | Description |
|---|---|
| `scripts/scan_pipeline_failures.py` | An automated Python script that scans a project for common CI/CD failure vectors and generates a JSON report. |
| `templates/github-actions-workflow.yml` | A production-ready, 6-stage GitHub Actions workflow template for linting, testing, and deployment. |
| `templates/Dockerfile` | A template Dockerfile for creating a reproducible, containerized testing environment. |
| `references/priority-classification.md` | A guide defining the P0-P3 priority levels for classifying pipeline failures. |
| `references/remediation-patterns.md` | A document containing standard solutions and architectural patterns for resolving CI/CD issues. |
