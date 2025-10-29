# Brussels Real Estate Analyzer

[![Run compare](https://github.com/gqcpn2kfr6-prog/brussels-real-estate-analyzer/actions/workflows/compare.yml/badge.svg)](https://github.com/gqcpn2kfr6-prog/brussels-real-estate-analyzer/actions/workflows/compare.yml)

Bot d'analyse du marché immobilier bruxellois.

## Lancer en un clic
- Ouvrez l'onglet Actions → workflow « compare » → Run workflow
- Laissez les valeurs par défaut ou choisissez la ville/source puis cliquez sur « Run workflow »
- Le rapport sera publié (Pages) et/ou disponible en artefact « report-html »

## Fonctionnalités
- Scraping (APIs ou pages publiques) d'annonces (Immoweb, Zimmo, ImmoVlan, Notaire) via connecteurs optionnels
- Nettoyage et normalisation des données (quartier, surface, chambres, prix, charges, rendement…)
- Enrichissement (géocodage, quartiers/stat. stratégiques de Bruxelles, indices CPI)
- Analyse (prix/m², tendances, anomalies, rendement brut/net)
- Détection d'opportunités (sous-évaluations, cash-flow > 0, rentabilité cible)
- Exports (CSV/Parquet) et rapport Markdown/HTML automatisé
