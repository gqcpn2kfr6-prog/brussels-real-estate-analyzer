from pydantic import BaseModel, Field, HttpUrl
from typing import Optional

class Listing(BaseModel):
    id: str
    source: str
    title: str
    price: float
    currency: str = "EUR"
    city: str
    commune: Optional[str] = None
    district: Optional[str] = None
    address: Optional[str] = None
    rooms: Optional[int] = None
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    area: Optional[float] = None
    floor: Optional[int] = None
    type: Optional[str] = None
    url: HttpUrl
