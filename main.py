from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from models import Movie

app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"


movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": 2009,
        "rating": 7.8,
        "category": "Acción",
    },
    {
        "id": 2,
        "title": "Shawshank Redemption",
        "overview": "En un espacio...",
        "year": 1994,
        "rating": 9.8,
        "category": "Aventura",
    },
]


@app.get("/", tags=["home"])  # ruta de inicio
def message():
    return HTMLResponse("<h1>Hellow world</h1>")


@app.get("/movies", tags=["movies"])
def get_movies():
    return movies


@app.get("/movies/{id}", tags=["movies"])
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []


@app.get("/movies/", tags=["movies"])  #  si terminar así es una query
def get_by_category(category: str, year: int):
    return [
        item for item in movies if item["category"] == category
    ]  # aqui no se está usando year


@app.post("/movies/", tags=["movies"])  #  si terminar así es una query
def create_movie(movie: Movie):
    movies.append(movie)
    return movies


# Este el método que se utiliza para modificar
@app.put("/movies/{id}", tags=["movies"])
def update_movie(id: int, movie: Movie):
    for item in movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["category"] = movie.category
            item["rating"] = movie.rating
            item["year"] = movie.year
    return movies


@app.delete("/movies/{id}", tags=["movies"])
def delete_movie(
    id: int,
):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
    return movies
