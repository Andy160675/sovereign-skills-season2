#!/usr/bin/env python3
"""
CI/CD Pipeline Failure Scanner
Scans a project directory for common CI/CD pipeline failure vectors.
Outputs a structured JSON report of findings with priority classifications.

Usage:
    python scan_pipeline_failures.py <project_dir> [--output report.json]
"""

import ast
import json
import os
import sys
import re
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Optional


@dataclass
class Finding:
    priority: str  # P0, P1, P2, P3
    category: str
    file: str
    line: Optional[int]
    description: str
    remediation: str


def scan_missing_imports(project_dir: str) -> List[Finding]:
    """Detect missing imports in Python files by parsing AST."""
    findings = []
    for py_file in Path(project_dir).rglob("*.py"):
        try:
            source = py_file.read_text()
            tree = ast.parse(source)
        except (SyntaxError, UnicodeDecodeError):
            findings.append(Finding(
                priority="P0", category="syntax_error",
                file=str(py_file), line=None,
                description=f"Syntax error in {py_file.name} — file cannot be parsed.",
                remediation="Fix syntax errors before any pipeline run."
            ))
            continue

        # Collect imported names
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imported.add(alias.asname or alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imported.add(node.module.split('.')[0])
                for alias in node.names:
                    imported.add(alias.asname or alias.name)

        # Check type hints for common missing imports
        type_hints_used = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Subscript):
                if isinstance(node.value, ast.Name):
                    type_hints_used.add(node.value.id)
            if isinstance(node, ast.Name) and node.id in ("List", "Dict", "Optional", "Any", "Tuple", "Set"):
                type_hints_used.add(node.id)

        missing = type_hints_used - imported
        for name in missing:
            findings.append(Finding(
                priority="P0", category="missing_import",
                file=str(py_file), line=None,
                description=f"Type hint '{name}' used but not imported.",
                remediation=f"Add 'from typing import {name}' to the file."
            ))
    return findings


