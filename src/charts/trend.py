from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go

from src.formatting import unit_display_name, convert_for_visual
from src.tokens import LAYER_CONFIGS


def hex_to_rgba(hex_color: str, alpha: float = 0.14) -> str:
    """Convierte un color HEX #RRGGBB a rgba(r,g,b,a), formato aceptado por Plotly."""
    color = hex_color.strip().lstrip("#")

    if len(color) != 6:
        return f"rgba(37, 99, 235, {alpha})"

    r = int(color[0:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:6], 16)

    return f"rgba({r}, {g}, {b}, {alpha})"


def _series_includes_2020(series: pd.DataFrame) -> bool:
    """Indica si la serie temporal incluye meses de 2020."""
    if series.empty or "fecha_mes" not in series.columns:
        return False
    years = pd.to_datetime(series["fecha_mes"]).dt.year
    return bool((years == 2020).any())


def build_trend_chart(
    series: pd.DataFrame,
    active_layer: str,
    metric_label: str,
    unit: str,
    selected_label: str,
) -> go.Figure:
    """Construye una serie temporal limpia para el periodo y aeropuerto seleccionados."""
    cfg = LAYER_CONFIGS[active_layer]
    line_color = cfg["color"]
    area_color = hex_to_rgba(line_color, alpha=0.13)
    unit_label = unit_display_name(unit)

    fig = go.Figure()

    if not series.empty:
        y_values = convert_for_visual(series["valor"], unit)

        fig.add_trace(
            go.Scatter(
                x=series["fecha_mes"],
                y=y_values,
                mode="lines+markers",
                line={"color": line_color, "width": 3, "shape": "spline"},
                marker={"size": 6, "color": line_color},
                fill="tozeroy",
                fillcolor=area_color,
                hovertemplate=f"%{{x|%Y-%m}}<br>%{{y:,.2f}} {unit_label}<extra></extra>",
            )
        )

        if _series_includes_2020(series):
            fig.add_vrect(
                x0="2020-03-01",
                x1="2020-12-31",
                fillcolor="rgba(239, 68, 68, 0.14)",
                line_width=1,
                line_color="rgba(239, 68, 68, 0.35)",
                layer="below",
                annotation_text="COVID-19 · 2020",
                annotation_position="top left",
                annotation_font={"size": 11, "color": "#991B1B"},
            )

    fig.update_layout(
        title={
            "text": f"Evolución · {metric_label} ({unit_label}) · {selected_label}",
            "x": 0.01,
            "xanchor": "left",
            "font": {"size": 16, "color": "#0F172A"},
        },
        height=260,
        margin={"l": 10, "r": 10, "t": 55, "b": 10},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={"family": "Arial", "color": "#475569"},
        xaxis={"showgrid": False, "zeroline": False, "title": "Mes"},
        yaxis={"gridcolor": "#E2E8F0", "zeroline": False, "title": unit_label},
        hovermode="x unified",
        showlegend=False,
    )

    return fig
