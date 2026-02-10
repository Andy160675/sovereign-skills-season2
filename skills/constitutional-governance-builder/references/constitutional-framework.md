# Constitutional Framework Reference

## Table of Contents
1. Seven Invariants
2. Six Forbidden States
3. Failure Policy
4. Authority Ladder
5. Quorum Rules
6. Agent Council (13 Roles)
7. Vote Types
8. Verdict Computation

## 1. Seven Invariants (Immutable)

| ID | Name | Rule |
|----|------|------|
| INV-001 | Subtractive Invariance | VIABLE = TOTAL - FORBIDDEN. Systems stabilize by eliminating impossibilities. |
| INV-002 | Halt Doctrine | Prefer stopping to lying. Uncertainty halts; it does not guess. |
| INV-003 | Authority Ladder | operator → innovator → steward. No cross-authority calls. |
| INV-004 | Audit Completeness | Every transition logged. No unaudited actions. |
| INV-005 | Legality Gate | No signal bypasses validation. Illegality is unrepresentable. |
| INV-006 | Extension Compliance | Extensions cannot modify kernel constraints. |
| INV-007 | Hash Chain Integrity | Tamper = halt. Evidence immutability is absolute. |

## 2. Six Forbidden States

| ID | State | Description |
|----|-------|-------------|
| FRB-001 | unaudited_action | Action executed without audit trail |
| FRB-002 | silent_escalation | Authority escalated without record |
| FRB-003 | cross_authority_call | Operator invoking steward functions |
| FRB-004 | tampered_signal | Evidence modified after commitment |
| FRB-005 | post_halt_execution | Process continuing after halt signal |
| FRB-006 | steward_override_without_dual_key | Override without dual authorization |

## 3. Failure Policy

| Trigger | Action | Severity |
|---------|--------|----------|
| RouterFailure | HALT | critical |
| AuditFailure | HALT | critical |
| LegalityFailure | ESCALATE | high |
| QuorumFailure | ESCALATE | high |
| ConstitutionalViolation | ESCALATE | critical |
| Unknown | HALT | critical |

## 4. Authority Ladder

```
L1: Agent       — Individual governance agent, analyses and votes within role constraints
L2: Council     — Collective of 13 agents, quorum-based decision
L3: Chair       — COORD synthesises council output, can escalate despite quorum
L4: Steward     — Human governance authority, receives escalations
L5: Human Override — Emergency authority, can halt or override with full audit
```

## 5. Quorum Rules

- **Approval**: 7 of 13 votes (simple majority)
- **Rejection**: 7 of 13 votes (simple majority)
- **Auto-Escalate**: Any constitutional violation triggers escalation regardless of vote count
- **Chair Override**: COORD may escalate despite quorum being met
- **Escalation threshold**: 3+ ESCALATE votes from agents → auto-escalate

## 6. Agent Council (13 Roles)

| ID | Title | Focus |
|----|-------|-------|
| LEGAL | Chief Legal Counsel | Legal risk, regulatory compliance, liability |
| FINANCE | Chief Financial Steward | Financial impact, ROI, budget alignment |
| SECURITY | Chief Information Security Officer | Security posture, threat assessment, data protection |
| ETHICS | Chief Ethics Officer | Ethical implications, stakeholder impact, fairness |
| TECH | Chief Technology Officer | Technical feasibility, architecture, scalability |
| OPS | Chief Operations Officer | Operational impact, resource allocation, logistics |
| RISK | Chief Risk Officer | Risk assessment, mitigation, contingency planning |
| AUDIT | Chief Audit Officer | Compliance verification, audit trail, governance |
| COMMS | Chief Communications Officer | Stakeholder communication, reputation, transparency |
| HR | Chief People Officer | Workforce impact, culture, talent implications |
| STRAT | Chief Strategy Officer | Strategic alignment, competitive positioning |
| INNOV | Chief Innovation Officer | Innovation potential, disruption assessment |
| COORD | Council Chair | Synthesises all 12 votes, delivers final recommendation (deliberates LAST) |

Processing order: 12 agents deliberate sequentially, then COORD synthesises.

## 7. Vote Types

- `approve` — Decision is sound and should proceed
- `reject` — Decision should not proceed
- `abstain` — Insufficient information or outside expertise
- `escalate` — Constitutional concern requiring human steward review

## 8. Verdict Computation Logic

```
if (hasConstitutionalViolation OR escalateCount >= 3) → "escalated"
else if (approveCount >= 7) → "approved"
else if (rejectCount >= 7) → "rejected"
else if (approveCount === rejectCount) → "split"
else → "deferred"
```

Derived scores:
- `complianceScore = (1 - (rejectCount + escalateCount) / total) * 100`
- `riskScore = (rejectCount + escalateCount) / total * 100`
- `avgConfidence = sum(confidenceLevels) / validResponses`
