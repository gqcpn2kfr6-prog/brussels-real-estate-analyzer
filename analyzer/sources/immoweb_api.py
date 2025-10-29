import httpx
from typing import Any, Dict, List
from ..models import Listing
from .constants import IMMOWEB_BASE, SEARCH_ENDPOINT, HEADERS

# Note: Les endpoints exacts peuvent évoluer. Adapter aux schémas actuels d'Immoweb.

async def search_immoweb(city: str, limit: int = 200) -> List[Listing]:
    query = {
        "offer": {"type": "FOR_SALE"},
        "property": {"type": ["APARTMENT","FLAT_STUDIO","HOUSE"]},
        "page": 1,
        "pageSize": min(limit, 200),
        "filters": {"regions": [city]},
    }
    async with httpx.AsyncClient(headers=HEADERS, timeout=30) as client:
        # Immoweb expose des APIs JSON pour la recherche; en cas de blocage, basculer vers Playwright.
        url = f"{IMMOWEB_BASE}{SEARCH_ENDPOINT}"
        r = await client.post(url, json=query)
        r.raise_for_status()
        data = r.json()
    listings: List[Listing] = []
    for item in data.get("results", []):
        try:
            listings.append(Listing(
                id=str(item.get("id")),
                source="immoweb",
                title=item.get("title") or "Annonce Immoweb",
                price=float(item.get("price", {}).get("value")),
                currency=item.get("price", {}).get("currency", "EUR"),
                city=item.get("location", {}).get("locality", city),
                commune=item.get("location", {}).get("municipality"),
                district=item.get("location", {}).get("district"),
                address=item.get("location", {}).get("street"),
                rooms=item.get("property", {}).get("rooms"),
                bedrooms=item.get("property", {}).get("bedrooms"),
                bathrooms=item.get("property", {}).get("bathrooms"),
                area=float(item.get("property", {}).get("netHabitableSurface") or 0) or None,
                floor=item.get("property", {}).get("floor"),
                type=item.get("property", {}).get("type"),
                url=item.get("webUrl") or f"https://www.immoweb.be/fr/annonce/{item.get('id')}",
            ))
        except Exception:
            continue
    return listings
