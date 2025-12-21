# Real Estate Price Modeling with dbt and GAMs

This project demonstrates an **end-to-end data pipeline** for real estate price modeling,
combining **dbt** for structured data transformations with **Generalized Additive Models (GAMs)**
for interpretable price prediction.

The focus is on building a **clean, modular, and reproducible analytics pipeline**,
with a Python GAM ready for portfolio presentation.

---

## Project Overview

The pipeline follows a **layered data modeling approach**:

1. **Staging Layer**  
   - Technical cleaning and preparation of raw transaction data  
   - Example table: `stg_transactions`

2. **Feature Layer**  
   - Model-ready features used as input for the GAM  
   - Example table: `gam_features`  
   - Includes checks for nulls and uniqueness via dbt tests

3. **Mart / Fact Layer**  
   - Definition of the target variable (`price`) and core analytical facts  
   - Example table: `fct_prices`

This structure ensures that:  
- data transformations are **transparent and testable**  
- modeling code remains **modular and focused**  
- analytical results are **reproducible**  

---

## Python GAM Implementation

- Data is loaded from Postgres via **SQLAlchemy** and dbt output tables  
- A **LinearGAM** is defined using `pygam` with splines for each feature:  
  - `living_area`, `rooms`, `year`, `latitude`, `longitude`  
- Evaluation metrics: **R²** and **RMSE**  
- Partial dependence plots are automatically generated for all features  
- Code is modular under `src/`:
  - `data/` → DB connection and feature loading  
  - `models/` → GAM definition and fitting  
  - `evaluation/` → plots and metrics  
  - `run_gam.py` → entry point

---

## Getting Started

1. **Install dependencies**:

### 1. Install dependencies
pip install pandas sqlalchemy psycopg2-binary pygam matplotlib scikit-learn

### 2. Set up Postgres and run the dbt pipeline:
dbt run
dbt test

### 3. Run the GAM:
python3 -m src.run_gam

Partial dependence plots will be displayed, and R²/RMSE metrics printed.

## Project Structure
```bash
.
├── data/                 # Raw CSVs
├── real_estate_dbt/      # dbt project
├── src/                  # Python GAM pipeline
│   ├── data/
│   ├── models/
│   ├── evaluation/
│   └── run_gam.py
├── README.md
└── .gitignore
```

## Future Work: Listings Data Enrichment

A conceptual architecture for responsibly collecting real estate
listings data is documented, but intentionally not implemented due to
legal and ethical considerations.
