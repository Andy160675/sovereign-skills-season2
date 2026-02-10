---
name: constitutional-governance-builder
description: Build constitutional AI governance platforms with multi-agent deliberation engines, hash-chained audit trails, and biophilic luxury design. Use when building boardroom-style decision systems, AI council deliberation apps, constitutional governance frameworks, multi-agent voting platforms, or sovereign governance portals. Covers schema design, 13-agent LLM deliberation engine, quorum logic, audit chains, extension marketplaces, and 8-page frontend builds.
---

# Constitutional Governance Builder

Build sovereign constitutional AI governance platforms — from brief ingestion through production delivery. Creates a 13-agent deliberation engine where AI council members vote on decisions under immutable constitutional constraints, with hash-chained audit trails and biophilic luxury design.

## Build Workflow

7 sequential phases. Complete each before advancing.

1. **Ingest brief** — Extract constitutional constraints, agent roles, pages, extensions, pricing tiers
2. **Design schema** — Define tables (users, deliberations, agent_responses, audit_chain, extensions), push migrations
3. **Build deliberation engine** — Agent definitions, LLM invocation, vote parsing, quorum logic, verdict computation, audit hashing
4. **Write tRPC routers** — Wire procedures for submit, get, history, agents, constitution, audit, extensions
5. **Implement design system** — Biophilic luxury theme (see `references/design-system.md`)
6. **Build 8 frontend pages** — Landing, Boardroom, History, Constitution, Audit Chain, Extensions, Settings, Profile
7. **Test and deliver** — Vitest tests, 0 TypeScript errors, checkpoint

## Phase 1: Ingest Brief

Parse the user's build brief. See `references/constitutional-framework.md` for the canonical framework.

Extract: 7 invariants, 6 forbidden states, failure policy, authority ladder (5 levels), 13 agent roles, quorum rules (7/13 majority), extension catalog, pricing tiers, design direction.

## Phase 2: Design Schema

Read `references/schema-architecture.md` Section 1 for complete schema definitions.

Five tables: `users` (with authorityTier enum), `deliberations` (vote tallies, verdict, hash, scores), `agent_responses` (vote, reasoning, concerns, recommendations, confidence, compliance flags, constitutional violation), `audit_chain` (hash-chained ledger), `extensions` (marketplace catalog).

After schema definition, run `pnpm db:push`.

## Phase 3: Build Deliberation Engine

Create `server/agents.ts` and `server/deliberation.ts`.

### Agent Definitions

13 agents in `server/agents.ts`. Each: id, role, name, title, icon, color, systemPrompt, isChair. Inject full constitutional context (7 invariants, 6 forbidden states, failure policy) into every system prompt. See `references/constitutional-framework.md` Section 6.

Separate: `DELIBERATING_AGENTS` (12) and `CHAIR_AGENT` (COORD only).

### Prompt Templates

Two templates with mustache placeholders (`{{title}}`, `{{description}}`, `{{context}}`):
- `DELIBERATION_PROMPT` — requests JSON: vote/reasoning/concerns/recommendations/confidenceLevel/complianceFlags/constitutionalViolation
- `CHAIR_SYNTHESIS_PROMPT` — includes all 12 votes, asks for synthesis

### Deliberation Flow

`startDeliberation(deliberationId)`: fetch → generate hash → audit "started" → process 12 agents **sequentially** (build prompt → invokeLLM with JSON schema → parse → save → update completedAgents → audit) → process COORD last with synthesis → computeVerdict → update record → audit "completed".

Fire asynchronously from tRPC mutation (don't await).

### Verdict Computation

Export `computeVerdict` as pure function:
```
if (constitutionalViolation OR escalateCount >= 3) → "escalated"
else if (approveCount >= 7) → "approved"
else if (rejectCount >= 7) → "rejected"
else if (approveCount === rejectCount) → "split"
else → "deferred"
```

### Audit Chain

Each entry: `hash = SHA-256(eventType + eventData + previousHash)`. First entry uses null. Tamper-evident — modified entry breaks all subsequent hashes.

## Phase 4: Write tRPC Routers

Read `references/schema-architecture.md` Section 2 for full structure.

Key: `deliberation.submit` (protected, validates title ≥3, description ≥10), `agents.list` (public, **never expose system prompts**), `constitution.get` (structured data), `audit.verify` (walk chain, recompute hashes).

## Phase 5: Implement Design System

Read `references/design-system.md` for complete specification.

Critical: light theme (warm stone, not white), serif headings (Cormorant Garamond), forest green primary, gold accent, top navigation (NOT sidebar), monospace ONLY for audit hashes, grain texture overlay, slow motion (400-600ms). Apply via Tailwind 4 `@theme inline` with OKLCH colors.

## Phase 6: Build 8 Frontend Pages

### Shared Components First

`Navigation.tsx` (top bar, logo, nav links, user), `Footer.tsx` (branding, links), `PageLayout.tsx` (wraps Nav + children + Footer).

### Pages (build order)

1. **Home** — hero "Decisions deserve deliberation", features, 13-agent showcase, 4-tier pricing, CTA
2. **BoardroomPage** — submission form (title, description, context), submit triggers engine
3. **DeliberationPage** — agent response cards with vote badges, progress, COORD synthesis, verdict
4. **HistoryPage** — search, filter by verdict (All/Approved/Rejected/Escalated/Split)
5. **ConstitutionPage** — invariants (expandable), forbidden states, failure policy table, authority ladder, quorum
6. **AuditPage** — hash-chained ledger viewer, integrity verification
7. **ExtensionsPage** — 10 extensions, category filters, tier badges, pricing. See `references/extensions-catalog.md`
8. **SettingsPage** — workspace config (general, team, notifications, API, billing, security)
9. **ProfilePage** — identity card, stats, recent decisions, governance identity

Vote badge colors: approve=green, reject=red, abstain=gray, escalate=gold. Empty states use organic/leaf motifs with CTAs.

## Phase 7: Test and Deliver

Vitest `server/deliberation.test.ts`:
1. Agent Definitions — 13 agents, unique IDs/roles, COORD is chair, prompts reference governance
2. Prompt Templates — placeholders, JSON format, vote options, invariant references
3. Verdict Computation — test `computeVerdict` directly: majority approve/reject, split, deferred, escalation triggers, edge cases
4. tRPC Routers — agent list (no prompts exposed), auth protection, input validation

Delivery checklist: 0 TypeScript errors, all tests passing, all pages render, navigation works, submission validates, no local media files, todo.md updated.

## Guardrails

- Never expose agent system prompts to frontend
- Constitutional constraints injected into every agent prompt — no exceptions
- Audit chain is append-only — no updates, no deletes
- COORD always deliberates LAST
- Hash chain integrity: broken hash = suspect chain
- Extensions cannot modify kernel (INV-006)
- Prefer stopping to lying (INV-002) — engine failure → mark "failed", never fabricate
