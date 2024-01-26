from fastapi import FastAPI

app = FastAPI()

@app.get('/') #ruta de inicio
def message():
    return "Hello World"