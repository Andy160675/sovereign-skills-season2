# Priority Classification Reference

## Priority Levels

| Priority | Label | Definition | SLA |
|----------|-------|------------|-----|
| **P0** | Pipeline Blocker | Causes immediate test/build failure. No pipeline run can succeed. | Fix before any other action. |
| **P1** | Test Reliability | Tests pass inconsistently, thread safety issues, missing infrastructure files. | Fix within same session. |
| **P2** | Build Maturity | Missing containerization, dependency management, or CI/CD workflow definitions. | Fix within current sprint. |
| **P3** | Integration Debt | Placeholder implementations, stub services, missing production integrations. | Schedule for next phase. |

## Common P0 Failure Patterns

**Missing method implementations:** A class calls `self.method()` but the method body is absent. Causes `AttributeError` at runtime.

**Missing imports:** Type hints like `List`, `Dict`, `Optional` used without `from typing import ...`. Causes `NameError`.

**Missing modules:** Test files import from modules that do not exist in the project. Causes `ImportError`.

**Syntax errors:** Malformed Python files that cannot be parsed. Blocks all downstream stages.

## Common P1 Failure Patterns

**Thread safety:** Concurrent tests share mutable state without locks. Causes intermittent failures.

**Missing `__init__.py`:** Python directories without `__init__.py` break package imports.

**Inconsistent test data:** Test fixtures missing required keys that the code under test expects.

## Common P2 Failure Patterns

**No CI/CD workflow:** No `.github/workflows/` directory or equivalent. Pipeline cannot run automatically.

**No Dockerfile:** No containerized test environment. Builds are not reproducible.

**No dependency manifest:** No `requirements.txt` or `pyproject.toml`. Dependencies are implicit.

## Common P3 Failure Patterns

**Placeholder cryptography:** Signing functions return fake signatures. Not production-ready.

**Stub services:** Integration points return hardcoded responses. Not validated end-to-end.

**Missing monitoring:** No health checks, no performance SLA enforcement, no alerting.
