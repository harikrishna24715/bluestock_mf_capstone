# Bluestock Mutual Fund Analytics Capstone Project

## Overview

The Bluestock Mutual Fund Analytics Capstone Project is an end-to-end data analytics solution designed to analyze mutual fund performance, investor behavior, industry trends, and risk metrics. The project combines data engineering, financial analytics, database management, and business intelligence to provide meaningful insights into the Indian mutual fund industry.

The solution processes multiple mutual fund datasets, performs extensive data cleaning and transformation, stores the processed data in a SQLite database, computes advanced performance and risk metrics, and visualizes insights through an interactive Power BI dashboard.

---

## Project Objectives

* Analyze mutual fund performance using historical NAV data.
* Evaluate investor behavior and transaction patterns.
* Measure risk-adjusted returns using financial metrics.
* Develop advanced risk analytics models.
* Create an interactive Power BI dashboard.
* Generate actionable investment insights through data-driven analysis.

---

## Key Features

### Data Engineering & ETL

* Data cleaning and validation
* Missing value handling
* Duplicate removal
* Date standardization
* SQLite database integration

### Exploratory Data Analysis (EDA)

* NAV Trend Analysis
* AUM Growth Analysis
* SIP Inflow Trends
* Investor Demographics Analysis
* Category Inflow Analysis
* Folio Growth Analysis

### Performance Analytics

* CAGR Calculation
* Sharpe Ratio
* Sortino Ratio
* Alpha & Beta Analysis
* Maximum Drawdown
* Fund Scorecard Ranking

### Advanced Analytics

* Value at Risk (VaR)
* Conditional Value at Risk (CVaR)
* Rolling Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Sector Concentration (HHI)
* Fund Recommendation System

### Dashboard Development

* Industry Overview Dashboard
* Fund Performance Dashboard
* Investor Analytics Dashboard
* SIP & Market Trends Dashboard

---

## Technologies Used

| Category        | Technologies                |
| --------------- | --------------------------- |
| Programming     | Python                      |
| Data Analysis   | Pandas, NumPy               |
| Visualization   | Matplotlib, Seaborn, Plotly |
| Database        | SQLite, SQLAlchemy          |
| Dashboard       | Microsoft Power BI          |
| Development     | Jupyter Notebook            |
| Version Control | Git, GitHub                 |

---

## Project Structure

```text
bluestock_mf_capstone/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── scripts/
│   ├── load_sqlite.py
│   ├── recommender.py
│   └── run_pipeline.py
│
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
│
├── reports/
│   ├── Final_Report.pdf
│   └── Bluestock_MF_Presentation.pptx
│
├── schema.sql
├── queries.sql
├── data_dictionary.md
├── README.md
└── requirements.txt
```

---

## Datasets Used

The project utilizes 10 cleaned datasets:

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Investor Transactions
8. Scheme Performance
9. Portfolio Holdings
10. Benchmark Indices

---

## Database Design

The project uses a star-schema-inspired SQLite database structure consisting of:

### Dimension Tables

* dim_fund
* dim_date

### Fact Tables

* fact_nav
* fact_transactions
* fact_performance
* fact_aum

This design supports efficient querying and analytical reporting.

---

## Performance Metrics Calculated

### Return Metrics

* Daily Returns
* CAGR (1-Year, 3-Year, 5-Year)

### Risk Metrics

* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Value at Risk (VaR)
* Conditional Value at Risk (CVaR)

### Portfolio Metrics

* Sector Concentration (HHI)
* Fund Scorecard

---

## Dashboard Pages

### 1. Industry Overview

* Total AUM
* SIP Inflows
* Folio Counts
* Industry Growth Trends
* AUM by AMC

### 2. Fund Performance

* Return vs Risk Analysis
* Benchmark Comparison
* Fund Rankings
* Interactive Filters

### 3. Investor Analytics

* Demographic Analysis
* Geographic Distribution
* Transaction Trends
* Investment Behavior

### 4. SIP & Market Trends

* SIP Growth Trends
* Category Inflows
* Market Performance
* Investment Patterns

---

## How to Run the Project

### Clone Repository

```bash
git clone <repository-url>
cd bluestock_mf_capstone
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Load Database

```bash
python scripts/load_sqlite.py
```

### Run Recommendation System

```bash
python scripts/recommender.py
```

### Open Dashboard

Open:

```text
dashboard/bluestock_mf_dashboard.pbix
```

using Microsoft Power BI Desktop.

---

## Key Findings

* Mutual fund industry AUM demonstrated strong growth from 2022 to 2025.
* SIP inflows reached record highs, reflecting increasing investor participation.
* Equity funds outperformed debt and liquid funds in long-term returns.
* Several funds generated positive alpha and outperformed benchmark indices.
* Risk-adjusted performance metrics provided deeper insights than returns alone.
* Investor participation expanded significantly across demographics and regions.

---

## Future Enhancements

* Machine Learning-based Fund Recommendation System
* Portfolio Optimization Models
* Real-time Market Data Integration
* Predictive Analytics for Fund Performance
* Web-based Dashboard Deployment
* Automated ETL Scheduling

---

## Author

**Hari Krishna**

Bluestock Mutual Fund Analytics Capstone Project

---

## License

This project was developed for educational and internship purposes as part of the Bluestock Capstone Program.
