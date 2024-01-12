from fastapi import FastAPI, Body
from http import HTTPStatus as http_response
import mockdata
from model.movie import Movie

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
def create_movie(movie: Movie):
    mockdata.movies.append(movie)

    return http_response.CREATED

@app.put('/movies/{id}', tags=[''])
def update_movie(movie_id: int, movie: Movie):
    for internal_movie in mockdata.movies:
        if internal_movie['id'] == movie_id:
            internal_movie['title'] = movie.title
            internal_movie['overview'] = movie.overview
            internal_movie['release_date'] = movie.release_date
            internal_movie['rating'] = movie.rating
            internal_movie['category'] = movie.category
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