def scan_missing_methods(project_dir: str) -> List[Finding]:
    """Detect method calls to undefined methods within classes."""
    findings = []
    for py_file in Path(project_dir).rglob("*.py"):
        try:
            source = py_file.read_text()
            tree = ast.parse(source)
        except (SyntaxError, UnicodeDecodeError):
            continue

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                defined_methods = {n.name for n in node.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
                called_methods = set()
                for child in ast.walk(node):
                    if isinstance(child, ast.Call):
                        if isinstance(child.func, ast.Attribute):
                            if isinstance(child.func.value, ast.Name) and child.func.value.id == "self":
                                called_methods.add(child.func.attr)

                missing = called_methods - defined_methods
                for method in missing:
                    findings.append(Finding(
                        priority="P0", category="missing_method",
                        file=str(py_file), line=None,
                        description=f"Class '{node.name}' calls self.{method}() but method is not defined.",
                        remediation=f"Implement '{method}' method in class '{node.name}'."
                    ))
    return findings


def scan_missing_modules(project_dir: str) -> List[Finding]:
    """Detect imports of modules that don't exist in the project."""
    findings = []
    project_modules = set()
    for py_file in Path(project_dir).rglob("*.py"):
        rel = py_file.relative_to(project_dir)
        module_name = str(rel).replace("/", ".").replace(".py", "")
        project_modules.add(module_name.split(".")[0])

    stdlib_and_common = {
        "os", "sys", "re", "json", "time", "datetime", "hashlib", "typing",
        "dataclasses", "enum", "copy", "collections", "functools", "itertools",
        "pathlib", "abc", "io", "math", "random", "string", "struct",
        "pytest", "unittest", "logging", "concurrent", "threading", "multiprocessing",
        "cryptography", "yaml", "pyyaml", "requests", "flask", "fastapi",
    }

    for py_file in Path(project_dir).rglob("*.py"):
        try:
            source = py_file.read_text()
            tree = ast.parse(source)
        except (SyntaxError, UnicodeDecodeError):
            continue

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module:
                root_module = node.module.split(".")[0]
                if root_module not in project_modules and root_module not in stdlib_and_common:
                    findings.append(Finding(
                        priority="P0", category="missing_module",
                        file=str(py_file), line=node.lineno,
                        description=f"Import from '{node.module}' — module not found in project or known packages.",
                        remediation=f"Create '{root_module}' module or add to requirements.txt, or skip the test."
                    ))
    return findings


def scan_infrastructure(project_dir: str) -> List[Finding]:
    """Check for missing CI/CD infrastructure files."""
    findings = []
    checks = [
        (".github/workflows", "P1", "No GitHub Actions workflow directory found.",
         "Create .github/workflows/main.yml with lint, test, and deploy stages."),
        ("requirements.txt", "P1", "No requirements.txt found.",
         "Create requirements.txt listing all Python dependencies."),
        ("Dockerfile", "P2", "No Dockerfile found.",
         "Create a Dockerfile for containerized, reproducible test execution."),
        ("pyproject.toml", "P2", "No pyproject.toml found.",
         "Create pyproject.toml for modern Python project configuration."),
    ]

    for path, priority, desc, fix in checks:
        full = Path(project_dir) / path
        if not full.exists():
            findings.append(Finding(
                priority=priority, category="missing_infrastructure",
                file=path, line=None, description=desc, remediation=fix
            ))

    # Check for __init__.py in directories containing .py files
    for dirpath, dirnames, filenames in os.walk(project_dir):
        py_files = [f for f in filenames if f.endswith(".py") and f != "__init__.py"]
        if py_files and "__init__.py" not in filenames:
            rel = os.path.relpath(dirpath, project_dir)
            if rel != "." and not rel.startswith("."):
                findings.append(Finding(
                    priority="P1", category="missing_init",
                    file=f"{rel}/__init__.py", line=None,
                    description=f"Directory '{rel}' has Python files but no __init__.py.",
                    remediation=f"Create an empty __init__.py in '{rel}/' for package resolution."
                ))
    return findings


def scan_thread_safety(project_dir: str) -> List[Finding]:
    """Detect potential thread safety issues in test files."""
    findings = []
    for py_file in Path(project_dir).rglob("test_*.py"):
        source = py_file.read_text()
        if "ThreadPoolExecutor" in source or "threading" in source:
            if "Lock" not in source and "lock" not in source:
                findings.append(Finding(
                    priority="P1", category="thread_safety",
                    file=str(py_file), line=None,
                    description="Concurrent test uses threads but no Lock is present for shared state.",
                    remediation="Add threading.Lock to protect shared mutable state in concurrent tests."
                ))
    return findings


def generate_report(project_dir: str, output_path: Optional[str] = None) -> dict:
    """Run all scanners and produce a consolidated report."""
    all_findings = []
    all_findings.extend(scan_missing_imports(project_dir))
    all_findings.extend(scan_missing_methods(project_dir))
    all_findings.extend(scan_missing_modules(project_dir))
    all_findings.extend(scan_infrastructure(project_dir))
    all_findings.extend(scan_thread_safety(project_dir))

    # Sort by priority
    priority_order = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
    all_findings.sort(key=lambda f: priority_order.get(f.priority, 99))

    report = {
        "project_dir": project_dir,
        "total_findings": len(all_findings),
        "by_priority": {
            "P0": len([f for f in all_findings if f.priority == "P0"]),
            "P1": len([f for f in all_findings if f.priority == "P1"]),
            "P2": len([f for f in all_findings if f.priority == "P2"]),
            "P3": len([f for f in all_findings if f.priority == "P3"]),
        },
        "findings": [asdict(f) for f in all_findings],
    }

    if output_path:
        Path(output_path).write_text(json.dumps(report, indent=2))
        print(f"Report written to {output_path}")
    else:
        print(json.dumps(report, indent=2))

    return report


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scan_pipeline_failures.py <project_dir> [--output report.json]")
        sys.exit(1)

    proj_dir = sys.argv[1]
    out = None
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            out = sys.argv[idx + 1]

    generate_report(proj_dir, out)
