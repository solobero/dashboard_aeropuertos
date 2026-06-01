from __future__ import annotations

import streamlit as st
from streamlit_folium import st_folium

from src.aggregations import (
    apply_filters,
    build_airport_summary,
    build_global_summary,
    build_timeseries,
    nearest_airport,
    resolve_metric,
)
from src.charts.trend import build_trend_chart
from src.config import MAP_HEIGHT
from src.maps.folium_map import build_airport_map
from src.state import clear_selected_airport, set_selected_airport
from src.styles import apply_active_layer_styles
from src.tokens import LAYER_CONFIGS
from src.ui.components import (
    render_airport_detail,
    render_brand,
    render_empty_selection,
    render_layer_context,
    render_layer_selector,
    render_layer_summary,
)
from src.ui.filters import render_filters


def _parse_map_click(map_output: dict, airport_df) -> str | None:
    """Interpreta clics de streamlit-folium como código ICAO seleccionado."""

    popup_value = map_output.get("last_object_clicked_popup") if isinstance(map_output, dict) else None

    if popup_value and str(popup_value).strip() in set(airport_df["icao_code"]):
        return str(popup_value).strip()

    clicked = map_output.get("last_clicked") if isinstance(map_output, dict) else None

    if clicked and "lat" in clicked and "lng" in clicked:
        return nearest_airport(airport_df, clicked["lat"], clicked["lng"])

    return None


def render_map_explorer(df) -> None:
    """Renderiza la experiencia principal basada en mapa, capas y clics."""

    header_cols = st.columns([1.6, 3.7, 1.15], vertical_alignment="center")

    with header_cols[0]:
        render_brand()

    with header_cols[1]:
        active_layer = render_layer_selector(st.session_state["active_layer"])

    with header_cols[2]:
        st.markdown(
            "<div class='ad-pill'>Actualizado · dataset mensual</div>",
            unsafe_allow_html=True,
        )

    active_layer = st.session_state["active_layer"]

    apply_active_layer_styles(active_layer)
    render_layer_context(active_layer)

    filter_col, map_col, detail_col = st.columns(
        [1.05, 4.0, 1.62],
        gap="large",
    )

    with filter_col:
        filters = render_filters(df, active_layer)

    submetric = (
        filters["climate_metric"]
        if active_layer == "clima"
        else filters["connectivity_metric"]
    )

    metric_col, metric_label, unit, agg_rule = resolve_metric(active_layer, submetric)

    filtered_df = apply_filters(
        df=df,
        start_date=filters["start_date"],
        end_date=filters["end_date"],
        region=filters["region"],
        airport_type=filters["airport_type"],
    )

    airport_df = build_airport_summary(filtered_df)

    selected_icao = st.session_state.get("selected_icao")

    if selected_icao and selected_icao not in set(airport_df["icao_code"]):
        selected_icao = None
        clear_selected_airport()

    with map_col:
        fmap = build_airport_map(
            airport_df=airport_df,
            active_layer=active_layer,
            metric_col=metric_col,
            metric_label=metric_label,
            unit=unit,
            selected_icao=selected_icao,
        )

        map_output = st_folium(
            fmap,
            height=MAP_HEIGHT,
            use_container_width=True,
            returned_objects=["last_object_clicked_popup", "last_clicked"],
            key=f"map_{active_layer}_{metric_col}_{filters['start_date']}_{filters['end_date']}",
        )

    clicked_icao = _parse_map_click(map_output, airport_df)

    if clicked_icao and clicked_icao != st.session_state.get("selected_icao"):
        set_selected_airport(clicked_icao)
        st.rerun()

    selected_icao = st.session_state.get("selected_icao")
    selected_row = None

    if selected_icao:
        selected_matches = airport_df[airport_df["icao_code"].eq(selected_icao)]

        if not selected_matches.empty:
            selected_row = selected_matches.iloc[0].to_dict()

    with detail_col:
        cfg = LAYER_CONFIGS[active_layer]

        if selected_row:
            render_airport_detail(selected_row, active_layer)

            with st.container(key="clear_selection_action"):
                if st.button(
                    "Limpiar selección",
                    key="clear_selection_button",
                    use_container_width=True,
                    type="secondary",
                ):
                    clear_selected_airport()
                    st.rerun()

        else:
            summary = build_global_summary(airport_df, metric_col, agg_rule)

            render_layer_summary(
                summary=summary,
                label=cfg["label"],
                unit=unit,
                icon=cfg["icon"],
                color=cfg["color"],
                active_layer=active_layer,
                metric_label=metric_label,
                agg_rule=agg_rule,
            )

            render_empty_selection()

    with map_col:
        selected_label = "Nacional"

        if selected_row:
            selected_label = f"{selected_row.get('municipality', selected_icao)} ({selected_icao})"

        series = build_timeseries(filtered_df, metric_col, agg_rule, selected_icao)

        fig = build_trend_chart(
            series=series,
            active_layer=active_layer,
            metric_label=metric_label,
            unit=unit,
            selected_label=selected_label,
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displayModeBar": False},
        )