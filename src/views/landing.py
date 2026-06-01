from __future__ import annotations

import base64
from pathlib import Path

import streamlit as st

from src.ui.components import render_landing_brand


def _enter_dashboard() -> None:
    """Cambia de la portada inicial al mapa interactivo."""

    st.session_state["show_landing"] = False


def _get_asset_path(filename: str) -> Path:
    """Construye una ruta portable hacia un archivo dentro de src/assets."""

    src_dir = Path(__file__).resolve().parents[1]
    assets_dir = src_dir / "assets"

    return assets_dir / filename


def _image_as_data_uri(filename: str) -> str | None:
    """Convierte una imagen local en data URI para insertarla en HTML."""

    image_path = _get_asset_path(filename)

    if not image_path.exists():
        return None

    suffix = image_path.suffix.lower()

    if suffix == ".svg":
        mime_type = "image/svg+xml"
    elif suffix in {".jpg", ".jpeg"}:
        mime_type = "image/jpeg"
    elif suffix == ".png":
        mime_type = "image/png"
    else:
        mime_type = "application/octet-stream"

    encoded_image = base64.b64encode(image_path.read_bytes()).decode("utf-8")

    return f"data:{mime_type};base64,{encoded_image}"


def render_landing() -> None:
    """Renderiza la portada inicial del proyecto."""

    image_uri = _image_as_data_uri("landing_air_operations.svg")

    st.markdown(
        "<div class='ad-landing-spacer'></div>",
        unsafe_allow_html=True,
    )

    left_col, right_col = st.columns(
        [0.95, 1.25],
        gap="large",
        vertical_alignment="center",
    )

    with left_col:
        st.markdown(
            "<div class='ad-landing-copy-only'>",
            unsafe_allow_html=True,
        )

        render_landing_brand()

        st.markdown(
            """
            <div class="ad-landing-kicker">
                Proyecto integrador · Aeropuertos Colombia
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <h1 class="ad-landing-title">
                Radiografía operacional y meteorológica de aeropuertos en Colombia
            </h1>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="ad-landing-subtitle">
                Exploración visual de operaciones, pasajeros, carga, conectividad y condiciones METAR entre 2020 y 2025.
                Incluye el choque COVID-19 y la recuperación posterior.
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.button(
            "Entrar al mapa interactivo",
            key="landing_enter_button",
            type="primary",
            on_click=_enter_dashboard,
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True,
        )

    with right_col:
        if image_uri:
            st.markdown(
                f"""
                <div class="ad-landing-image">
                    <img src="{image_uri}" alt="Operaciones aéreas en Colombia">
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
                <div class="ad-landing-image ad-landing-image-fallback">
                    <div>
                        <strong>Operaciones aéreas</strong>
                        <span>Mapa · datos · clima</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )