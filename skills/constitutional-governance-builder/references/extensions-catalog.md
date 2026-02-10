# Extensions Catalog

10 bolt-on extensions for the Constitutional Boardroom. Each extension operates within INV-006 (Extension Compliance) — no override, no bypass.

## Extension Definitions

Use this data to populate the extensions marketplace UI and database seed.

```ts
const EXTENSIONS = [
  {
    extensionId: "agi-rental",
    name: "AGI Rental Engine",
    category: "Compute",
    tier: "professional",
    pricingModel: "per-hour",
    price: "£2.50/hr",
    description: "On-demand access to advanced reasoning models for complex multi-step deliberations.",
    features: ["Advanced reasoning chains", "Multi-model ensemble", "Priority queue access", "Usage-based billing"],
    icon: "Cpu"
  },
  {
    extensionId: "piopl-tools",
    name: "PIOPL Tools Suite",
    category: "Operations",
    tier: "professional",
    pricingModel: "monthly",
    price: "£29/month",
    description: "Procedural Intelligence Operations Pipeline — structured workflow tools for governance operations.",
    features: ["Workflow automation", "Compliance checklists", "Evidence collection", "Report generation"],
    icon: "Wrench"
  },
  {
    extensionId: "truth-tools",
    name: "Truth Verification Tools",
    category: "Verification",
    tier: "professional",
    pricingModel: "monthly",
    price: "£19/month",
    description: "Cross-reference claims against verified data sources with confidence scoring.",
    features: ["Source verification", "Claim cross-referencing", "Confidence scoring", "Citation tracking"],
    icon: "Search"
  },
  {
    extensionId: "pathology-detector",
    name: "Pathology Detector",
    category: "Analysis",
    tier: "enterprise",
    pricingModel: "monthly",
    price: "£39/month",
    description: "Identifies reasoning pathologies, logical fallacies, and cognitive biases in deliberations.",
    features: ["Fallacy detection", "Bias identification", "Manipulation flags", "Reasoning quality score"],
    icon: "Brain"
  },
  {
    extensionId: "sovereign-sync",
    name: "Sovereign Sync",
    category: "Infrastructure",
    tier: "enterprise",
    pricingModel: "monthly",
    price: "£49/month",
    description: "Multi-instance synchronisation for distributed governance across workspaces.",
    features: ["Cross-workspace sync", "Constitutional alignment", "Conflict resolution", "Distributed audit"],
    icon: "RefreshCw"
  },
  {
    extensionId: "property-intel",
    name: "Property Intelligence",
    category: "Domain",
    tier: "professional",
    pricingModel: "per-lead",
    price: "£5/lead",
    description: "Real estate governance analysis with market data integration and due diligence.",
    features: ["Market analysis", "Due diligence automation", "Risk assessment", "Regulatory compliance"],
    icon: "Building"
  },
  {
    extensionId: "gov-reporter",
    name: "Governance Reporter",
    category: "Reporting",
    tier: "professional",
    pricingModel: "monthly",
    price: "£19/month",
    description: "Automated governance report generation with compliance summaries and trend analysis.",
    features: ["Auto-generated reports", "Compliance summaries", "Trend analysis", "Export to PDF/DOCX"],
    icon: "FileText"
  },
  {
    extensionId: "delib-templates",
    name: "Deliberation Templates",
    category: "Templates",
    tier: "foundation",
    pricingModel: "one-time",
    price: "£49",
    description: "Pre-configured decision frameworks for common governance scenarios.",
    features: ["50+ templates", "Custom template builder", "Category organisation", "Community templates"],
    icon: "Layout"
  },
  {
    extensionId: "voice-interface",
    name: "Voice Interface",
    category: "Interface",
    tier: "professional",
    pricingModel: "monthly",
    price: "£15/month",
    description: "Submit decisions and receive verdicts via voice with natural language processing.",
    features: ["Voice submission", "Audio verdicts", "Multi-language", "Transcription logs"],
    icon: "Mic"
  },
  {
    extensionId: "evidence-vault",
    name: "Evidence Vault",
    category: "Storage",
    tier: "enterprise",
    pricingModel: "monthly",
    price: "£25/month",
    description: "Encrypted document storage with hash-verified integrity for deliberation evidence.",
    features: ["Encrypted storage", "Hash verification", "Access control", "Retention policies"],
    icon: "Shield"
  }
];
```

## Pricing Tiers

| Tier | Price | Included Extensions |
|------|-------|-------------------|
| Foundation | Free | Deliberation Templates only |
| Professional | £49/mo | All Professional + Foundation extensions |
| Enterprise | £199/mo | All Enterprise + Professional + Foundation |
| Sovereign | Custom | Everything + dedicated infrastructure |

## Category Filter Values

`All`, `Compute`, `Operations`, `Verification`, `Analysis`, `Infrastructure`, `Domain`, `Reporting`, `Templates`, `Interface`, `Storage`
