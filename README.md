# Apuntes del curso
- La API Rest es un reflejo de lo que hay en la base de datos pero aplicándole estructurando los datos de otra manera

## Clase 2
- Ejecutar la aplicación de FastAPI indicando el puerto: `uvicorn main:app --reload --port=5000`
- Ejecutar la aplicación para que esté disponible para que acceder desde el movil (dispositivos conectados a tu red): `uvicorn main:app --reload --port=5000 --host=0.0.0.0`

## Clase 3
- Acceder a la documentacion por medio de endpoint de la aplicación + docs/: `http://127.0.0.1:5000/docs`
- El título de la app es el titulo de la docs, también la documentaicón es importante, y los tags indican el título de los puntos de acceso que vas creando en la API. Los tags sirven para agrupar puntos

## Clase 5
- FastAPI puede retornar muchas cosas. Por ejemplo, si agregamos el módulo de HTMLResponse podemos returnar código HTML como una página web

# Clase 6
- Agregamos tipos en la defincion de las funciones de los endpoints podemos correr validaciones de los strings

# Clase 8
- Si importamos el método Body() de FastAPI podemos pasar multiples argumentos como un único request en docs de la API

# Clase 10
- Puede correr validaciones de schemas utilizando PyDantic, una librería incluída en FastAPI. Al declarara el BaseModel podemos utilizarlo como argumento de entrada para la funciones.
- Creo entender que Pydantic lo que hace es convertir las clases que tenemos en diccionarios, y aplicar validaciones sobre aquellos campos que hemos creado
