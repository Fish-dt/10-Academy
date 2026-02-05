# Data Audit Report: Finance vs. Delivery Reconciliation

## 1. Identified Discrepancies
* **Orphaned Payments**: Order `O5008` is marked `PAID` in Finance (Jan 10) but is completely missing from Delivery logs.
* **Fulfillment Latency**: Order `O5006` shows a 27-day gap between Payment (Jan 5) and Delivery (Feb 1), indicating a pipeline bottleneck.
* **Status Dissonance**: Orders `O5003` and `O5009` are settled in Finance but remain `PENDING` in Delivery, risking duplicate fulfillment.

## 2. The "Three Whys" Root Cause Analysis
1.  **Why is there a discrepancy?** The Finance ledger shows 10 units of revenue, but the Delivery log only shows 7 units of fulfillment.
2.  **Why is the fulfillment log trailing?** Data is being captured in silos; the Delivery team’s "Legacy Process" lacks an automated hook to the new Finance API.
3.  **Why does the legacy process persist?** Perceived "Information Hoarding" stems from a fear of exposing manual inefficiencies during the digital transformation.