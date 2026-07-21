from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Product:
    name: str
    price: float
    currency: str
    image_url: str
    product_url: str
    source: str
    product_id: Optional[str] = None
    rating: Optional[float] = None
    review_count: Optional[int] = None
    seller: Optional[str] = None
    category: Optional[str] = None
    discovered_at: Optional[datetime] = None

    def __post_init__(self):
        if self.discovered_at is None:
            self.discovered_at = datetime.now()