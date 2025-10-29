import asyncio
from typing import List
from ..models import Listing
from .immoweb_api import search_immoweb

async def fetch_immoweb_async(city: str, limit: int) -> List[Listing]:
    return await search_immoweb(city=city, limit=limit)
