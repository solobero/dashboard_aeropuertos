from __future__ import annotations

import pandas as pd
import streamlit as st

from src.labels import display_airport_type, display_month, display_region
from src.tokens import CLIMATE_METRICS, CONNECTIVITY_METRICS


def _last_n_months(max_date, months: int):
    """Calcula un rango mensual relativo al último mes disponible del dataset, no a la fecha actual."""
    end_date = pd.to_datetime(max_date).date()
    start_date = (pd.to_datetime(max_date) - pd.DateOffset(months=months - 1)).date()
    return start_date, end_date


def _year_range(df: pd.DataFrame, year: int):
    """Devuelve el rango real disponible para un año específico dentro del dataset."""
    year_dates = df.loc[df["fecha_mes"].dt.year.eq(year), "fecha_mes"]
    return year_dates.min().date(), year_dates.max().date()


def _render_period_filter(df: pd.DataFrame):
    """Renderiza un filtro temporal totalmente en español y limitado al rango real del dataset."""
    min_date = df["fecha_mes"].min().date()
    max_date = df["fecha_mes"].max().date()
    years = sorted(df["fecha_mes"].dt.year.dropna().astype(int).unique().tolist())

    period_options = (
        ["Todo el periodo"]
        + [str(year) for year in years]
        + ["Últimos 12 meses del dataset", "Últimos 24 meses del dataset", "Rango personalizado"]
    )

    period = st.selectbox(
        "Período",
        period_options,
        index=0,
    )

    if period == "Todo el periodo":
        return min_date, max_date, period

    if period == "Últimos 12 meses del dataset":
        start_date, end_date = _last_n_months(max_date, months=12)
        return max(start_date, min_date), end_date, period

    if period == "Últimos 24 meses del dataset":
        start_date, end_date = _last_n_months(max_date, months=24)
        return max(start_date, min_date), end_date, period

    if period == "Rango personalizado":
        months = sorted(df["fecha_mes"].dropna().dt.to_period("M").unique())
        month_dates = [month.to_timestamp().date() for month in months]
        month_labels = {date_value: display_month(date_value) for date_value in month_dates}

        start_col, end_col = st.columns(2)
        with start_col:
            start_date = st.selectbox(
                "Desde",
                month_dates,
                index=0,
                format_func=lambda value: month_labels[value],
            )
        with end_col:
            valid_end_dates = [date_value for date_value in month_dates if date_value >= start_date]
            end_date = st.selectbox(
                "Hasta",
                valid_end_dates,
                index=len(valid_end_dates) - 1,
                format_func=lambda value: month_labels[value],
            )
        return start_date, end_date, period

    year = int(period)
    start_date, end_date = _year_range(df, year)
    return start_date, end_date, period


def render_filters(df: pd.DataFrame, active_layer: str) -> dict:
    """Renderiza filtros mínimos en español y basados únicamente en el rango real del dataset."""
    st.markdown("<div class='ad-card'><div class='ad-title'>Filtros</div>", unsafe_allow_html=True)

    start_date, end_date, period_label = _render_period_filter(df)

    raw_regions = sorted(df["region_name"].fillna("Sin región").unique().tolist(), key=display_region)
    region_options = ["Todas"] + raw_regions
    region = st.selectbox(
        "Región",
        region_options,
        index=0,
        format_func=lambda value: "Todas" if value == "Todas" else display_region(value),
    )

    raw_types = sorted(df["type"].fillna("Sin tipo").unique().tolist(), key=display_airport_type)
    type_options = ["Todos"] + raw_types
    airport_type = st.selectbox(
        "Tipo de aeropuerto",
        type_options,
        index=0,
        format_func=lambda value: "Todos" if value == "Todos" else display_airport_type(value),
    )

    climate_metric = st.session_state.get("climate_metric", "Lluvia")
    connectivity_metric = st.session_state.get("connectivity_metric", "Destinos")

    if active_layer == "clima":
        climate_metric = st.radio(
            "Variable METAR",
            list(CLIMATE_METRICS.keys()),
            horizontal=False,
            index=list(CLIMATE_METRICS.keys()).index(climate_metric),
        )
        st.session_state["climate_metric"] = climate_metric

    if active_layer == "conectividad":
        connectivity_metric = st.radio(
            "Métrica de conectividad",
            list(CONNECTIVITY_METRICS.keys()),
            horizontal=False,
            index=list(CONNECTIVITY_METRICS.keys()).index(connectivity_metric),
        )
        st.session_state["connectivity_metric"] = connectivity_metric

    st.markdown(
        f"<div class='ad-muted' style='margin-top:.9rem;'>Periodo aplicado: {display_month(start_date)} – {display_month(end_date)}</div>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    return {
        "start_date": start_date,
        "end_date": end_date,
        "period_label": period_label,
        "region": region,
        "airport_type": airport_type,
        "climate_metric": climate_metric,
        "connectivity_metric": connectivity_metric,
    }
