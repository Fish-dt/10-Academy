# Functional Specification: Project Chimera

## 1. Agent Network Capabilities

- **Content Generation**: Agents must be able to generate text and media
  (images/video) by orchestrating external APIs (Gemini, Claude, Kling),
  never via local GPU inference.
- **Trend Awareness**: At least one skill (`skill-trend-scout`) must surface
  a ranked list of trending topics with an associated "Viral Potential" score.
- **Economic Agency**: Each agent must be able to initiate on-chain
  transactions via Coinbase AgentKit, subject to governance constraints.

## 2. Governance & Wallet Controls

- **Daily Spend Limits**: All outbound economic actions must be gated by a
  governor component (`WalletManager`) that enforces a configurable
  daily USDC limit per agent.
- **Auditability**: Every approved transaction must be logged to a
  `wallet_ledger` store for downstream reconciliation and analytics.

## 3. Data Audit & Delivery Reconciliation

- **Discrepancy Detection**: The system must detect and report discrepancies
  between Finance and Delivery logs, including:
  - Orphaned payments (payments without matching delivery events).
  - Fulfillment latency beyond an acceptable threshold.
  - Status dissonance between systems for the same order IDs.
- **Narrative Reporting**: The output of the audit must be human-readable,
  summarizing key issues and root causes in markdown format.

## 4. Skill Interface Contracts (High Level)

- **Trend Scout Skill**:
  - Consumes web/MCP search tools to identify viral topics.
  - Produces a ranked list of at least three candidate trends, each with a
    short description and a numeric "Viral Potential" score.
- **Wallet Manager Skill**:
  - Exposes a minimal interface to evaluate and approve/deny proposed spends.
  - Integrates with the governance layer defined in `technical.md`.
- **Media Orchestrator Skill**:
  - Routes content-generation requests to the appropriate external provider
    (image vs. video) based on budget and context.

