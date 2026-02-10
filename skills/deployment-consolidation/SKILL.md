---
name: deployment-consolidation
description: Consolidate scattered code and artifacts from multiple sources (Google Drive, local directories, Git bundles) into a production-ready Git repository with full CI/CD integration, cryptographic attestations, and comprehensive documentation. Use when consolidating uncommitted work, organizing codebases, preparing deployment packages, or establishing CI/CD pipelines for scattered projects.
license: Complete terms in LICENSE.txt
---

# Deployment Consolidation

Consolidate scattered code and artifacts into a production-ready Git repository with full CI/CD integration.

## When to Use This Skill

Use this skill when you need to:

- Consolidate uncommitted work from multiple sources (Google Drive, chats, local directories)
- Organize scattered codebases by best practices
- Prepare deployment packages with cryptographic attestations
- Establish CI/CD pipelines for consolidated repositories
- Generate comprehensive documentation for deployment
- Schedule automated GitHub deployments

## Core Workflow

### Phase 1: Scan and Inventory

Scan all potential sources for code and artifacts:

1. **Google Drive directories** - Use `rclone lsf` to list directories and identify code repositories
2. **Local directories** - Use `find` to locate Python scripts, shell scripts, documentation
3. **Git bundles** - Identify `.bundle` files for repository snapshots
4. **Archives** - Locate `.tar.gz` and `.zip` files with code artifacts

Create an inventory manifest documenting:
- Source location
- File count by type (Python, shell, markdown, JSON, etc.)
- Total size
- Last modified date

### Phase 2: Consolidate and Organize

Organize files according to best practices structure. Read `/home/ubuntu/skills/deployment-consolidation/references/best-practices-structure.md` for the standard directory layout.

Create the consolidated structure:

```bash
mkdir -p consolidated-repo/{core,infrastructure,releases,docs,scripts,evidence,catalogs,build}
mkdir -p consolidated-repo/infrastructure/{modules,orchestration,config}
mkdir -p consolidated-repo/releases/{bundles,archives}
mkdir -p consolidated-repo/docs/{architecture,doctrine,operational,reports,presentations}
mkdir -p consolidated-repo/scripts/{deployment,orchestration,verification}
mkdir -p consolidated-repo/evidence/{snapshots,attestations,audit-logs}
mkdir -p consolidated-repo/catalogs/{ai-threads,state}
mkdir -p consolidated-repo/build/{ci-cd,docker,manifests}
```

Copy files to appropriate locations based on type and function:

- Core components → `core/[component-name]/`
- Orchestration scripts → `infrastructure/orchestration/`
- Deployment scripts → `scripts/deployment/`
- Documentation → `docs/[category]/`
- Git bundles → `releases/bundles/`
- Archives → `releases/archives/`

### Phase 3: Generate Deployment Scripts

Use templates to generate deployment infrastructure:

1. **Master Deployment Script** - Copy and customize `templates/master_deploy.sh.template`
   - Replace `{{PROJECT_NAME}}` with repository name
   - Replace `{{RESPONSIBLE_PERSON}}` with responsible person name
   - Replace `{{GENERATION_DATE}}` with current date
   - Make executable: `chmod +x scripts/deployment/master_deploy.sh`

2. **GitHub Actions Workflow** - Copy and customize `templates/github-actions-workflow.yml.template`
   - Replace `{{PROJECT_NAME}}` with repository name
   - Place in `build/ci-cd/github-actions-workflow.yml`

3. **README** - Copy and customize `templates/README.md.template`
   - Replace all template variables
   - Add project-specific sections as needed

### Phase 4: Initialize Git and Generate Attestations

Initialize Git repository and create cryptographic attestations:

```bash
cd consolidated-repo
git init
git branch -M main
git config user.email "email@example.com"
git config user.name "Responsible Person Name"

# Run deployment script for verification and attestation
./scripts/deployment/master_deploy.sh --confirm
```

This generates:
- Deployment manifest in `evidence/snapshots/`
- Cryptographic attestation in `evidence/attestations/`
- Initial Git commit with full audit trail

### Phase 5: Create GitHub Repository and Schedule Deployment

