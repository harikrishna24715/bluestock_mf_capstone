import pandas as pd

perf = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

risk = input(
    "Risk Appetite (Low/Moderate/High): "
)

funds = perf[
    perf["risk_grade"]
    .str.contains(
        risk,
        case=False,
        na=False
    )
]

recommend = funds.sort_values(
    "sharpe_ratio",
    ascending=False
).head(3)

print(recommend[
    [
        "scheme_name",
        "risk_grade",
        "sharpe_ratio"
    ]
])