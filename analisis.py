import pandas as pd

# Paso 3.1: Cargar CSV
df = pd.read_csv("pronostico_huancayo.csv")
df["fecha"] = pd.to_datetime(df["fecha"])

print("--- Primeras filas ---")
print(df.head())
print("\n--- Información del DataFrame ---")
print(df.info())

# Paso 3.2: Transformación de datos
df["amplitud_termica"] = df["temp_max"] - df["temp_min"]
df["dia_lluvioso"] = df["precipitacion"] > 0
df["categoria"] = df["temp_max"].apply(
    lambda t: "cálido" if t >= 20 else ("templado" if t >= 15 else "frío")
)

print("\n--- DataFrame Transformado ---")
print(df)
print("\n--- Descripción Estadística ---")
print(df.describe())

# Paso 3.3: Agregaciones
resumen = df.groupby("categoria").agg(
    dias=("categoria", "count"),
    temp_max_promedio=("temp_max", "mean"),
    precipitacion_total=("precipitacion", "sum"),
)

print("\n--- Resumen por Categoría ---")
print(resumen)

# Paso 3.4: Exportación de resultados
df.to_csv("pronostico_huancayo_procesado.csv", index=False)
resumen.to_csv("resumen_por_categoria.csv")
## Flujo de datos — Semana 2

Esta sección documenta el pipeline de datos construido en la Semana 2 (Librerías para Datos y Automatización).

**Fuente:** API pública Open-Meteo (`https://api.open-meteo.com/v1/forecast`), sin necesidad de clave de acceso. Se consulta el pronóstico de 7 días para Huancayo (latitud -12.07, longitud -75.21): temperatura máxima, temperatura mínima y precipitación diaria.

**Transformación:**
1. `clima.py` consume la API con `requests` (timeout de 5s y manejo de excepciones) y guarda la respuesta cruda en `pronostico_huancayo.json`.
2. La misma respuesta se convierte a `pronostico_huancayo.csv` con el módulo estándar `csv`.
3. `analisis.py` carga el CSV en un DataFrame de Pandas, agrega las columnas derivadas `amplitud_termica`, `dia_lluvioso` y `categoria` (frío/templado/cálido), y calcula un resumen agrupado por categoría con `groupby`.

**Salida:**
- `pronostico_huancayo.json` — respuesta cruda de la API (trazabilidad del dato original).
- `pronostico_huancayo.csv` — datos tabulares sin procesar.
- `pronostico_huancayo_procesado.csv` — datos con las columnas derivadas.
- `resumen_por_categoria.csv` — agregación por categoría de temperatura.

**Cómo reproducirlo:**
```bash
python clima.py
python analisis.py
```