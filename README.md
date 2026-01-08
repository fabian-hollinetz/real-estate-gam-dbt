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

- Data is loaded from **Parquet snapshots** generated from dbt (no hardcoded SQL required)
- Features are defined via **`FeatureSpec` objects**, allowing flexible assignment of:
  - Feature type: `categorical`, `continuous`, `binned`
  - GAM term: `factor` or `spline`
  - Optional smoothing parameter (`lam`) for splines
- Design matrices are automatically built from the `FeatureSpec` list
- A **LinearGAM** is dynamically constructed using `pygam` with terms derived from the design matrix
- Evaluation metrics: **R²** and **RMSE**
- Partial dependence plots are automatically generated for all features
- Code is modular under `src/`:
  - `data/` → feature loading and minimal preprocessing
  - `models/` → dynamic GAM term construction and fitting
  - `evaluation/` → plots and metrics
  - `run_gam.py` → pipeline orchestration

---

## Getting Started

1. **Install dependencies**:

```bash
pip install pandas numpy pygam matplotlib scikit-learn pyyaml
```

2. **Set up dbt pipeline** :

```bash
dbt run
dbt test
```

3. **Run the GAM**:

```bash
python3 -m src.run_gam
```

Partial dependence plots will be displayed, and R²/RMSE metrics printed.

## Project Structure

.
├── data/ # Raw CSVs and Parquet snapshots
├── real_estate_dbt/ # dbt project
├── real_estate_gam/ # Python GAM pipeline
│ ├── data/ # Feature loading, preprocessing
│ ├── models/ # GAM building and fitting
│ ├── evaluation/ # Plots and metrics
│ ├── features/ # FeatureSpec definitions and design matrix
│ └── run_gam.py # Entry point
├── README.md
└── .gitignore

## Notes on Current Pipeline

- The pipeline is fully functional with the new dynamic GAM construction
- Partial dependence plots and evaluation metrics confirm the correct handling of new data
- FeatureSpec allows easy experimentation with factor vs smooth terms
- All design decisions (feature order, encoding, GAM term type) are configurable via Python objects, ready for YAML-based experiments in the future

## Future Work: Listings Data Enrichment

A conceptual architecture for responsibly collecting real estate
listings data is documented, but intentionally not implemented due to
legal and ethical considerations.

## This version:

- Updates **GAM implementation description** to match your dynamic `FeatureSpec`/design matrix approach
- Notes that the **pipeline is verified on new data**
- Mentions that **partial dependence plots** are now fully functional
- Prepares the README for the **future YAML experiment setup**

---
