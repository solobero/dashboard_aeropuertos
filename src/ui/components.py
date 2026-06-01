from __future__ import annotations

import streamlit as st

from src.formatting import format_metric
from src.labels import display_region
from src.tokens import COLORS, LAYER_CONFIGS
from src.ui.icons import svg_icon


def _render_html(markup: str) -> None:
    """Renderiza HTML compacto para evitar que Markdown lo muestre como bloque de código."""

    compact_markup = " ".join(markup.split())
    st.markdown(compact_markup, unsafe_allow_html=True)


def build_brand_markup(link_to_home: bool = True, extra_class: str = "") -> str:
    """Construye el HTML de la marca de forma consistente en dashboard y landing."""

    if link_to_home:
        wrapper_open = (
            f'<a class="ad-brand-link {extra_class}" '
            f'href="./" target="_self" title="Volver a la portada">'
        )
        wrapper_close = "</a>"
    else:
        wrapper_open = f'<div class="ad-brand-link {extra_class}">'
        wrapper_close = "</div>"

    return f"""
    {wrapper_open}
        <span class="ad-brand-shell">
            <span class="ad-brand-logo">
                <span class="ad-brand-logo-symbol">✈</span>
            </span>
            <span class="ad-brand-text">
                <span class="ad-brand-main">AeroDatos</span>
                <span class="ad-brand-accent">Colombia</span>
            </span>
        </span>
    {wrapper_close}
    """


def render_brand() -> None:
    """Marca del dashboard. Al hacer clic vuelve a la landing page en la misma pestaña."""

    _render_html(build_brand_markup(link_to_home=True))


def render_landing_brand() -> None:
    """Marca de la landing page. Es visual, no navega."""

    _render_html(build_brand_markup(link_to_home=False, extra_class="ad-landing-brand"))


def render_layer_selector(active_layer: str) -> str:
    """Renderiza selector de capas con botones Streamlit."""

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

    _render_html(
        f"""
        <section class="ad-layer-context" style="--layer-color:{cfg['color']}; --layer-soft:{cfg['soft']};">
            <div class="ad-layer-context-icon">
                {svg_icon(cfg['icon'], cfg['color'], 20)}
            </div>
            <div>
                <div class="ad-layer-context-title">{cfg['title']}</div>
                <div class="ad-layer-context-text">{cfg['description']}</div>
            </div>
        </section>
        """
    )


def leader_svg_icon(color: str = "#F59E0B") -> str:
    """Ícono para indicar aeropuerto con mayor valor en la vista actual."""

    return f"""
    <svg width="26" height="26" viewBox="0 0 24 24" fill="none"
         xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="M7 4H17V7.5C17 10.26 14.76 12.5 12 12.5C9.24 12.5 7 10.26 7 7.5V4Z"
              stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M7 6H4V7.5C4 9.43 5.57 11 7.5 11"
              stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M17 6H20V7.5C20 9.43 18.43 11 16.5 11"
              stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M12 12.5V17"
              stroke="{color}" stroke-width="2" stroke-linecap="round"/>
        <path d="M9 20H15"
              stroke="{color}" stroke-width="2" stroke-linecap="round"/>
        <path d="M10 17H14"
              stroke="{color}" stroke-width="2" stroke-linecap="round"/>
    </svg>
    """

def airport_marker_svg_icon(color: str = "#2563EB") -> str:
    """Ícono tipo marcador de ubicación con avión, para el encabezado del aeropuerto seleccionado."""

    return f"""
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none"
         xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="M12 21C12 21 19 14.2 19 9.5C19 5.91 15.87 3 12 3C8.13 3 5 5.91 5 9.5C5 14.2 12 21 12 21Z"
              stroke="{color}" stroke-width="2" stroke-linejoin="round"/>
        <circle cx="12" cy="9.5" r="4.1" fill="white" stroke="{color}" stroke-width="1.6"/>
        <path d="M10.15 10.2L13.95 8.3C14.3 8.12 14.68 8.5 14.5 8.85L12.6 12.65C12.45 12.95 12.05 12.98 11.86 12.7L11.2 11.72L10.22 11.06C9.94 10.87 9.97 10.47 10.27 10.32L10.15 10.2Z"
              fill="{color}"/>
    </svg>
    """

