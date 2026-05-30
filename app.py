import streamlit as st

from src.config import PAGE_CONFIG
from src.data_loader import load_dataset
from src.state import init_state
from src.styles import apply_styles
from src.views.landing import render_landing
from src.views.map_explorer import render_map_explorer


# Configura Streamlit antes de renderizar cualquier elemento.
st.set_page_config(**PAGE_CONFIG)

# Aplica estilos CSS globales para mantener consistencia visual.
apply_styles()

# Inicializa estado de capa activa, aeropuerto seleccionado y submétricas.
init_state()

# Carga el dataset real de aeropuerto-mes con cache para mejorar rendimiento.
dataset = load_dataset()

# Controla la navegación interna sin enlaces HTML, sin query params y sin abrir pestañas nuevas.
if st.session_state.get("show_landing", True):
    render_landing()
else:
    # Renderiza la herramienta interactiva principal basada en mapa y clicks.
    render_map_explorer(dataset)
