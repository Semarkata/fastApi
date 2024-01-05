from fastapi import FastAPI, Body
from http import HTTPStatus as http_response
import mockdata

app = FastAPI(
    title='Fast Api',
    description='My Fast Api project',
    version='0.0.1',
)

@app.get('/', tags=['Root'])
def read_root():
    return {"Hello": "World"}

@app.get('/movies', tags=['Movies'])
def get_movies():
    return mockdata.movies

@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int):
    for movie in mockdata.movies:
        if movie['id'] == id:
            return movie
    return 'No Movie Found'

@app.get('/movies/', tags=['Movies'])
def get_movies_by_category(category: str):
    for movie in mockdata.movies:
        if movie['category'] == category:
            return movie
    return 'No Movie Found'

@app.post('/movies', tags=['Movies'])
def create_movie(
        id: int = Body(),
        title: str = Body(),
        overview: str = Body(),
        release_date: str = Body(),
        rating: float = Body(),
        category: str = Body(),
):
    mockdata.movies.append({
        'id': id,
        'title': title,
        'overview': overview,
        'release_date': release_date,
        'rating': rating,
        'category': category
    })
    return http_response.CREATED

@app.put('/movies/{id}', tags=[''])
def update_movie(
        id: int,
        title: str = Body(),
        overview: str = Body(),
        release_date: str = Body(),
        rating: float = Body(),
        category: str = Body(),
):
    for movie in mockdata.movies:
        if movie['id'] == id:
            movie['title'] = title
            movie['overview'] = overview
            movie['release_date'] = release_date
            movie['rating'] = rating
            movie['category'] = category
            return http_response.OK
        else:
            return http_response.NOT_FOUND

@app.delete('/movies/{id}', tags=[''])
def delete_movie(id:int):
    for movie in mockdata.movies:
        if movie['id'] == id:
            mockdata.movies.remove(movie)
            return http_response.OK
        else:
            return http_response.NOT_FOUND
