from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"

@app.get('/', tags=['home']) #ruta de inicio
def message():
    return HTMLResponse('<h1>Hellow world</h1>')