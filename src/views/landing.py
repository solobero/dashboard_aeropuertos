from __future__ import annotations

import base64
from pathlib import Path

import streamlit as st

from src.ui.icons import svg_icon
from src.state import enter_dashboard


ASSET_PATH = Path(__file__).resolve().parents[1] / "assets" / "landing_air_operations.svg"


def _asset_data_uri(path: Path) -> str:
    """Convierte el SVG local de portada en una URI embebida."""
    raw = path.read_bytes()
    encoded = base64.b64encode(raw).decode("utf-8")
    return f"data:image/svg+xml;base64,{encoded}"


def render_landing() -> None:
    """Renderiza una portada inicial centrada verticalmente."""
    image_uri = _asset_data_uri(ASSET_PATH)
    brand_icon = svg_icon("plane", "white", 22)

    st.markdown("<div class='ad-landing-spacer'></div>", unsafe_allow_html=True)
    left_col, right_col = st.columns([0.95, 1.25], gap="large", vertical_alignment="center")

    with left_col:
        st.markdown(
            f"""
            <section class="ad-landing-copy-only">
                <div class="ad-brand ad-landing-brand">
                    <div class="ad-logo">{brand_icon}</div>
                    <div>AeroDatos <span>Colombia</span></div>
                </div>
                <div class="ad-landing-kicker">Proyecto integrador · Aeropuertos Colombia</div>
                <h1 class="ad-landing-title">Radiografía operacional y meteorológica de aeropuertos en Colombia</h1>
                <div class="ad-landing-subtitle">Exploración visual de operaciones, pasajeros, carga, conectividad y METAR entre 2020 y 2025. Incluye el choque COVID-19 y la recuperación posterior.</div>
            </section>
            """,
            unsafe_allow_html=True,
        )
        st.button(
            "Entrar al mapa interactivo",
            key="landing_enter_button",
            type="primary",
            use_container_width=False,
            on_click=enter_dashboard,
        )

    with right_col:
        st.markdown(
            f"""
            <div class="ad-landing-image">
                <img src="{image_uri}" alt="Operaciones aéreas en Colombia" />
            </div>
            """,
            unsafe_allow_html=True,
        )
