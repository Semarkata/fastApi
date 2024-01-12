from pydantic import BaseModel, Field

class Movie(BaseModel):
    id: int
    title: str = Field(default='Title', min_length=2, max_length=60)
    overview: str = Field(default='Overview')
    release_date: str = Field(default='01-01-1990')
    rating: float = Field(default=7.5)
    category: str = Field(default='Category')