Create GitHub repository and optionally schedule deployment:

```bash
# Create private GitHub repository
gh repo create repo-name --private --description "Description" --source=. --remote=origin

# For scheduled deployment, create cron task
# Example: Schedule push for 12:00 UTC
# Cron expression: 0 0 12 DD MM *
```

Use the `schedule` tool to create automated deployment tasks if needed.

### Phase 6: Generate Documentation

Create comprehensive documentation:

1. **Deployment Summary** - Document the consolidation process, statistics, and outcomes
2. **IDE Integration Guide** - Instructions for cloning and setting up in IDE
3. **CI Deployment Plan** - Comprehensive CI/CD strategy document
4. **Presentation Scripts** - Speaker notes for stakeholder presentations

## Best Practices

### Measure Twice, Cut Once

- Always run `--dry-run` before `--confirm` on deployment scripts
- Verify directory structure before copying files
- Test scripts in isolation before integration
- Review generated manifests and attestations

### Cryptographic Integrity

Every deployment must generate:
- **Deployment Manifest** - JSON file with metadata and statistics
- **Cryptographic Attestation** - SHA256 hash of repository state
- **Audit Trail** - Complete record in evidence directory

### Responsible Person Protocol

Always assign and document a responsible person for each deployment:
- Include in deployment manifest
- Include in cryptographic attestation
- Include in Git commit message
- Include in README

### Zero-Dependency Mindset

Design for autonomous operation:
- All scripts should be self-contained
- No external dependencies unless absolutely necessary
- Include all required templates and references
- Document all prerequisites clearly

## Template Variables

When using templates, replace these variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `{{PROJECT_NAME}}` | Repository name | `sovereign-elite-consolidated` |
| `{{PROJECT_DESCRIPTION}}` | Brief description | `Consolidated deployment repository` |
| `{{RESPONSIBLE_PERSON}}` | Name and identifier | `Architect (Andy160675)` |
| `{{GENERATION_DATE}}` | ISO date | `2026-02-09` |
| `{{LICENSE}}` | License type | `Proprietary - Sovereign Elite System` |

## Common Patterns

### Scanning Google Drive

```bash
# List top-level directories
rclone lsd manus_google_drive: --config /home/ubuntu/.gdrive-rclone.ini

# List files in specific directory
rclone lsf manus_google_drive:DIRECTORY_NAME --config /home/ubuntu/.gdrive-rclone.ini

# Copy directory to local
rclone copy manus_google_drive:DIRECTORY_NAME /local/path --config /home/ubuntu/.gdrive-rclone.ini
```

### File Type Categorization

```bash
# Count Python scripts
find . -name "*.py" | wc -l

# Count shell scripts
find . -name "*.sh" | wc -l

# Count markdown files
find . -name "*.md" | wc -l

# Find all files of specific type
find . -name "*.json" -o -name "*.yml" -o -name "*.yaml"
```

### Git Configuration

```bash
# Set repository-specific user
git config user.email "email@example.com"
git config user.name "Name"

# Create .gitignore
cat > .gitignore <<EOF
__pycache__/
*.pyc
.vscode/
.idea/
*.log
EOF
```

## Output Deliverables

A complete deployment consolidation produces:

1. **Consolidated Repository** - Organized by best practices
2. **Deployment Scripts** - Master deploy, scheduled push, CI/CD workflows
3. **Evidence Trail** - Manifests, attestations, audit logs
4. **Documentation** - README, integration guides, deployment plans
5. **GitHub Repository** - Private repository with initial commit
6. **Scheduled Tasks** - Optional cron tasks for automated deployment

## Resources

- **Best Practices Structure**: `/home/ubuntu/skills/deployment-consolidation/references/best-practices-structure.md`
- **Master Deploy Template**: `/home/ubuntu/skills/deployment-consolidation/templates/master_deploy.sh.template`
- **GitHub Actions Template**: `/home/ubuntu/skills/deployment-consolidation/templates/github-actions-workflow.yml.template`
- **README Template**: `/home/ubuntu/skills/deployment-consolidation/templates/README.md.template`
