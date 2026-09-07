import requests

respuesta = requests.get("https://official-joke-api.appspot.com/random_joke")
datos = respuesta.json()
print(datos["setup"])
print(datos["punchline"])
