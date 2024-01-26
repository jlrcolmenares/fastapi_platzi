# Apuntes del curso 

## Clase 1
- Ejecutar la aplicación de FastAPI indicando el puerto: `uvicorn main:app --reload --port=5000`
- Ejecutar la aplicación para que esté disponible para que acceder desde el movil (dispositivos conectados a tu red): `uvicorn main:app --reload --port=5000 --host=0.0.0.0`

## Clase 2
- Acceder a la documentacion por medio de endpoint de la aplicación + docs/: `http://127.0.0.1:5000/docs`
- El título de la app es el titulo de la docs, también la documentaicón es importante, y los tags indican el título de los puntos de acceso que vas creando en la API

## Clase 3
- FastAPI puede retornar muchas cosas. Por ejemplo, si agregamos el módulo de HTMLResponse podemos returnar código HTML como una página web
- 