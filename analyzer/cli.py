import typer
from .jobs.fetch import fetch
from .jobs.analyze import analyze
from .jobs.report import report

app = typer.Typer(help="Brussels Real Estate Analyzer")

@app.command()
def fetch_cmd(source: str = typer.Option(..., help="Source: immoweb|zimmo|immovlan|notaire"),
              city: str = typer.Option("Bruxelles", help="Ville ou commune"),
              limit: int = typer.Option(200, help="Nombre max d'annonces")):
    fetch(source=source, city=city, limit=limit)

@app.command()
def analyze_cmd(min_yield: float = typer.Option(4.0, help="Rendement cible brut %")):
    analyze(min_yield=min_yield)

@app.command()
def report_cmd(output: str = typer.Option("reports/latest.md", help="Chemin du rapport")):
    report(output=output)
