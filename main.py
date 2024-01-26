from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"


movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]

@app.get('/', tags=['home']) #ruta de inicio
def message():
    return HTMLResponse('<h1>Hellow world</h1>')

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies