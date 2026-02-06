# Technical Specification & Data Contracts

## 1. The FastRender Swarm Pattern (SRS 3.1)
The system decouples reasoning from execution:
- **Planner**: Consumes `SOUL.md` and `GlobalState` to create a Task DAG.
- **Worker**: Stateless executor of MCP Tools.
- **Judge**: Validates output and manages **Optimistic Concurrency Control (OCC)**.

## 2. Skill Interface: Wallet Manager (SRS 4.5)
- **Module**: `skills.wallet`
- **Class**: `WalletManager`
- **Wallet Manager Skill Contract**: 
    - `daily_limit: float`: Maximum USDC allowed per 24h.
    - `execute_transaction(amount: float, target: str)`: 
        - Validates against `daily_limit`.
        - Records entry in `wallet_ledger`.
        - Interface must handle `RuntimeError` for network failures.

## 3. Data Schema: Trend Scout
The `skill-trend-scout` must return the following JSON structure:
```json
{
  "request_id": "UUID",
  "trends": [
    {
      "topic": "string",
      "viral_potential": "float (0.0-1.0)",
      "description": "string"
    }
  ]
}