def render_summary_card(
    title: str,
    value: str,
    subtitle: str,
    icon_svg: str,
    color: str,
    soft_color: str,
) -> None:
    """Renderiza una tarjeta lateral con color semántico por indicador."""

    value_text = str(value) if value is not None else "—"

    value_class = "ad-side-kpi-value"

    if any(char.isalpha() for char in value_text) or len(value_text) > 10:
        value_class += " ad-side-kpi-value-text"

    _render_html(
        f"""
        <div class="ad-side-kpi-card" style="--card-accent:{color}; --card-soft:{soft_color};">
            <div class="ad-side-kpi-top">
                <div class="ad-side-kpi-title">{title}</div>
                <div class="ad-side-kpi-icon">
                    {icon_svg}
                </div>
            </div>

            <div class="{value_class}">
                {value_text}
            </div>

            <div class="ad-side-kpi-subtitle">
                {subtitle}
            </div>
        </div>
        """
    )


def get_right_panel_texts(active_layer: str, metric_label: str | None = None) -> dict:
    """Devuelve títulos y subtítulos claros para las tarjetas laterales."""

    metric_label = metric_label or LAYER_CONFIGS[active_layer]["display"]

    texts = {
        "operacion": {
            "total_title": "Operaciones acumuladas",
            "total_subtitle": "total del periodo seleccionado",
            "leader_title": "Mayor operación",
            "leader_subtitle": "aeropuerto con más operaciones",
            "count_title": "Aeropuertos en la vista",
            "count_subtitle": "con datos filtrados",
        },
        "pasajeros": {
            "total_title": "Pasajeros movilizados",
            "total_subtitle": "total del periodo seleccionado",
            "leader_title": "Mayor flujo de pasajeros",
            "leader_subtitle": "aeropuerto con más pasajeros",
            "count_title": "Aeropuertos en la vista",
            "count_subtitle": "con datos filtrados",
        },
        "carga": {
            "total_title": "Carga transportada",
            "total_subtitle": "toneladas acumuladas",
            "leader_title": "Mayor carga",
            "leader_subtitle": "aeropuerto con más carga",
            "count_title": "Aeropuertos en la vista",
            "count_subtitle": "con datos filtrados",
        },
        "conectividad": {
            "total_title": f"{metric_label} promedio",
            "total_subtitle": "promedio mensual del periodo",
            "leader_title": f"Mayor {metric_label.lower()}",
            "leader_subtitle": "aeropuerto con mayor valor",
            "count_title": "Aeropuertos en la vista",
            "count_subtitle": "con datos filtrados",
        },
        "clima": {
            "total_title": f"{metric_label} observado",
            "total_subtitle": "porcentaje promedio METAR",
            "leader_title": f"Mayor {metric_label.lower()}",
            "leader_subtitle": "aeropuerto con mayor porcentaje",
            "count_title": "Aeropuertos en la vista",
            "count_subtitle": "con datos METAR filtrados",
        },
    }

    return texts.get(active_layer, texts["operacion"])


