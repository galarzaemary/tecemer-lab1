import requests
try:
 respuesta = requests.get(
 "https://official-joke-api.appspot.com/random_joke", timeout=5
 )
 respuesta.raise_for_status()
 datos = respuesta.json()
 print(datos["setup"])
 print(datos["punchline"])
except requests.RequestException as error:
 print(f"No se pudo obtener el chiste: {error}")