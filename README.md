# Real Estate Price Modeling with dbt and GAMs

This project demonstrates an end-to-end data pipeline for real estate price modeling,
combining **dbt** for data transformations with **Generalized Additive Models (GAMs)**
for interpretable price prediction.

The focus is on building a **clean, reproducible, and well-structured analytics pipeline**
that prepares data specifically for statistical modeling.

---

## Project Overview

The pipeline follows a layered data modeling approach:

1. **Staging Layer**  
   Technical cleaning and preparation of raw transaction data.

2. **Mart / Fact Layer**  
   Definition of the target variable (`price`) and core analytical facts.

3. **Feature Layer**  
   Model-ready features used as input for a GAM.

This structure ensures that:
- data transformations are transparent and testable
- modeling code remains simple and focused
- analytical results are reproducible

---

## Data Flow
