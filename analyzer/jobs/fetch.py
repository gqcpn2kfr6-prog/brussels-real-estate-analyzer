import httpx
import asyncio
from .parsers import parse_immoweb
from ..db import con
from ..models import Listing

async def fetch_immoweb(city: str, limit: int = 200):
    # Placeholder: utilise l’API publique si disponible, sinon endpoints JSON
    # Ici, on met un exemple minimal (à adapter selon endpoints réels)
    listings: list[Listing] = []
    # ... implémentation spécifique à la source ...
    return listings

async def fetch_zimmo(city: str, limit: int = 200):
    return []

async def fetch_immovlan(city: str, limit: int = 200):
    return []

async def fetch_notaire(city: str, limit: int = 200):
    return []

async def run_fetch(source: str, city: str, limit: int):
    if source == "immoweb":
        return await fetch_immoweb(city, limit)
    if source == "zimmo":
        return await fetch_zimmo(city, limit)
    if source == "immovlan":
        return await fetch_immovlan(city, limit)
    if source == "notaire":
        return await fetch_notaire(city, limit)
    raise ValueError("Source inconnue")

def upsert_listings(rows: list[Listing]):
    if not rows:
        return
    con.execute("INSERT OR REPLACE INTO listings SELECT * FROM rows", {"rows": rows})

def fetch(source: str, city: str, limit: int):
    rows = asyncio.run(run_fetch(source, city, limit))
    upsert_listings(rows)
