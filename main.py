from fastapi import Body, FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"


movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overvie    w": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
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
def create_movie(
    id: int = Body(),
    title: str = Body(),
    overview: str = Body(),
    category: str = Body(),
    rating: float = Body(),
    year: int = Body(),
):
    movies.append(
        {
            "id": id,
            "title": title,
            "overview": overview,
            "year": year,
            "rating": rating,
            "category": category,
        },
    )
    return movies


# Este el método que se utiliza para modificar
@app.put("/movies/{id}", tags=["movies"])
def update_movie(
    id: int,
    title: str = Body(),
    overview: str = Body(),
    category: str = Body(),
    rating: float = Body(),
    year: int = Body(),
):
    for item in movies:
        if item["id"] == id:
            item["title"] = title
            item["overview"] = overview
            item["category"] = category
            item["rating"] = rating
            item["year"] = year
    return movies


@app.delete("/movies/{id}", tags=["movies"])
def delete_movie(
    id: int,
):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
    return movies
