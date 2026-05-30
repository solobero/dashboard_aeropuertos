from __future__ import annotations

import pandas as pd
import streamlit as st

from src.config import DATA_PATH
from src.tokens import MODEL_COLUMNS_TO_HIDE


REQUIRED_COLUMNS = {
    "icao_code",
    "fecha_mes",
    "name",
    "type",
    "municipality",
    "region_name",
    "latitude_deg",
    "longitude_deg",
    "operaciones_total",
    "pasajeros_total",
    "carga_total_kg",
    "n_destinos_total",
    "n_origenes_total",
    "n_empresas_salida",
    "n_empresas_llegada",
    "prop_lluvia",
    "prop_niebla",
    "prop_tormenta",
    "prop_baja_visibilidad",
    "viento_medio_kt",
    "visibilidad_media_sm",
    "cobertura_metar_ratio",
}


@st.cache_data(show_spinner="Cargando dataset aeroportuario...")
def load_dataset(path: str = str(DATA_PATH)) -> pd.DataFrame:
    """Carga el dataset mensual aeropuerto-mes y aplica validaciones mínimas."""
    df = pd.read_csv(path)
    missing = REQUIRED_COLUMNS.difference(df.columns)
    if missing:
        raise ValueError(f"Faltan columnas requeridas en el dataset: {sorted(missing)}")

    df = df.copy()
    df["fecha_mes"] = pd.to_datetime(df["fecha_mes"], errors="coerce")
    df = df.dropna(subset=["fecha_mes", "latitude_deg", "longitude_deg", "icao_code"])

    # La herramienta es descriptiva. Se eliminan columnas del modelo para evitar mezclarlas en vistas ejecutivas.
    columns_to_keep = [col for col in df.columns if col not in MODEL_COLUMNS_TO_HIDE]
    return df[columns_to_keep]
