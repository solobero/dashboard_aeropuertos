from __future__ import annotations

import folium
import pandas as pd
from branca.element import Element

from src.config import COLOMBIA_CENTER, DEFAULT_ZOOM
from src.formatting import format_metric, unit_display_name
from src.labels import display_region
from src.tokens import LAYER_CONFIGS, VALUE_SCALE_COLORS


def _scale_radius(values: pd.Series, min_radius: float = 5.0, max_radius: float = 22.0) -> pd.Series:
    """Escala valores numéricos a radios de burbuja aptos para el mapa."""
    cleaned = values.fillna(0).clip(lower=0)
    if cleaned.max() == cleaned.min():
        return pd.Series([10.0] * len(cleaned), index=cleaned.index)
    sqrt_values = cleaned.pow(0.5)
    scaled = min_radius + (sqrt_values - sqrt_values.min()) / (sqrt_values.max() - sqrt_values.min()) * (max_radius - min_radius)
    return scaled.fillna(min_radius)


def _normalized_value(value: float | None, min_value: float, max_value: float) -> float | None:
    """Normaliza un valor entre 0 y 1 para clasificar color."""
    if value is None or pd.isna(value):
        return None
    if max_value <= min_value:
        return 1.0
    return max(0.0, min(1.0, (float(value) - min_value) / (max_value - min_value)))


def _value_color(value: float | None, low_threshold: float, high_threshold: float) -> str:
    """Color para magnitudes no meteorológicas: rojo bajo, amarillo medio, verde alto.

    Usa terciles de la vista filtrada para que el color sea legible incluso cuando
    hay aeropuertos muy dominantes como Bogotá.
    """
    if value is None or pd.isna(value):
        return VALUE_SCALE_COLORS["missing"]
    if float(value) >= high_threshold:
        return VALUE_SCALE_COLORS["high"]
    if float(value) >= low_threshold:
        return VALUE_SCALE_COLORS["mid"]
    return VALUE_SCALE_COLORS["low"]


def _climate_color(value: float | None) -> str:
    """Asigna color a proporciones meteorológicas crudas: 0.12 equivale a 12 %."""
    if value is None or pd.isna(value):
        return "#94A3B8"
    if value < 0.03:
        return "#60A5FA"
    if value < 0.08:
        return "#22C55E"
    if value < 0.15:
        return "#F59E0B"
    return "#EF4444"


def _tooltip_html(row: pd.Series, metric_col: str, metric_label: str, unit: str) -> str:
    """Construye tooltip corto para hover sobre aeropuertos."""
    unit_label = unit_display_name(unit)
    return f"""
    <div style="font-family: Inter, Arial; min-width: 190px;">
        <b>{row.get('municipality', 'Aeropuerto')} ({row.get('icao_code', '')})</b><br>
        <span style="color:#64748B;">{row.get('name', '')}</span><br>
        <span style="color:#64748B;">{display_region(row.get('region_name'))}</span><br>
        <hr style="border:0;border-top:1px solid #E2E8F0;margin:6px 0;">
        {metric_label}: <b>{format_metric(row.get(metric_col), unit)}</b><br>
        <span style="color:#64748B;font-size:11px;">Unidad: {unit_label}</span>
    </div>
    """


def _add_value_legend(fmap: folium.Map, metric_label: str, unit: str) -> None:
    """Agrega leyenda manual para tamaño/color de burbujas no climáticas."""
    unit_label = unit_display_name(unit)
    html = f"""
    <div style="position: fixed; left: 24px; bottom: 24px; z-index: 9999;
        background: rgba(255,255,255,.94); border: 1px solid #E2E8F0; border-radius: 14px;
        box-shadow: 0 12px 28px rgba(15,23,42,.12); padding: 12px 14px; font-family: Inter, Arial;
        color: #0F172A; min-width: 190px;">
        <div style="font-weight: 800; font-size: 13px; margin-bottom: 4px;">{metric_label}</div>
        <div style="color:#64748B;font-size:11px;margin-bottom:9px;">Unidad: {unit_label}</div>
        <div style="display:flex; align-items:end; gap:14px;">
            <div style="text-align:center;font-size:11px;color:#64748B;">
                <div style="margin:auto;width:13px;height:13px;border-radius:999px;background:{VALUE_SCALE_COLORS['low']};border:2px solid white;box-shadow:0 0 0 1px #CBD5E1;"></div>
                Bajo
            </div>
            <div style="text-align:center;font-size:11px;color:#64748B;">
                <div style="margin:auto;width:19px;height:19px;border-radius:999px;background:{VALUE_SCALE_COLORS['mid']};border:2px solid white;box-shadow:0 0 0 1px #CBD5E1;"></div>
                Medio
            </div>
            <div style="text-align:center;font-size:11px;color:#64748B;">
                <div style="margin:auto;width:27px;height:27px;border-radius:999px;background:{VALUE_SCALE_COLORS['high']};border:2px solid white;box-shadow:0 0 0 1px #CBD5E1;"></div>
                Alto
            </div>
        </div>
    </div>
    """
    fmap.get_root().html.add_child(Element(html))


