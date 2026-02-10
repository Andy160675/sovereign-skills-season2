# Remediation Patterns Reference

## Table of Contents

1. Code-Level Remediation (P0)
2. Infrastructure Remediation (P1-P2)
3. Pipeline Architecture Patterns
4. Trust Gate Integration
5. Report Structure

## 1. Code-Level Remediation (P0)

### Missing Method Stub Pattern

When a class calls methods that are not implemented, generate stubs:

```python
def _missing_method(self, *args, **kwargs):
    """Stub implementation — replace with production logic."""
    raise NotImplementedError("Method not yet implemented")
```

For methods that must not block testing, provide minimal functional stubs instead of `NotImplementedError`.

### Missing Import Fix Pattern

Scan for type hint usage (`List`, `Dict`, `Optional`, `Any`) and ensure corresponding `from typing import ...` exists at the top of the file.

### Missing Module Resolution

Three options, in order of preference:
1. Create a placeholder module with the expected interface
2. Mark dependent tests with `@pytest.mark.skip(reason="Module not implemented")`
3. Use `pytest.importorskip("module_name")` for conditional test execution

## 2. Infrastructure Remediation (P1-P2)

### Dependency Manifest

Always create `requirements.txt` listing all direct dependencies. Include test and lint dependencies:

```
pytest
ruff
mypy
pyyaml
```

### Package Structure

Ensure every directory containing `.py` files has an `__init__.py`. Use the scanner script to detect missing ones.

### Containerization

Use the Dockerfile template from `templates/Dockerfile`. Adapt the `CMD` line to the project's test runner.

## 3. Pipeline Architecture Patterns

### 6-Stage Sovereign Pipeline

The recommended pipeline architecture has six stages:

1. **Lint & Validate** — Code quality, YAML schema, doc link checks
2. **Unit Tests** — Per-component falsification suites, performance SLA gates
3. **Integration** — Cross-component validation, end-to-end governor chains
4. **Security** — Cryptographic verification, tamper detection, adversarial simulation
5. **Trust Gate** — Trust classification (T0/T1/T2) determines manual vs. automatic deployment
6. **Deploy** — Staging → smoke tests → production → post-deploy verification → WORM audit log

### Progressive Gating

As the project grows, expand the test suite progressively. Do not require all future tests to pass before the pipeline is operational. Gate on what exists now.

## 4. Trust Gate Integration

Map deployment trust levels to pipeline behavior:

| Trust Class | Pipeline Behavior |
|-------------|-------------------|
| **T0 (Advisory)** | Pipeline runs but deployment requires manual approval from Architect. |
| **T1 (Conditional)** | Pipeline auto-checks; deployment requires manual trigger. |
| **T2 (Pre-Approved)** | Pipeline auto-deploys within defined bounds (e.g., staging only). |
| **T3 (Auto-Executable)** | Full auto-deploy to production. Reserved for emergency defense. |

## 5. Report Structure

The final remediation report should follow this structure:

```
# CI/CD Remediation Report: [Project Name]

## Part 1: Immediate Remediation (P0)
[Table of P0 findings with file, description, remediation]

## Part 2: Pipeline Architecture
[Diagram + stage descriptions]

## Part 3: Implementation Mapping
[Table mapping project tracks/phases to pipeline stages]

## Part 4: Implementation Artifacts
[Workflow YAML, Dockerfile, dependency manifest]
```

Generate a Mermaid diagram of the pipeline architecture using `manus-render-diagram`.
