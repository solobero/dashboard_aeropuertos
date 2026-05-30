from __future__ import annotations

import streamlit as st

from src.formatting import format_metric, unit_display_name
from src.labels import display_region
from src.tokens import COLORS, LAYER_CONFIGS
from src.ui.icons import svg_icon


def _render_html(markup: str) -> None:
    """Renderiza HTML compacto para evitar bloques de código Markdown."""
    compact_markup = " ".join(markup.split())
    st.markdown(compact_markup, unsafe_allow_html=True)


def render_brand() -> None:
    """Renderiza la marca del proyecto como enlace de retorno a la portada."""

    st.markdown(
        """
        <a class="ad-brand-link" href="./" target="_self" title="Volver a la portada">
            <div class="ad-brand">
                <div class="ad-logo">✈</div>
                <div class="ad-brand-text">
                    <span>AeroDatos</span>
                    <strong>Colombia</strong>
                </div>
            </div>
        </a>
        """,
        unsafe_allow_html=True,
    )


def render_layer_selector(active_layer: str) -> str:
    """Renderiza selector de capas con botones Streamlit sin tooltips ni pestañas nuevas."""
    from src.state import set_active_layer

    cols = st.columns(len(LAYER_CONFIGS), gap="small")

    for col, (key, cfg) in zip(cols, LAYER_CONFIGS.items()):
        with col:
            is_active = key == active_layer
            clicked = st.button(
                cfg["label"],
                key=f"layer_button_{key}",
                use_container_width=True,
                type="primary" if is_active else "secondary",
            )
            if clicked and not is_active:
                set_active_layer(key)
                active_layer = key
                st.rerun()

    return active_layer


def render_layer_context(active_layer: str) -> None:
    """Muestra título y microdescripción de la capa activa debajo del selector."""
    cfg = LAYER_CONFIGS[active_layer]
    _render_html(f"""
    <section class="ad-layer-context" style="--layer-color:{cfg['color']}; --layer-soft:{cfg['soft']};">
        <div class="ad-layer-context-icon">{svg_icon(cfg['icon'], cfg['color'], 20)}</div>
        <div>
            <div class="ad-layer-context-title">{cfg['title']}</div>
            <div class="ad-layer-context-text">{cfg['description']}</div>
        </div>
    </section>
    """)


def render_summary_card(
    title: str,
    value: str,
    subtitle: str,
    icon: str,
    color: str,
) -> None:
    """Renderiza una tarjeta ejecutiva compacta."""
    _render_html(f"""
    <div class="ad-card-soft">
        <div style="display:flex; gap:.85rem; align-items:center;">
            <div style="width:46px;height:46px;border-radius:16px;background:{color}22;display:grid;place-items:center;">
                {svg_icon(icon, color, 23)}
            </div>
            <div style="min-width:0;">
                <div class="ad-muted">{title}</div>
                <div class="ad-kpi-number">{value}</div>
                <div class="ad-muted">{subtitle}</div>
            </div>
        </div>
    </div>
    """)


def _summary_subtitle(unit: str, agg_rule: str) -> str:
    """Subtítulo unitario para tarjetas de resumen."""
    if unit == "%":
        return "% promedio METAR"
    if unit == "kg":
        return "toneladas · periodo seleccionado"
    if agg_rule == "mean":
        return f"{unit_display_name(unit)} · promedio"
    return f"{unit_display_name(unit)} · periodo seleccionado"


def render_layer_summary(summary: dict, label: str, unit: str, icon: str, color: str, agg_rule: str = "sum") -> None:
    """Muestra resumen contextual de la capa actual."""
    leader = summary.get("leader")
    leader_label = "—"
    leader_sub = "Sin selección"
    if leader:
        leader_label = f"{leader.get('municipality', '—')} ({leader.get('icao_code', '—')})"
        leader_sub = "mayor valor en la vista actual"

    render_summary_card(
        title=label,
        value=format_metric(summary.get("total"), unit),
        subtitle=_summary_subtitle(unit, agg_rule),
        icon=icon,
        color=color,
    )
    render_summary_card(
        title="Aeropuerto líder",
        value=leader_label,
        subtitle=leader_sub,
        icon="tower",
        color=COLORS["green"],
    )
    render_summary_card(
        title="Aeropuertos activos",
        value=str(summary.get("n_airports", 0)),
        subtitle="con datos filtrados",
        icon="pin",
        color=COLORS["purple"],
    )


def render_airport_detail(row: dict, active_layer: str) -> None:
    """Renderiza panel de detalle luego de hacer clic en un aeropuerto."""
    cfg = LAYER_CONFIGS[active_layer]
    _render_html(f"""
    <div class="ad-card">
        <div style="display:flex; justify-content:space-between; gap:1rem; align-items:start;">
            <div>
                <div class="ad-title">{row.get('name', 'Aeropuerto')}</div>
                <div class="ad-muted">{row.get('icao_code', '—')} · {row.get('municipality', '—')} · {display_region(row.get('region_name'))}</div>
            </div>
            <div style="width:44px;height:44px;border-radius:16px;background:{cfg['soft']};display:grid;place-items:center;">
                {svg_icon(cfg['icon'], cfg['color'], 22)}
            </div>
        </div>
    </div>
    """)

    render_summary_card(
        "Operaciones",
        format_metric(row.get("operaciones_total"), "operaciones"),
        "operaciones · periodo seleccionado",
        "plane",
        COLORS["blue"],
    )
    render_summary_card(
        "Pasajeros",
        format_metric(row.get("pasajeros_total"), "personas"),
        "pasajeros · periodo seleccionado",
        "users",
        COLORS["green"],
    )
    render_summary_card(
        "Carga",
        format_metric(row.get("carga_total_kg"), "kg"),
        "toneladas · periodo seleccionado",
        "box",
        COLORS["purple"],
    )
    render_summary_card(
        "Lluvia",
        format_metric(row.get("prop_lluvia"), "%"),
        "% de reportes METAR",
        "cloud",
        COLORS["cyan"],
    )


def render_empty_selection() -> None:
    """Muestra instrucción breve cuando no hay aeropuerto seleccionado."""
    _render_html("""
    <div class="ad-layer-note">
        Haz clic sobre un aeropuerto en el mapa para abrir su perfil operativo y meteorológico.
    </div>
    """)
