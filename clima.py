import requests
import json
import csv

URL = "https://api.open-meteo.com/v1/forecast"
PARAMETROS = {
    "latitude": -12.07,  # Huancayo
    "longitude": -75.21,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "America/Lima",
    "forecast_days": 7,
}

try:
    respuesta = requests.get(URL, params=PARAMETROS, timeout=5)
    respuesta.raise_for_status()
    datos = respuesta.json()
except requests.exceptions.RequestException as error:
    raise SystemExit(f"No se pudo obtener el pronóstico: {error}")

# Mostrar una vista previa en la consola
print(json.dumps(datos["daily"], indent=2, ensure_ascii=False))

# 1. Guardar la respuesta cruda en formato JSON (Paso 2.4 de la guía)
with open("pronostico_huancayo.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, ensure_ascii=False, indent=2)

# 2. Construir y guardar el archivo CSV (Paso 2.4 de la guía)
diario = datos["daily"]
filas = zip(
    diario["time"],
    diario["temperature_2m_max"],
    diario["temperature_2m_min"],
    diario["precipitation_sum"],
)

with open("pronostico_huancayo.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["fecha", "temp_max", "temp_min", "precipitacion"])
    escritor.writerows(filas)

print("¡Archivos 'pronostico_huancayo.json' y 'pronostico_huancayo.csv' generados con éxito!")