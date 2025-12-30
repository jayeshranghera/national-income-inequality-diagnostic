# National Income Inequality Diagnostic

## Project Overview
Income inequality is one of the most critical socio-economic challenges affecting
economic stability, social mobility, and policy effectiveness.
This project analyzes income inequality across countries using the Gini Index,
with a focused diagnostic on Germany and comparative global perspectives.

The objective is not prediction, but **diagnosis, comparison, and interpretation**
of inequality patterns using officially published public data.

---

## Research Questions
- How has income inequality evolved over time across countries?
- How does Germany compare to regional and income-group averages?
- Does higher national income imply lower inequality?
- Which countries exhibit persistent inequality versus volatile inequality?

---

## Data Sources
- World Bank – Gini Index (SI.POV.GINI)
- World Bank Country Metadata (region, income group)

The dataset is aggregated at the country-year level and reflects
officially reported inequality indicators used in policy research.

---

## Methodology

### 1. Data Pipeline
- Raw data downloaded from official World Bank sources (CSV format)
- Raw data preserved unchanged
- Programmatic transformation using Python:
  - Wide-to-long reshaping
  - Type normalization
  - Removal of missing inequality values
  - Enrichment with country metadata (region, income group)

### 2. Analysis Approach
- Time-series trend analysis
- Regional and income-group aggregation
- Country-level comparison (Germany focus)
- Inequality persistence analysis using mean and volatility (standard deviation)

---

## Project Structure

national-income-inequality-diagnostic/
│
├── data/
│ ├── raw/ # Original World Bank CSV files
│ └── processed/ # Analysis-ready datasets (generated)
│
├── notebooks/
│ ├── 01_data_understanding.ipynb
│ ├── 02_data_cleaning.ipynb
│ ├── 03_inequality_trends.ipynb
│ └── 04_country_comparison.ipynb
│
├── src/ # Reusable Python modules
│ ├── data_loader.py
│ ├── cleaning.py
│ ├── inequality_metrics.py
│ └── visualization.py
│
├── outputs/
│ ├── figures/ # Saved plots
│ └── tables/ # Summary tables
│
├── README.md
├── requirements.txt
└── .gitignore


---

## Key Findings
- Income inequality trends vary significantly across regions.
- High-income countries do not necessarily exhibit low inequality.
- Germany shows relatively stable inequality compared to global extremes.
- Regional and income-group averages often mask country-level variation.
- Persistence analysis helps distinguish structural inequality from volatility.

---

## Tools & Technologies
- Python
- pandas
- numpy
- matplotlib
- Jupyter Notebook

---

## Reproducibility
1. Clone the repository
2. Install dependencies from `requirements.txt`
3. Run notebooks sequentially from `01_data_understanding.ipynb` to `04_country_comparison.ipynb`

All processed datasets and figures are generated programmatically.

---

## Disclaimer
This project uses aggregated public data and is intended for analytical
and educational purposes. It does not perform individual-level income modeling
or causal inference.

---

## Author
Jayesh Ranghera
Social / Applied Data Science
