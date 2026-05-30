import streamlit as st


def init_state() -> None:
    """Inicializa variables de sesión para controlar capa, selección y submétricas."""
    st.session_state.setdefault("active_layer", "operacion")
    st.session_state.setdefault("selected_icao", None)
    st.session_state.setdefault("climate_metric", "Lluvia")
    st.session_state.setdefault("connectivity_metric", "Destinos")
    st.session_state.setdefault("show_landing", True)


def set_active_layer(layer_key: str) -> None:
    """Actualiza la capa activa sin borrar la selección de aeropuerto."""
    st.session_state["active_layer"] = layer_key


def set_selected_airport(icao_code: str | None) -> None:
    """Actualiza el aeropuerto seleccionado por clic en mapa o por control manual."""
    st.session_state["selected_icao"] = icao_code


def enter_dashboard() -> None:
    """Abre la herramienta principal sin depender de enlaces ni query params."""
    st.session_state["show_landing"] = False

def show_landing_page() -> None:
    """Devuelve explícitamente a la portada. No se usa en el logo del encabezado."""
    st.session_state["show_landing"] = True
