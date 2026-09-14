## Flujo de datos - Semana 2

**Fuente:** API pública Open-Meteo (`https://api.open-meteo.com/v1/forecast`), sin necesidad de clave de acceso. Se consulta el pronóstico de 7 días para Huancayo (latitud -12.07, longitud -75.21): temperatura máxima, temperatura mínima y precipitación diaria[cite: 1].

**Transformación:**
1. `clima.py` consume la API con `requests` (timeout de 5s y manejo de excepciones) y guarda la respuesta cruda en `pronostico_huancayo.json`[cite: 1].
2. La misma respuesta se convierte a `pronostico_huancayo.csv` con el módulo estándar `csv`[cite: 1].
3. `analisis.py` carga el CSV en un DataFrame de Pandas, agrega las columnas derivadas `amplitud_termica`, `dia_lluvioso` y `categoria` (frío/templado/cálido), y calcula un resumen agrupado por categoría con `groupby`[cite: 1].

**Salida:**
- `pronostico_huancayo.json` — respuesta cruda de la API (trazabilidad del dato original)[cite: 1].
- `pronostico_huancayo.csv` — datos tabulares sin procesar[cite: 1].
- `pronostico_huancayo_procesado.csv` — datos con las columnas derivadas[cite: 1].
- `resumen_por_categoria.csv` — agregación por categoría de temperatura[cite: 1].

**Cómo reproducirlo:**
```bash
python numpy_demo.py
python clima.py
python analisis.py