def _add_climate_legend(fmap: folium.Map, metric_label: str) -> None:
    """Agrega leyenda climática manual en porcentaje, evitando mostrar proporciones 0.12."""
    html = f"""
    <div style="position: fixed; left: 24px; bottom: 24px; z-index: 9999;
        background: rgba(255,255,255,.94); border: 1px solid #E2E8F0; border-radius: 14px;
        box-shadow: 0 12px 28px rgba(15,23,42,.12); padding: 12px 14px; font-family: Inter, Arial;
        color: #0F172A; min-width: 235px;">
        <div style="font-weight: 800; font-size: 13px; margin-bottom: 4px;">{metric_label} promedio</div>
        <div style="color:#64748B;font-size:11px;margin-bottom:8px;">Unidad: % de reportes METAR</div>
        <div style="height:10px;border-radius:999px;background:linear-gradient(90deg,#60A5FA,#22C55E,#F59E0B,#EF4444);"></div>
        <div style="display:flex;justify-content:space-between;font-size:10.5px;color:#64748B;margin-top:5px;">
            <span>0 %</span><span>3 %</span><span>8 %</span><span>15 %+</span>
        </div>
    </div>
    """
    fmap.get_root().html.add_child(Element(html))


def build_airport_map(
    airport_df: pd.DataFrame,
    active_layer: str,
    metric_col: str,
    metric_label: str,
    unit: str,
    selected_icao: str | None = None,
) -> folium.Map:
    """Construye el mapa interactivo con marcadores clicables."""
    fmap = folium.Map(
        location=COLOMBIA_CENTER,
        zoom_start=DEFAULT_ZOOM,
        tiles="OpenStreetMap",
        control_scale=False,
        prefer_canvas=True,
    )

    if airport_df.empty or metric_col not in airport_df.columns:
        return fmap

    metric_values = airport_df[metric_col].fillna(0).clip(lower=0)
    low_threshold = float(metric_values.quantile(0.33))
    high_threshold = float(metric_values.quantile(0.66))
    radius_source = airport_df["operaciones_total"] if active_layer == "clima" else airport_df[metric_col]
    radius_values = _scale_radius(radius_source, 5, 22)

    for idx, row in airport_df.iterrows():
        is_selected = selected_icao == row["icao_code"]
        base_color = _climate_color(row.get(metric_col)) if active_layer == "clima" else _value_color(row.get(metric_col), low_threshold, high_threshold)
        radius = float(radius_values.loc[idx]) + (4 if is_selected else 0)
        fill_opacity = 0.86 if not is_selected else 0.96
        border_color = "#0F172A" if is_selected else "#FFFFFF"
        border_weight = 3.5 if is_selected else 2.0

        folium.CircleMarker(
            location=[row["latitude_deg"], row["longitude_deg"]],
            radius=radius,
            color=border_color,
            weight=border_weight,
            fill=True,
            fill_color=base_color,
            fill_opacity=fill_opacity,
            tooltip=folium.Tooltip(_tooltip_html(row, metric_col, metric_label, unit), sticky=True),
            popup=folium.Popup(str(row["icao_code"]), parse_html=False, max_width=120),
        ).add_to(fmap)

        if is_selected:
            folium.CircleMarker(
                location=[row["latitude_deg"], row["longitude_deg"]],
                radius=radius + 8,
                color=base_color,
                weight=2,
                fill=False,
                opacity=0.35,
            ).add_to(fmap)

    if active_layer == "clima":
        _add_climate_legend(fmap, metric_label)
    else:
        _add_value_legend(fmap, metric_label, unit)

    return fmap
