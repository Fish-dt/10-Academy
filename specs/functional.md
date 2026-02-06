# Functional Specification

## 1. Agent Network Capabilities (FastRender Swarm)
- **Content Generation**: Agents must orchestrate external APIs (Gemini, Midjourney, Kling) via MCP Tools.
- **Trend Awareness**: The `skill-trend-scout` must surface a ranked list of topics with "Viral Potential" scores.
- **Economic Agency**: Agents must be able to manage on-chain transactions via Coinbase AgentKit.

## 2. Governance & Safety
- **Human-in-the-Loop (HITL)**: Any content with a "Judge Confidence Score" below 0.8 must be escalated to the Human Orchestrator.
- **Spend Limits**: Outbound transactions must be gated by the `WalletManager` component.

## 3. User Stories
- **As an Orchestrator**, I want to define a "Soul" (SOUL.md) so my agent maintains a consistent persona across all platforms.
- **As an Agent**, I need to monitor web trends so I can propose relevant content to the Planner.