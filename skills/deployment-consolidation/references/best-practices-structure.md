# Best Practices: Repository Directory Structure

## Standard Sovereign Elite Structure

```
repository-root/
├── core/                    # Core system components
│   ├── [component-name]/    # Individual core components
│   └── ...
├── infrastructure/          # Infrastructure and deployment
│   ├── modules/             # Infrastructure modules
│   ├── orchestration/       # Orchestration automation
│   └── config/              # Configuration management
├── releases/                # Version-controlled releases
│   ├── v[X.Y]/              # Versioned releases
│   ├── bundles/             # Git bundles
│   └── archives/            # Historical archives
├── docs/                    # Documentation and doctrine
│   ├── architecture/        # System architecture
│   ├── doctrine/            # Operational doctrine
│   ├── operational/         # Operational procedures
│   ├── reports/             # Reports and analytics
│   └── presentations/       # Presentation materials
├── scripts/                 # Deployment and automation
│   ├── deployment/          # Deployment scripts
│   ├── orchestration/       # Orchestration automation
│   └── verification/        # Verification and attestation
├── evidence/                # Compliance and audit trail
│   ├── snapshots/           # Evidence snapshots
│   ├── attestations/        # Cryptographic attestations
│   └── audit-logs/          # Audit trail records
├── catalogs/                # State and catalog management
│   ├── ai-threads/          # AI thread catalogs
│   └── state/               # State management
└── build/                   # Build and CI/CD
    ├── ci-cd/               # CI/CD pipeline configs
    ├── docker/              # Container definitions
    └── manifests/           # Deployment manifests
```

## File Type Categorization

| File Type | Target Directory | Notes |
|-----------|------------------|-------|
| Python scripts (`.py`) | `infrastructure/orchestration/` or `scripts/` | Orchestration in infrastructure, deployment in scripts |
| Shell scripts (`.sh`) | `scripts/deployment/` | All deployment and automation scripts |
| Documentation (`.md`) | `docs/[category]/` | Categorize by type (architecture, operational, etc.) |
| Configuration (`.json`, `.yml`, `.yaml`) | `infrastructure/config/` or `build/ci-cd/` | Config in infrastructure, CI/CD in build |
| Git bundles (`.bundle`) | `releases/bundles/` | Version-controlled release bundles |
| Archives (`.tar.gz`, `.zip`) | `releases/archives/` | Compressed historical releases |
| Evidence manifests (`.json`) | `evidence/snapshots/` | Deployment manifests and snapshots |
| Attestations (`.sha256`) | `evidence/attestations/` | Cryptographic attestations |
| Catalogs (`.json`) | `catalogs/ai-threads/` or `catalogs/state/` | AI thread catalogs and state management |
| CI/CD workflows (`.yml`) | `build/ci-cd/` | GitHub Actions and other CI/CD configs |

## Directory Purpose Guidelines

**core/** - Contains the fundamental system components that define the core functionality. Each component should be self-contained with its own documentation and release artifacts.

**infrastructure/** - Houses all infrastructure-related code, including orchestration scripts, modules, and configuration files. This is the operational backbone.

**releases/** - Version-controlled releases organized by version number. Includes git bundles for complete repository snapshots and archives for compressed releases.

**docs/** - Comprehensive documentation organized by category. Architecture for system design, doctrine for operational philosophy, operational for procedures, reports for analytics, and presentations for stakeholder materials.

**scripts/** - All automation and deployment scripts. Deployment scripts for production releases, orchestration for automation workflows, and verification for attestation and validation.

**evidence/** - Complete audit trail and compliance records. Snapshots for deployment manifests, attestations for cryptographic verification, and audit-logs for historical tracking.

**catalogs/** - State and catalog management. AI threads for conversation catalogs and state for system state management.

**build/** - Build and CI/CD infrastructure. CI/CD for pipeline configurations, docker for containerization, and manifests for deployment specifications.

## Consolidation Mapping Examples

| Source Location | Target Location | Reasoning |
|----------------|-----------------|-----------|
| `AI_VAULT/sovereign-governor/` | `core/sovereign-governor/` | Core system component |
| `AI_VAULT/orchestration/*.py` | `infrastructure/orchestration/` | Orchestration scripts |
| `SOVEREIGN_SYSTEM/releases/v4.5/` | `releases/v4.5/` | Version-controlled release |
| `agi-rollout-pack/docs/` | `docs/[category]/` | Documentation by category |
| `knowledge_exchange/doctrine/` | `docs/doctrine/` | Operational doctrine |
| Deployment scripts | `scripts/deployment/` | Deployment automation |
| Git bundles | `releases/bundles/` | Complete repository snapshots |
| Evidence snapshots | `evidence/snapshots/` | Deployment manifests |
