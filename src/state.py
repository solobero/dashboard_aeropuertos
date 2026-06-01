from __future__ import annotations

import streamlit as st


DEFAULT_LAYER = "operacion"


def init_state() -> None:
    """Inicializa las variables persistentes de la aplicación."""

    if "show_landing" not in st.session_state:
        st.session_state["show_landing"] = True

    if "active_layer" not in st.session_state:
        st.session_state["active_layer"] = DEFAULT_LAYER

    if "selected_icao" not in st.session_state:
        st.session_state["selected_icao"] = None


def enter_dashboard() -> None:
    """Entra desde la landing page hacia el mapa interactivo."""

    st.session_state["show_landing"] = False


def go_to_landing() -> None:
    """Regresa a la landing page."""

    st.session_state["show_landing"] = True


def set_active_layer(layer_key: str) -> None:
    """
    Cambia la capa activa sin borrar el aeropuerto seleccionado.

    Esto permite que, si el usuario selecciona un aeropuerto y luego cambia
    de Operación a Pasajeros, Carga, Conectividad o Clima, el dashboard
    conserve el mismo aeropuerto como foco de análisis.
    """

    st.session_state["active_layer"] = layer_key


def set_selected_airport(icao_code: str | None) -> None:
    """Actualiza el aeropuerto seleccionado en el mapa."""

    st.session_state["selected_icao"] = icao_code


def clear_selected_airport() -> None:
    """Limpia manualmente el aeropuerto seleccionado."""

    st.session_state["selected_icao"] = None