import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from ..db import con

def render_html(output: str = "reports/latest.html"):
    df = con.execute("SELECT * FROM analysis").fetch_df()
    if df.empty:
        print("Aucune analyse. Lancez analyze d'abord.")
        return
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape()
    )
    os.makedirs("reports", exist_ok=True)
    template = env.get_template("report.html.j2")
    html = template.render(
        n=len(df),
        ppm2_median=float(df["price_per_m2"].median()),
        top=df.sort_values("price_per_m2").head(20).to_dict(orient="records"),
    )
    with open(output, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Rapport HTML généré: {output}")
