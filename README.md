# AeroDatos Colombia — herramienta interactiva de aeropuertos

Herramienta Streamlit para explorar el dataset `monthly_airport_model_dataset.csv` mediante un mapa interactivo de aeropuertos colombianos.

## Enfoque

Esta versión evita métricas de modelo y se concentra únicamente en el dataset:

- Operación
- Pasajeros
- Carga
- Conectividad
- Clima observado desde variables METAR

La interacción principal es hacer clic sobre aeropuertos en el mapa. Al seleccionar un aeropuerto, se abre un panel contextual con indicadores operativos, pasajeros, carga y señales meteorológicas.

## Estructura

```text
aerodatos_colombia_streamlit/
├── app.py
├── data/
│   └── monthly_airport_model_dataset.csv
├── src/
│   ├── aggregations.py
│   ├── config.py
│   ├── data_loader.py
│   ├── formatting.py
│   ├── state.py
│   ├── styles.py
│   ├── tokens.py
│   ├── charts/
│   │   └── trend.py
│   ├── maps/
│   │   └── folium_map.py
│   ├── ui/
│   │   ├── components.py
│   │   ├── filters.py
│   │   └── icons.py
│   └── views/
│       └── map_explorer.py
├── requirements.txt
└── .streamlit/
    └── config.toml
```

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecución

```bash
streamlit run app.py
```

## Notas de diseño

- El mapa usa `folium` + `streamlit-folium` para permitir clics sobre aeropuertos.
- La capa visual base usa `CartoDB positron`, que es limpia y adecuada para dashboards ejecutivos.
- Google Maps no se usa en esta primera versión para evitar API keys, costos por uso y complejidad de callbacks en Streamlit. Puede agregarse como proveedor de mapa en una segunda fase.
