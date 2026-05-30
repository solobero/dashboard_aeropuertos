from __future__ import annotations

import numpy as np
import pandas as pd

from src.tokens import CONNECTIVITY_METRICS, CLIMATE_METRICS, LAYER_CONFIGS


STATIC_COLS = [
    "icao_code",
    "name",
    "type",
    "municipality",
    "region_name",
    "iata_code",
    "latitude_deg",
    "longitude_deg",
    "elevation_ft",
    "scheduled_service",
]

SUM_COLS = [
    "operaciones_llegada",
    "operaciones_salida",
    "operaciones_otras",
    "operaciones_total",
    "pasajeros_salida",
    "pasajeros_llegada",
    "pasajeros_total",
    "carga_salida_kg",
    "carga_llegada_kg",
    "carga_total_kg",
    "n_metar_mes",
]

MEAN_COLS = [
    "n_destinos_total",
    "n_origenes_total",
    "n_empresas_salida",
    "n_empresas_llegada",
    "temp_media_c",
    "humedad_media_pct",
    "viento_medio_kt",
    "viento_max_kt",
    "visibilidad_media_sm",
    "visibilidad_min_sm",
    "prop_lluvia",
    "prop_tormenta",
    "prop_niebla",
    "prop_baja_visibilidad",
    "prop_viento_fuerte",
    "prop_rafaga",
    "prop_ifr_aprox",
    "cobertura_metar_ratio",
]


def apply_filters(
    df: pd.DataFrame,
    start_date,
    end_date,
    region: str,
    airport_type: str,
) -> pd.DataFrame:
    """Filtra el dataset por periodo, región y tipo de aeropuerto."""
    mask = (df["fecha_mes"] >= pd.to_datetime(start_date)) & (df["fecha_mes"] <= pd.to_datetime(end_date))
    if region != "Todas":
        mask &= df["region_name"].fillna("Sin región").eq(region)
    if airport_type != "Todos":
        mask &= df["type"].fillna("Sin tipo").eq(airport_type)
    return df.loc[mask].copy()


def resolve_metric(active_layer: str, submetric: str | None = None) -> tuple[str, str, str, str]:
    """Devuelve columna, etiqueta, unidad y regla de agregación para la capa activa."""
    cfg = LAYER_CONFIGS[active_layer]
    if active_layer == "clima" and submetric:
        column = CLIMATE_METRICS[submetric]
        return column, submetric, "%", "mean"
    if active_layer == "conectividad" and submetric:
        column = CONNECTIVITY_METRICS[submetric]
        if "origen" in column:
            unit = "orígenes"
        elif "empresa" in column:
            unit = "empresas"
        else:
            unit = "destinos"
        return column, submetric, unit, "mean"
    return cfg["metric"], cfg["display"], cfg["unit"], cfg["agg"]


def build_airport_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Agrega el dataset aeropuerto-mes a una fila por aeropuerto."""
    if df.empty:
        return pd.DataFrame(columns=STATIC_COLS)

    agg_spec = {}
    for col in STATIC_COLS:
        if col != "icao_code" and col in df.columns:
            agg_spec[col] = "first"
    for col in SUM_COLS:
        if col in df.columns:
            agg_spec[col] = "sum"
    for col in MEAN_COLS:
        if col in df.columns:
            agg_spec[col] = "mean"

    airport_df = df.groupby("icao_code", as_index=False).agg(agg_spec)

    # Normaliza coordenadas y campos principales.
    airport_df["latitude_deg"] = pd.to_numeric(airport_df["latitude_deg"], errors="coerce")
    airport_df["longitude_deg"] = pd.to_numeric(airport_df["longitude_deg"], errors="coerce")
    airport_df = airport_df.dropna(subset=["latitude_deg", "longitude_deg"])

    # Métrica auxiliar para vista ejecutiva de conectividad.
    for col in CONNECTIVITY_METRICS.values():
        if col not in airport_df.columns:
            airport_df[col] = 0
    airport_df["conectividad_compuesta"] = airport_df[list(CONNECTIVITY_METRICS.values())].fillna(0).sum(axis=1)
    return airport_df


def build_global_summary(airport_df: pd.DataFrame, metric_col: str, agg_rule: str) -> dict:
    """Construye indicadores globales para la vista actual."""
    if airport_df.empty or metric_col not in airport_df.columns:
        return {"total": 0, "leader": None, "n_airports": 0}

    values = airport_df[metric_col].fillna(0)
    total = values.mean() if agg_rule == "mean" else values.sum()
    leader_idx = values.idxmax() if len(values) else None
    leader = airport_df.loc[leader_idx].to_dict() if leader_idx is not None else None
    return {"total": total, "leader": leader, "n_airports": int(airport_df["icao_code"].nunique())}


def nearest_airport(airport_df: pd.DataFrame, lat: float, lng: float) -> str | None:
    """Obtiene el aeropuerto más cercano a unas coordenadas clicadas en el mapa."""
    if airport_df.empty:
        return None
    distances = np.sqrt((airport_df["latitude_deg"] - lat) ** 2 + (airport_df["longitude_deg"] - lng) ** 2)
    nearest_idx = distances.idxmin()
    if distances.loc[nearest_idx] <= 0.8:
        return str(airport_df.loc[nearest_idx, "icao_code"])
    return None


def build_timeseries(df: pd.DataFrame, metric_col: str, agg_rule: str, selected_icao: str | None = None) -> pd.DataFrame:
    """Construye serie temporal nacional o de un aeropuerto seleccionado."""
    if df.empty or metric_col not in df.columns:
        return pd.DataFrame(columns=["fecha_mes", "valor"])
    working = df.copy()
    if selected_icao:
        working = working[working["icao_code"].eq(selected_icao)]
    if working.empty:
        return pd.DataFrame(columns=["fecha_mes", "valor"])

    if agg_rule == "mean":
        series = working.groupby("fecha_mes", as_index=False)[metric_col].mean()
    else:
        series = working.groupby("fecha_mes", as_index=False)[metric_col].sum()
    series = series.rename(columns={metric_col: "valor"})
    return series.sort_values("fecha_mes")
