from pydantic import BaseModel

class Movie(BaseModel):
    id: int
    title: str
    overview: str
    release_date: str
    rating: float
    category: str