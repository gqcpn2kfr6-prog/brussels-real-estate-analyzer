import duckdb
import pandas as pd
from ..db import con

def analyze(min_yield: float = 4.0):
    # Calculs simples: prix/m², filtrage, détection d’outliers
    df = con.execute("SELECT * FROM listings").fetch_df()
    if df.empty:
        print("Aucune donnée. Lancez fetch d'abord.")
        return
    df["price_per_m2"] = df["price"] / df["area"].replace({0: None})
    q1 = df["price_per_m2"].quantile(0.25)
    q3 = df["price_per_m2"].quantile(0.75)
    iqr = q3 - q1
    df["is_outlier_low"] = df["price_per_m2"] < (q1 - 1.5 * iqr)
    df["is_outlier_high"] = df["price_per_m2"] > (q3 + 1.5 * iqr)

    con.register("df", df)
    con.execute("CREATE OR REPLACE TABLE analysis AS SELECT * FROM df")
    print("Analyse terminée.")