def render_layer_summary(
    summary: dict,
    label: str,
    unit: str,
    icon: str,
    color: str,
    active_layer: str,
    metric_label: str | None = None,
    agg_rule: str = "sum",
) -> None:
    """Muestra resumen contextual de la capa actual con títulos claros."""

    panel_texts = get_right_panel_texts(active_layer, metric_label)

    leader = summary.get("leader")
    leader_label = "—"

    if leader:
        leader_label = f"{leader.get('municipality', '—')} ({leader.get('icao_code', '—')})"

    render_summary_card(
        title=panel_texts["total_title"],
        value=format_metric(summary.get("total"), unit),
        subtitle=panel_texts["total_subtitle"],
        icon_svg=svg_icon(icon, color, 26),
        color=color,
        soft_color=LAYER_CONFIGS[active_layer]["soft"],
    )

    render_summary_card(
        title=panel_texts["leader_title"],
        value=leader_label,
        subtitle=panel_texts["leader_subtitle"],
        icon_svg=leader_svg_icon(COLORS.get("amber", "#F59E0B")),
        color=COLORS.get("amber", "#F59E0B"),
        soft_color=COLORS.get("amber_soft", "#FEF3C7"),
    )

    render_summary_card(
        title=panel_texts["count_title"],
        value=str(summary.get("n_airports", 0)),
        subtitle=panel_texts["count_subtitle"],
        icon_svg=svg_icon("pin", COLORS["purple"], 26),
        color=COLORS["purple"],
        soft_color=COLORS.get("purple_soft", "#EDE9FE"),
    )


def render_airport_detail(row: dict, active_layer: str) -> None:
    """Renderiza el panel de detalle cuando el usuario hace clic en un aeropuerto."""

    cfg = LAYER_CONFIGS[active_layer]

    _render_html(
        f"""
        <div class="ad-airport-hero" style="--airport-accent:{cfg['color']}; --airport-soft:{cfg['soft']};">
            <div class="ad-airport-hero-top">
                <div class="ad-airport-eyebrow">Aeropuerto seleccionado</div>
                <div class="ad-airport-hero-icon">
                    {airport_marker_svg_icon(cfg['color'])}
                </div>
            </div>

            <div class="ad-airport-hero-name">
                {row.get('name', 'Aeropuerto')}
            </div>

            <div class="ad-airport-hero-meta">
                <span class="ad-airport-meta-chip ad-airport-meta-icao">
                    {row.get('icao_code', '—')}
                </span>
                <span class="ad-airport-meta-chip">
                    {row.get('municipality', '—')}
                </span>
                <span class="ad-airport-meta-chip">
                    {display_region(row.get('region_name'))}
                </span>
            </div>
        </div>
        """
    )

    render_summary_card(
        title="Operación del aeropuerto",
        value=format_metric(row.get("operaciones_total"), "operaciones"),
        subtitle="operaciones acumuladas en el periodo",
        icon_svg=svg_icon("plane", COLORS["blue"], 26),
        color=COLORS["blue"],
        soft_color=COLORS.get("blue_soft", "#DBEAFE"),
    )

    render_summary_card(
        title="Pasajeros movilizados",
        value=format_metric(row.get("pasajeros_total"), "personas"),
        subtitle="pasajeros acumulados en el periodo",
        icon_svg=svg_icon("users", COLORS["green"], 26),
        color=COLORS["green"],
        soft_color=COLORS.get("green_soft", "#DCFCE7"),
    )

    render_summary_card(
        title="Carga transportada",
        value=format_metric(row.get("carga_total_kg"), "kg"),
        subtitle="toneladas acumuladas en el periodo",
        icon_svg=svg_icon("box", COLORS["purple"], 26),
        color=COLORS["purple"],
        soft_color=COLORS.get("purple_soft", "#EDE9FE"),
    )

    render_summary_card(
        title="Lluvia observada",
        value=format_metric(row.get("prop_lluvia"), "%"),
        subtitle="porcentaje de reportes METAR con lluvia",
        icon_svg=svg_icon("cloud", COLORS["cyan"], 26),
        color=COLORS["cyan"],
        soft_color=COLORS.get("cyan_soft", "#CFFAFE"),
    )


def render_empty_selection() -> None:
    """Muestra instrucción breve cuando no hay aeropuerto seleccionado."""

    _render_html(
        """
        <div class="ad-layer-note">
            Haz clic sobre un aeropuerto en el mapa para abrir su perfil operativo y meteorológico.
        </div>
        """
    )