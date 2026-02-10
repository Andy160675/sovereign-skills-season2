# Schema & Architecture Reference

## Table of Contents
1. Database Schema
2. tRPC Router Structure
3. Deliberation Engine
4. Audit Chain
5. Extension Marketplace
6. Frontend Routes
7. Test Strategy

## 1. Database Schema (Drizzle ORM, MySQL/TiDB)

### users
Extended with `authorityTier` enum for governance tiers.

```ts
users = mysqlTable("users", {
  id: int().autoincrement().primaryKey(),
  openId: varchar({ length: 64 }).notNull().unique(),
  name: text(),
  email: varchar({ length: 320 }),
  role: mysqlEnum(["user", "admin"]).default("user"),
  authorityTier: mysqlEnum(["foundation", "professional", "enterprise", "sovereign"]).default("foundation"),
  createdAt: timestamp().defaultNow(),
  updatedAt: timestamp().defaultNow().onUpdateNow(),
  lastSignedIn: timestamp().defaultNow(),
});
```

### deliberations
Core decision record with vote tallies and verdict.

```ts
deliberations = mysqlTable("deliberations", {
  id: int().autoincrement().primaryKey(),
  userId: int().notNull(),
  title: varchar({ length: 500 }).notNull(),
  description: text().notNull(),
  context: text(),
  status: mysqlEnum(["pending", "deliberating", "completed", "failed"]).default("pending"),
  finalVerdict: mysqlEnum(["approved", "rejected", "escalated", "split", "deferred"]),
  approveCount: int().default(0),
  rejectCount: int().default(0),
  abstainCount: int().default(0),
  escalateCount: int().default(0),
  complianceScore: float(),
  riskScore: float(),
  summary: text(),
  decisionHash: varchar({ length: 64 }),
  completedAgents: int().default(0),
  totalAgents: int().default(13),
  createdAt: timestamp().defaultNow(),
  completedAt: timestamp(),
});
```

### agent_responses
Individual agent deliberation output.

```ts
agentResponses = mysqlTable("agent_responses", {
  id: int().autoincrement().primaryKey(),
  deliberationId: int().notNull(),
  agentRole: varchar({ length: 64 }).notNull(),
  agentName: varchar({ length: 128 }).notNull(),
  vote: mysqlEnum(["approve", "reject", "abstain", "escalate"]),
  reasoning: text(),
  concerns: text(),
  recommendations: text(),
  confidenceLevel: float(),
  complianceFlags: json().$type<string[]>(),
  constitutionalViolation: boolean().default(false),
  status: mysqlEnum(["pending", "processing", "completed", "failed"]).default("pending"),
  processingTimeMs: int(),
  createdAt: timestamp().defaultNow(),
  completedAt: timestamp(),
});
```

### audit_chain
Hash-chained ledger for tamper-proof audit trail.

```ts
auditChain = mysqlTable("audit_chain", {
  id: int().autoincrement().primaryKey(),
  deliberationId: int().notNull(),
  eventType: varchar({ length: 64 }).notNull(),
  eventData: text(),
  hash: varchar({ length: 128 }).notNull(),
  previousHash: varchar({ length: 128 }),
  createdAt: timestamp().defaultNow(),
});
```

### extensions
Bolt-on marketplace catalog.

```ts
extensions = mysqlTable("extensions", {
  id: int().autoincrement().primaryKey(),
  extensionId: varchar({ length: 32 }).notNull().unique(),
  name: varchar({ length: 128 }).notNull(),
  description: text(),
  category: varchar({ length: 64 }).notNull(),
  pricingModel: varchar({ length: 32 }).notNull(),
  price: varchar({ length: 64 }),
  tier: mysqlEnum(["foundation", "professional", "enterprise", "sovereign"]).default("professional"),
  isActive: boolean().default(true),
  createdAt: timestamp().defaultNow(),
});
```

## 2. tRPC Router Structure

```
appRouter
├── auth.me (public query)
├── auth.logout (public mutation)
├── agents.list (public query) — returns 13 agents without system prompts
├── constitution.get (public query) — returns invariants, forbidden states, failure policy
├── deliberation.submit (protected mutation) — creates deliberation, starts engine
├── deliberation.get (public query) — single deliberation with responses
├── deliberation.responses (public query) — agent responses for a deliberation
├── deliberation.history (protected query) — user's deliberation history
├── deliberation.recent (public query) — recent deliberations
├── audit.chain (public query) — audit entries for a deliberation
├── audit.verify (public query) — verify hash chain integrity
└── extensions.list (public query) — all extensions
```

