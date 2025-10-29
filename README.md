# Brussels Real Estate Analyzer

Bot d'analyse du marché immobilier bruxellois.

## Fonctionnalités
- Scraping (APIs ou pages publiques) d'annonces (Immoweb, Zimmo, ImmoVlan, Notaire) via connecteurs optionnels
- Nettoyage et normalisation des données (quartier, surface, chambres, prix, charges, rendement…)
- Enrichissement (géocodage, quartiers/stat. stratégiques de Bruxelles, indices CPI)
- Analyse (prix/m², tendances, anomalies, rendement brut/net)
- Détection d'opportunités (sous-évaluations, cash-flow > 0, rentabilité cible)
- Exports (CSV/Parquet) et rapport Markdown automatisé

## Stack
- Python 3.11, Poetry
- Pandas, Polars, NumPy, Pydantic
- DuckDB pour stockage colonne
- Typer (CLI)
- Requests/HTTPX, Playwright (scraping optionnel)
- GeoPandas/Shapely (géospatial)
- scikit-learn (modèles simples)
- GitHub Actions (cron) pour refresh quotidien/hebdo

## Legal & Ethique
- Respect des CGU des sites; privilégier les APIs/offres data officielles
- Povider des délais, user-agent, robots.txt; pas de charge abusive
- Données destinées à un usage personnel/étude; vérifier la conformité RGPD

## Démarrage rapide
```
poetry install
poetry run analyzer fetch --source immoweb --city "Bruxelles"
poetry run analyzer analyze --min-yield 4.5
```
