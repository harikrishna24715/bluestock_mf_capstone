# Data Dictionary

## dim_fund

| Column             | Data Type | Description                      |
| ------------------ | --------- | -------------------------------- |
| amfi_code          | INTEGER   | Unique AMFI scheme code          |
| fund_house         | TEXT      | Asset management company name    |
| scheme_name        | TEXT      | Mutual fund scheme name          |
| category           | TEXT      | Fund category (Equity/Debt)      |
| sub_category       | TEXT      | Detailed category classification |
| plan               | TEXT      | Direct/Regular plan              |
| launch_date        | DATE      | Fund launch date                 |
| benchmark          | TEXT      | Benchmark index                  |
| expense_ratio_pct  | REAL      | Expense ratio percentage         |
| exit_load_pct      | REAL      | Exit load percentage             |
| min_sip_amount     | REAL      | Minimum SIP investment           |
| min_lumpsum_amount | REAL      | Minimum lump-sum investment      |
| fund_manager       | TEXT      | Fund manager name                |
| risk_category      | TEXT      | Risk classification              |
| sebi_category_code | TEXT      | SEBI category code               |

## fact_nav

| Column    | Data Type | Description      |
| --------- | --------- | ---------------- |
| amfi_code | INTEGER   | Fund scheme code |
| date      | DATE      | NAV date         |
| nav       | REAL      | Net Asset Value  |

## fact_transactions

| Column             | Data Type | Description                 |
| ------------------ | --------- | --------------------------- |
| investor_id        | TEXT      | Investor identifier         |
| transaction_date   | DATE      | Transaction date            |
| amfi_code          | INTEGER   | Fund scheme code            |
| transaction_type   | TEXT      | SIP / Lumpsum / Redemption  |
| amount_inr         | REAL      | Transaction amount          |
| state              | TEXT      | Investor state              |
| city               | TEXT      | Investor city               |
| city_tier          | TEXT      | T30/B30 classification      |
| age_group          | TEXT      | Investor age bucket         |
| gender             | TEXT      | Investor gender             |
| annual_income_lakh | REAL      | Annual income in lakhs      |
| payment_mode       | TEXT      | UPI/Cheque/Net Banking etc. |
| kyc_status         | TEXT      | KYC verification status     |


dim_fund
amfi_code
fund_house
scheme_name
category
sub_category
...
fact_nav
amfi_code
date
nav
fact_transactions
investor_id
transaction_date
amount_inr
...
fact_performance
return_1yr_pct
sharpe_ratio
beta
...
fact_aum
date
fund_house
aum_crore