## 3. Deliberation Engine

File: `server/deliberation.ts`

Flow:
1. Create deliberation record (status: pending)
2. Generate decision hash (SHA-256 of title + description + timestamp)
3. Add audit entry: "deliberation_started"
4. Process 12 agents sequentially (not COORD):
   a. Build agent prompt with constitutional context
   b. Call LLM with JSON schema response format
   c. Parse vote, reasoning, concerns, recommendations
   d. Save agent_response record
   e. Update deliberation.completedAgents
   f. Add audit entry per agent
5. Process COORD (Chair) last:
   a. Build synthesis prompt with all 12 votes
   b. COORD can override to ESCALATE despite quorum
6. Compute verdict using quorum rules
7. Update deliberation with final verdict, scores, summary
8. Add audit entry: "deliberation_completed"

Key functions:
- `buildAgentPrompt(agent, title, description, context)` — template with mustache-style placeholders
- `buildChairPrompt(title, description, context, agentVotes, counts)` — synthesis prompt
- `invokeAgent(agent, userPrompt)` — calls invokeLLM with JSON schema
- `computeVerdict(responses)` — quorum logic
- `startDeliberation(deliberationId)` — orchestrates full flow

LLM response schema per agent:
```json
{
  "vote": "approve|reject|abstain|escalate",
  "reasoning": "string",
  "concerns": "string",
  "recommendations": "string",
  "confidenceLevel": 0.0-1.0,
  "complianceFlags": ["string"],
  "constitutionalViolation": false
}
```

## 4. Audit Chain

Each entry is hash-chained: `hash = SHA-256(eventType + eventData + previousHash)`

Event types: `deliberation_started`, `agent_vote_{ROLE}`, `deliberation_completed`

Verification: walk the chain, recompute each hash, compare.

## 5. Extension Marketplace

10 bolt-on extensions with pricing models:

| Extension | Category | Tier | Pricing |
|-----------|----------|------|---------|
| AGI Rental Engine | Compute | Professional | £2.50/hr |
| PIOPL Tools Suite | Operations | Professional | £29/mo |
| Truth Verification Tools | Verification | Professional | £19/mo |
| Pathology Detector | Analysis | Enterprise | £39/mo |
| Sovereign Sync | Infrastructure | Enterprise | £49/mo |
| Property Intelligence | Domain | Professional | £5/lead |
| Governance Reporter | Reporting | Professional | £19/mo |
| Deliberation Templates | Templates | Foundation | £49 one-time |
| Voice Interface | Interface | Professional | £15/mo |
| Evidence Vault | Storage | Enterprise | £25/mo |

## 6. Frontend Routes

| Path | Page | Description |
|------|------|-------------|
| `/` | Home | Landing page with hero, features, agents, pricing |
| `/boardroom` | BoardroomPage | Decision submission form |
| `/deliberation/:id` | DeliberationPage | Single deliberation view with agent responses |
| `/history` | HistoryPage | Decision history with search and filters |
| `/constitution` | ConstitutionPage | Invariants, forbidden states, failure policy |
| `/audit` | AuditPage | Hash-chained ledger viewer |
| `/extensions` | ExtensionsPage | 10 bolt-on marketplace |
| `/settings` | SettingsPage | Workspace configuration |
| `/profile` | ProfilePage | Sovereign governance identity |

## 7. Test Strategy

Vitest test file: `server/deliberation.test.ts`

Test groups:
1. **Agent Definitions** — 13 agents, unique IDs/roles, required fields, COORD is chair, prompts reference governance
2. **Deliberation Prompt Template** — placeholders, JSON format, vote options, invariant references
3. **Verdict Computation** — quorum logic (7/13), escalation triggers, edge cases (all abstain, unanimous, split)
4. **tRPC Routers** — agent list shape, auth protection, input validation

Import `computeVerdict` and agent constants directly for unit testing. Use `createCaller` for tRPC procedure tests.
