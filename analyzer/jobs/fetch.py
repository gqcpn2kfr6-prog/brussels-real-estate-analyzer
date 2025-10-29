import asyncio
from ..db import con
from ..models import Listing
from ..sources import fetch_immoweb_async

async def run_fetch(source: str, city: str, limit: int):
    if source == "immoweb":
        return await fetch_immoweb_async(city, limit)
    raise ValueError("Source inconnue")

def upsert_listings(rows: list[Listing]):
    if not rows:
        return
    con.execute("INSERT OR REPLACE INTO listings SELECT * FROM rows", {"rows": rows})

def fetch(source: str, city: str, limit: int):
    rows = asyncio.run(run_fetch(source, city, limit))
    upsert_listings(rows)
