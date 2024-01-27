from typing import Optional

from pydantic import BaseModel


class Movie(BaseModel):
    id: Optional[int]
    title: str
    overview: str
    year: int
    rating: float
    category: str
