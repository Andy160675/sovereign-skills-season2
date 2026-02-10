---
name: skill-consolidation-deployer
description: Consolidate skills into categorized seasons, build an interactive web portal, deploy to Git (public/private), execute governance close-out with SITREP/SWOT/hashes, and sync to Google Drive. Use when cataloging skills, deploying skill repos, building skill dashboards, creating season-based Git deployments, or performing full close-out with evidence trails.
---

# Skill Consolidation Deployer

Consolidate, categorize, deploy, and close out skill collections through a deterministic 8-step pipeline.

## Workflow Overview

1. **Catalog** — Read all skill definitions from `/home/ubuntu/skills/*/SKILL.md`
2. **Categorize** — Assign each skill to a lifecycle category and deployment season
3. **Map** — Generate a consolidation map document (`skill-consolidation-map.md`)
4. **Build Portal** — Create an interactive web dashboard displaying all skills by season/category
5. **Deploy to Git** — Create GitHub repos per season (public or private) and push
6. **Close-Out** — Generate SITREP with SWOT, hash all artifacts, create evidence trail
7. **Sync** — Upload close-out artifacts to Google Drive
8. **Seal** — Apply constitutional seal, assign responsible person, freeze state

## Step 1: Catalog Skills

Read every `SKILL.md` in `/home/ubuntu/skills/`. Extract for each skill:

| Field | Source |
|-------|--------|
| `name` | YAML frontmatter `name` |
| `description` | YAML frontmatter `description` |
| `involvesGit` | Scan body for Git/GitHub references |
| `involvesIDE` | Scan body for IDE/editor references |
| `keyTechnologies` | Extract from body (tools, APIs, languages) |

Use parallel subtasks (`map` tool) for 5+ skills to read simultaneously.

## Step 2: Categorize into Lifecycle Groups

Assign each skill to exactly one lifecycle category:

| Category | Criteria |
|----------|----------|
| Intelligence & Research | Data gathering, OSINT, analytics, market research |
| Strategic Planning | Doctrine, strategy, operational planning |
| Development & Build | Code generation, app building, skill creation |
| Deployment & CI/CD | Git ops, pipeline diagnosis, consolidation |
| Governance & Compliance | Audit portals, evidence systems, constitutional governance |
| Valuation & Analysis | Financial modeling, enterprise valuation |
| Presentation & Reporting | Slides, reports, documentation workflows |
| Community & Outreach | Campaigns, networking, multi-platform outreach |
| Close-out & Archival | Governance close-out, sealing, hash archival |
| Audit & Provenance | Backward audits, provenance tracing, evidence chains |

Add new categories only if no existing category fits.

## Step 3: Assign to Seasons

Seasons group skills by deployment tier and visibility:

| Season | Visibility | Purpose |
|--------|-----------|---------|
| Season I | Public | Foundation — core intelligence and planning skills |
| Season II | Public | Build & Deploy — development, CI/CD, presentation |
| Season III | Private | Elite Operations — governance, valuation, close-out |
| Season IV+ | User-defined | Extension seasons as needed |

**Rules:**
- Public seasons: open-source, community-accessible
- Private seasons: sensitive operations, proprietary workflows
- Each season gets its own GitHub repo: `sovereign-skills-season{N}`

Generate `skill-consolidation-map.md` with tables per category and season assignments. See `references/consolidation_map_example.md` for format.

## Step 4: Build Portal

Build an interactive web dashboard using `webdev_init_project` (React + Tailwind + shadcn/ui).

**Required sections:**
- Hero banner with project summary stats
- Season selector (filter by season)
- Season cards with badges and progress rings
- Skill grid grouped by lifecycle category
- Pipeline visualization (Git → Build → Deploy → Seal)
- SWOT analysis display (from close-out SITREP)
- Close-out tracker checklist
- Stats bar (total skills, Git-integrated, IDE-linked, sealed)
- Search/filter by skill name, category, or technology

**Design:** Dark theme, industrial/SCADA aesthetic. Use `generate_image` for hero banner and season badges (one per season).

**Data model** — create `client/src/data/skills.ts`:
```typescript
type Season = 1 | 2 | 3 | 4;
interface Skill { id, name, displayName, summary, category, season, involvesGit, involvesIDE, keyTechnologies, status }
interface SeasonConfig { id, name, subtitle, visibility, repoName, color, badgeUrl, skills[] }
```

## Step 5: Deploy to Git

For each season, create a GitHub repo and push:

```bash
# Public season
gh repo create sovereign-skills-season{N} --public --source=. --push --description "..."

# Private season
gh repo create sovereign-skills-season{N} --private --source=. --push --description "..."
```

**Repo structure per season:**
```
sovereign-skills-season{N}/
├── README.md
├── skills/
│   ├── skill-a/
│   └── skill-b/
└── docs/
```

Tag each repo: `git tag -a v1.0.0 -m "Season {N} initial deployment"` and push tags.

**README template:** See `templates/season_readme_template.md`.

## Step 6: Close-Out

Generate governance close-out artifacts using templates from `templates/` directory.

**Required artifacts:**

1. **CLOSE_OUT_PROTOCOL_DESIGN.md** — Use `templates/close_out_template.md`. Fill: deliverables, preconditions, state freeze, verification, repo URLs, hash manifest, constitutional seal.

2. **SITREP.md** — Use `templates/sitrep_template.md`. Fill: executive summary, SWOT, artifact inventory, deployment ledger, final assessment.

**SWOT rules:**
- All weaknesses/threats mitigated to ALARP
- Focus narrative on strengths and opportunities
- Mark each weakness/threat with mitigation note

3. **Hash manifest** — Run: `python3 scripts/generate_hashes.py <directory>`

4. **Flow diagram** — Create Mermaid `.mmd` file and render: `manus-render-diagram flow.mmd flow.png`

## Step 7: Sync to Google Drive

```bash
rclone copy skills-closeout/ manus_google_drive:"Sovereign-Skills-Closeout/" --config /home/ubuntu/.gdrive-rclone.ini
rclone link manus_google_drive:"Sovereign-Skills-Closeout/SITREP.md" --config /home/ubuntu/.gdrive-rclone.ini
```

## Step 8: Seal

- Assign responsible person (user by default)
- Version tag: `v{X}.{Y}.{Z}-SEALED`
- Update portal close-out tracker — all items complete
- Update portal version in header and footer
- Save final `webdev_save_checkpoint`

> No further modification permitted without a new, formally authorized mandate.

## Adding Skills to Existing Deployment

1. Read new skill definitions
2. Assign category and season (existing or new)
3. Update `client/src/data/skills.ts` — add skill objects and season config
4. If new season: generate badge with `generate_image`, create GitHub repo
5. If existing season: update existing repo with new skill files
6. Update portal stats, close-out tracker, version
7. Bump version to `v{X}.{Y+1}.{Z}`
8. Save checkpoint
