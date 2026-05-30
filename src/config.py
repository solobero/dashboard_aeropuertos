from pathlib import Path

# Carpeta raíz del proyecto. Se calcula desde este archivo para evitar rutas absolutas.
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Archivo principal de datos. Debe permanecer dentro de data/.
DATA_PATH = PROJECT_ROOT / "data" / "monthly_airport_model_dataset.csv"

# Configuración visual de la página Streamlit.
PAGE_CONFIG = {
    "page_title": "AeroDatos Colombia",
    "page_icon": "✈️",
    "layout": "wide",
    "initial_sidebar_state": "collapsed",
}

# Centro geográfico aproximado para visualizar Colombia.
COLOMBIA_CENTER = [4.5709, -74.2973]

# Zoom inicial recomendado para ver Colombia completa.
DEFAULT_ZOOM = 6

# Alto del mapa principal en píxeles.
MAP_HEIGHT = 690
