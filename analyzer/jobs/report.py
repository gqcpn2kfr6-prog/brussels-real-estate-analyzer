from datetime import datetime
from ..db import con

TEMPLATE = """
# Rapport du {date}

## Statistiques clés
- Nombre d'annonces: {n}
- Prix/m² médian: {ppm2_median:.0f} €
- Part d'outliers bas: {low:.1%}
- Part d'outliers hauts: {high:.1%}

## Top 10 opportunités (prix/m² le + bas)
{top10}
"""

def report(output: str = "reports/latest.md"):
    df = con.execute("SELECT * FROM analysis").fetch_df()
    if df.empty:
        print("Aucune analyse. Lancez analyze d'abord.")
        return
    n = len(df)
    ppm2_median = df["price_per_m2"].median()
    low = (df["is_outlier_low"].mean()) if "is_outlier_low" in df else 0
    high = (df["is_outlier_high"].mean()) if "is_outlier_high" in df else 0

    top = df.sort_values("price_per_m2").head(10)
    lines = []
    for _, r in top.iterrows():
        lines.append(f"- {r['title']} | {r['price_per_m2']:.0f} €/m² | {r['url']}")

    content = TEMPLATE.format(
        date=datetime.now().strftime("%Y-%m-%d"),
        n=n,
        ppm2_median=ppm2_median,
        low=low,
        high=high,
        top10="\n".join(lines),
    )

    import os
    os.makedirs("reports", exist_ok=True)
    with open(output, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Rapport généré: {output}")
