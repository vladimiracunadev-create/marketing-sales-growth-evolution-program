# Persistent Business Simulation

`AndesFlow` is a fictional Chile-based B2B software company. Learners can also replace it with another synthetic company, but should keep the same state model so decisions remain cumulative.

## Initial state
- 500 target accounts.
- 120 known leads.
- 40 active opportunities.
- Average monthly subscription: CLP 180,000.
- Gross margin: 78%.
- Monthly logo churn: 3.2%.
- Marketing monthly budget: CLP 4,000,000.
- Sales team: 2 AEs + 1 SDR.
- Weak CRM discipline and incomplete attribution.

## State fields
Market → segments → offers → prices → campaigns → leads → opportunities → deals → customers → usage/health → renewals → expansion → churn → cash contribution.

Each project updates a state snapshot in `simulations/state/`.
