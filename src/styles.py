import streamlit as st

from src.tokens import COLORS, LAYER_CONFIGS


def apply_styles() -> None:
    """Inyecta CSS ligero para obtener una interfaz limpia y consistente."""

    st.markdown(
        f"""
        <style>
        .block-container {{
            padding-top: 0rem !important;
            padding-bottom: 1.5rem;
            max-width: 100%;
        }}

        header[data-testid="stHeader"] {{
            display: none !important;
            visibility: hidden !important;
            height: 0rem !important;
        }}

        [data-testid="stToolbar"] {{ display: none !important; }}
        [data-testid="stDecoration"] {{ display: none !important; }}
        [data-testid="stStatusWidget"] {{ display: none !important; }}
        .stDeployButton {{ display: none !important; }}
        [data-testid="stSidebar"] {{ display: none; }}
        #MainMenu {{ visibility: hidden; }}
        footer {{ visibility: hidden; }}

        div[data-testid="stVerticalBlock"] {{
            gap: 0.95rem;
        }}

        /* ============================================================
           Marca / logo consistente para dashboard y landing
           ============================================================ */

        .ad-brand-link,
        .ad-brand-link:visited,
        .ad-brand-link:hover,
        .ad-brand-link:active {{
            display: inline-flex;
            align-items: center;
            text-decoration: none !important;
            color: inherit !important;
            cursor: pointer !important;
            width: fit-content;
        }}

        .ad-brand-shell {{
            display: inline-flex;
            align-items: center;
            gap: 0.9rem;
            width: fit-content;
        }}

        .ad-brand-logo {{
            width: 42px;
            height: 42px;
            min-width: 42px;
            border-radius: 14px;
            background: linear-gradient(135deg, {COLORS['blue']}, {COLORS['cyan']});
            display: inline-flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 10px 24px rgba(37, 99, 235, .24);
        }}

        .ad-brand-logo-symbol {{
            color: white !important;
            font-size: 1.18rem;
            line-height: 1;
            transform: rotate(-8deg);
        }}

        .ad-brand-text {{
            display: inline-flex;
            align-items: baseline;
            gap: 0.24rem;
            white-space: nowrap;
            line-height: 1;
        }}

        .ad-brand-main {{
            font-weight: 900;
            font-size: 1.34rem;
            letter-spacing: -0.045em;
            color: {COLORS['text']};
        }}

        .ad-brand-accent {{
            font-weight: 900;
            font-size: 1.34rem;
            letter-spacing: -0.045em;
            color: {COLORS['blue']};
        }}

        .ad-landing-brand {{
            margin-bottom: 1.7rem;
            cursor: default !important;
        }}

        .ad-landing-brand .ad-brand-main,
        .ad-landing-brand .ad-brand-accent {{
            font-size: 1.42rem;
        }}

        .ad-landing-brand .ad-brand-logo {{
            width: 44px;
            height: 44px;
            min-width: 44px;
            border-radius: 15px;
        }}

        /* ============================================================
           Componentes generales
           ============================================================ */

        .ad-card {{
            background: {COLORS['surface']};
            border: 1px solid var(--active-layer-border, {COLORS['border']});
            border-radius: 22px;
            padding: 1.15rem;
            box-shadow: 0 16px 40px rgba(15, 23, 42, .07);
        }}

        .ad-card-soft {{
            background: linear-gradient(180deg, #FFFFFF, #F8FAFC);
            border: 1px solid {COLORS['border']};
            border-radius: 22px;
            padding: 1rem;
            box-shadow: 0 14px 34px rgba(15, 23, 42, .06);
            transition: border-color .15s ease, transform .15s ease, box-shadow .15s ease;
        }}

        .ad-card-soft:hover {{
            border-color: var(--active-layer-color, {COLORS['blue']});
            transform: translateY(-1px);
            box-shadow: 0 18px 42px rgba(15, 23, 42, .09);
        }}

        .ad-title {{
            color: {COLORS['text']};
            font-weight: 800;
            font-size: 1.05rem;
            margin-bottom: .15rem;
        }}

        .ad-muted {{
            color: {COLORS['muted']};
            font-size: .82rem;
        }}

        .ad-pill {{
            display: inline-flex;
            align-items: center;
            gap: .45rem;
            border: 1px solid {COLORS['border']};
            border-radius: 999px;
            padding: .45rem .75rem;
            color: {COLORS['muted']};
            background: {COLORS['surface']};
            font-size: .82rem;
            white-space: nowrap;
        }}

        .ad-layer-note {{
            background: {COLORS['blue_soft']};
            color: #1E3A8A;
            border-radius: 16px;
            padding: .8rem 1rem;
            font-size: .86rem;
            border: 1px solid #BFDBFE;
        }}

        /* ============================================================
           Contexto de capa
           ============================================================ */

        .ad-layer-context {{
            display: flex;
            align-items: center;
            gap: .9rem;
            margin: .45rem 0 .15rem 0;
            padding: .85rem 1rem;
            border-radius: 20px;
            background: linear-gradient(180deg, #FFFFFF, #F8FAFC);
            border: 1px solid {COLORS['border']};
            box-shadow: 0 12px 30px rgba(15, 23, 42, .045);
        }}

        .ad-layer-context:hover {{
            border-color: var(--active-layer-color);
        }}

        .ad-layer-context-icon {{
            width: 42px;
            height: 42px;
            border-radius: 15px;
            display: grid;
            place-items: center;
            background: var(--active-layer-soft);
            flex: 0 0 auto;
        }}

        .ad-layer-context-title {{
            color: {COLORS['text']};
            font-size: 1rem;
            font-weight: 850;
            letter-spacing: -0.02em;
        }}

        .ad-layer-context-text {{
            color: {COLORS['muted']};
            font-size: .88rem;
            line-height: 1.32;
            margin-top: .15rem;
        }}

        /* ============================================================
           Botones Streamlit
           ============================================================ */

        div.stButton > button {{
            border-radius: 16px !important;
            border: 1px solid {COLORS['border']} !important;
            background: white !important;
            color: {COLORS['text']} !important;
            height: 3.1rem;
            font-weight: 700 !important;
            box-shadow: 0 8px 24px rgba(15, 23, 42, .045);
            transition: color .15s ease, background .15s ease, border-color .15s ease, transform .15s ease, box-shadow .15s ease;
        }}

        div.stButton > button:hover {{
            border-color: var(--active-layer-color, {COLORS['blue']}) !important;
            color: var(--active-layer-color, {COLORS['blue']}) !important;
            background: var(--active-layer-soft, {COLORS['blue_soft']}) !important;
            transform: translateY(-1px);
            box-shadow: 0 14px 30px rgba(15, 23, 42, .075);
        }}

        div.stButton > button[kind="primary"],
        div.stButton > button[data-testid="stBaseButton-primary"] {{
            background: var(--active-layer-color, {COLORS['blue']}) !important;
            border-color: var(--active-layer-color, {COLORS['blue']}) !important;
            color: white !important;
            box-shadow: 0 14px 34px rgba(15, 23, 42, .10);
        }}

        div.stButton > button[kind="primary"]:hover,
        div.stButton > button[data-testid="stBaseButton-primary"]:hover {{
            background: var(--active-layer-color, {COLORS['blue']}) !important;
            color: white !important;
            filter: brightness(.97);
        }}

        div[data-baseweb="select"] > div {{
            border-radius: 14px !important;
            transition: border-color .15s ease, box-shadow .15s ease;
        }}

        div[data-baseweb="select"]:hover > div {{
            border-color: var(--active-layer-color, {COLORS['blue']}) !important;
            box-shadow: 0 0 0 1px var(--active-layer-color, {COLORS['blue']}) inset !important;
        }}

        label:hover,
        .stRadio:hover label {{
            color: var(--active-layer-color, {COLORS['blue']}) !important;
        }}

        .folium-map {{
            border-radius: 24px !important;
            overflow: hidden;
        }}

        iframe {{
            border-radius: 24px !important;
        }}

        /* ============================================================
           Panel lateral derecho: tarjetas KPI claras y legibles
           ============================================================ */

        .ad-side-kpi-card {{
            width: 100%;
            min-height: 156px;
            padding: 1.25rem 1.25rem 1.15rem 1.25rem;
            border-radius: 28px;
            background: rgba(255, 255, 255, 0.98);
            border: 1px solid #DDE7F3;
            box-shadow: 0 16px 38px rgba(15, 23, 42, 0.085);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            gap: 0.72rem;
            margin-bottom: 1.1rem;
        }}

        .ad-side-kpi-top {{
            display: grid;
            grid-template-columns: minmax(0, 1fr) 52px;
            align-items: start;
            gap: 1rem;
        }}

        .ad-side-kpi-title {{
            font-size: 1.08rem;
            font-weight: 900;
            line-height: 1.12;
            color: #0F172A;
            letter-spacing: -0.035em;
            max-width: none;
            word-break: normal;
            overflow-wrap: normal;
        }}

        .ad-side-kpi-icon {{
            width: 52px;
            height: 52px;
            min-width: 52px;
            border-radius: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .ad-side-kpi-icon svg {{
            width: 26px;
            height: 26px;
        }}

        .ad-side-kpi-value {{
            font-size: 2.15rem;
            font-weight: 950;
            line-height: 1.02;
            letter-spacing: -0.06em;
            color: #0F172A;
            word-break: normal;
        }}

        .ad-side-kpi-value-text {{
            font-size: 1.55rem;
            line-height: 1.12;
            letter-spacing: -0.04em;
            word-break: normal;
            overflow-wrap: break-word;
        }}

        .ad-side-kpi-subtitle {{
            font-size: 0.94rem;
            font-weight: 700;
            line-height: 1.25;
            color: #52657A;
        }}


        /* ============================================================
        Panel de aeropuerto seleccionado
        ============================================================ */

        .ad-airport-profile-card {{
            background: linear-gradient(180deg, #FFFFFF, #F8FAFC);
            border: 1px solid #DDE7F3;
            border-left: 6px solid var(--active-layer-color, #2563EB);
            border-radius: 28px;
            padding: 1.35rem 1.35rem 1.25rem 1.45rem;
            box-shadow: 0 16px 38px rgba(15, 23, 42, 0.085);
            margin-bottom: 1.1rem;
        }}

        .ad-airport-profile-main {{
            display: grid;
            grid-template-columns: minmax(0, 1fr) 56px;
            align-items: start;
            gap: 1.1rem;
        }}

        .ad-airport-profile-title {{
            color: #0F172A;
            font-size: 1.28rem;
            font-weight: 950;
            line-height: 1.08;
            letter-spacing: -0.045em;
            margin-bottom: 0.55rem;
        }}

        .ad-airport-profile-subtitle {{
            color: #52657A;
            font-size: 0.98rem;
            font-weight: 750;
            line-height: 1.28;
        }}

        .ad-airport-profile-subtitle strong {{
            color: #0F172A;
            font-weight: 900;
        }}

        .ad-airport-profile-icon {{
            width: 56px;
            height: 56px;
            min-width: 56px;
            border-radius: 20px;
            display: grid;
            place-items: center;
            box-shadow: inset 0 0 0 1px rgba(255, 255, 255, .75);
        }}

        .ad-airport-profile-icon svg {{
            width: 28px;
            height: 28px;
        }}


        /* ============================================================
        Landing page
        ============================================================ */

        .ad-landing-spacer {{
            height: clamp(2rem, 8vh, 6rem);
        }}

        .ad-landing-copy-only {{
            padding: 2rem 1.5rem 2rem 3rem;
        }}

        .ad-landing-kicker {{
            display: inline-flex;
            align-items: center;
            border-radius: 999px;
            border: 1px solid #BFDBFE;
            color: #1E40AF;
            background: rgba(255,255,255,.78);
            padding: .52rem .85rem;
            font-weight: 700;
            margin-bottom: 1.15rem;
        }}

        .ad-landing-title {{
            color: {COLORS['text']};
            font-size: clamp(2.2rem, 4.5vw, 4.7rem);
            line-height: .98;
            letter-spacing: -0.07em;
            font-weight: 900;
            margin: 1rem 0 1rem 0;
            max-width: 760px;
        }}

        .ad-landing-subtitle {{
            max-width: 680px;
            margin-top: 0rem;
            margin-bottom: 1.8rem;
            color: {COLORS['muted']};
            font-size: 1rem;
            line-height: 1.55;
        }}

        .ad-landing-image {{
            min-height: 500px;
            border-radius: 34px;
            border: 1px solid rgba(226, 232, 240, .9);
            overflow: hidden;
            background: #FFFFFF;
            box-shadow: 0 30px 80px rgba(15, 23, 42, .12);
        }}

        .ad-landing-image img {{
            width: 100%;
            height: 100%;
            min-height: 500px;
            object-fit: cover;
            display: block;
        }}

        .ad-landing-image-fallback {{
            display: grid;
            place-items: center;
            color: {COLORS['text']};
        }}

        .ad-landing-image-fallback div {{
            display: flex;
            flex-direction: column;
            gap: 0.4rem;
            align-items: center;
        }}

        .ad-landing-image-fallback strong {{
            font-size: 1.4rem;
        }}

        .ad-landing-image-fallback span {{
            color: {COLORS['muted']};
        }}

        @media (max-width: 1100px) {{
            .ad-landing-spacer {{
                height: 1rem;
            }}

            .ad-landing-copy-only {{
                padding: 1rem;
            }}

            .ad-landing-image {{
                min-height: 340px;
            }}

            .ad-landing-image img {{
                min-height: 340px;
            }}
        }}
        
        
        /* ============================================================
        Panel lateral derecho: tarjetas KPI con color semántico
        ============================================================ */

        .ad-side-kpi-card {{
            position: relative;
            width: 100%;
            min-height: 158px;
            padding: 1.25rem 1.25rem 1.15rem 1.35rem;
            border-radius: 28px;
            background: rgba(255, 255, 255, 0.985);
            border: 1px solid #DDE7F3;
            border-left: 6px solid var(--card-accent);
            box-shadow: 0 16px 38px rgba(15, 23, 42, 0.085);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            gap: 0.72rem;
            margin-bottom: 1.15rem;
            transition: transform .15s ease, box-shadow .15s ease, border-color .15s ease;
        }}

        .ad-side-kpi-card:hover {{
            transform: translateY(-1px);
            box-shadow: 0 20px 44px rgba(15, 23, 42, 0.115);
            border-color: var(--card-accent);
        }}

        .ad-side-kpi-top {{
            display: grid;
            grid-template-columns: minmax(0, 1fr) 54px;
            align-items: start;
            gap: 1rem;
        }}

        .ad-side-kpi-title {{
            font-size: 1.16rem;
            font-weight: 950;
            line-height: 1.1;
            color: var(--card-accent);
            letter-spacing: -0.045em;
            max-width: none;
            word-break: normal;
            overflow-wrap: normal;
        }}

        .ad-side-kpi-icon {{
            width: 54px;
            height: 54px;
            min-width: 54px;
            border-radius: 19px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: var(--card-soft);
            box-shadow: inset 0 0 0 1px rgba(255, 255, 255, .7);
        }}

        .ad-side-kpi-icon svg {{
            width: 27px;
            height: 27px;
        }}

        .ad-side-kpi-value {{
            font-size: 2.22rem;
            font-weight: 950;
            line-height: 1.02;
            letter-spacing: -0.06em;
            color: #0F172A;
            word-break: normal;
        }}

        .ad-side-kpi-value-text {{
            font-size: 1.58rem;
            line-height: 1.12;
            letter-spacing: -0.045em;
            word-break: normal;
            overflow-wrap: break-word;
        }}

        .ad-side-kpi-subtitle {{
            font-size: 0.96rem;
            font-weight: 750;
            line-height: 1.25;
            color: #52657A;
        }}
        
        /* ============================================================
        Tarjeta hero del aeropuerto seleccionado
        ============================================================ */

        .ad-airport-hero {{
            position: relative;
            width: 100%;
            padding: 1.35rem 1.35rem 1.25rem 1.35rem;
            border-radius: 30px;
            border: 1px solid color-mix(in srgb, var(--airport-accent) 32%, #DDE7F3);
            background:
                radial-gradient(circle at 92% 18%, var(--airport-soft) 0, transparent 34%),
                linear-gradient(180deg, #FFFFFF 0%, #F8FAFC 100%);
            box-shadow: 0 18px 42px rgba(15, 23, 42, 0.11);
            margin-bottom: 1.15rem;
            overflow: hidden;
        }}

        .ad-airport-hero::before {{
            content: "";
            position: absolute;
            inset: 0 auto 0 0;
            width: 8px;
            background: var(--airport-accent);
            border-radius: 30px 0 0 30px;
        }}

        .ad-airport-hero-top {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            margin-bottom: 0.8rem;
            padding-left: 0.35rem;
        }}

        .ad-airport-eyebrow {{
            display: inline-flex;
            align-items: center;
            width: fit-content;
            padding: 0.34rem 0.62rem;
            border-radius: 999px;
            background: var(--airport-soft);
            color: var(--airport-accent);
            font-size: 0.76rem;
            font-weight: 900;
            line-height: 1;
            letter-spacing: 0.015em;
            text-transform: uppercase;
        }}

        .ad-airport-hero-icon {{
            width: 54px;
            height: 54px;
            min-width: 54px;
            border-radius: 20px;
            display: grid;
            place-items: center;
            background: var(--airport-soft);
            box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.75);
        }}

        .ad-airport-hero-icon svg {{
            width: 28px;
            height: 28px;
        }}

        .ad-airport-hero-name {{
            padding-left: 0.35rem;
            color: #0F172A;
            font-size: 1.45rem;
            font-weight: 950;
            line-height: 1.03;
            letter-spacing: -0.06em;
            margin-bottom: 0.9rem;
        }}

        .ad-airport-hero-meta {{
            padding-left: 0.35rem;
            display: flex;
            flex-wrap: wrap;
            gap: 0.42rem;
        }}

        .ad-airport-meta-chip {{
            display: inline-flex;
            align-items: center;
            min-height: 1.85rem;
            padding: 0.35rem 0.58rem;
            border-radius: 999px;
            background: #F1F5F9;
            color: #475569;
            font-size: 0.82rem;
            font-weight: 800;
            line-height: 1;
        }}

        .ad-airport-meta-icao {{
            background: var(--airport-accent);
            color: #FFFFFF;
        }}
        
        
        
        /* ============================================================
        Botón rojo para limpiar selección
        ============================================================ */

        .st-key-clear_selection_action div.stButton > button,
        .st-key-clear-selection-action div.stButton > button,
        .st-key-clear_selection_action button,
        .st-key-clear-selection-action button {{
            background: #FEE2E2 !important;
            border: 1px solid #FCA5A5 !important;
            color: #B91C1C !important;
            font-weight: 900 !important;
            box-shadow: 0 10px 24px rgba(185, 28, 28, 0.12) !important;
        }}

        .st-key-clear_selection_action div.stButton > button:hover,
        .st-key-clear-selection-action div.stButton > button:hover,
        .st-key-clear_selection_action button:hover,
        .st-key-clear-selection-action button:hover {{
            background: #EF4444 !important;
            border-color: #DC2626 !important;
            color: #FFFFFF !important;
            transform: translateY(-1px);
            box-shadow: 0 16px 34px rgba(220, 38, 38, 0.24) !important;
        }}

        .st-key-clear_selection_action div.stButton > button:active,
        .st-key-clear-selection-action div.stButton > button:active,
        .st-key-clear_selection_action button:active,
        .st-key-clear-selection-action button:active {{
            background: #B91C1C !important;
            border-color: #991B1B !important;
            color: #FFFFFF !important;
            transform: translateY(0);
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def apply_active_layer_styles(active_layer: str) -> None:
    """Define variables CSS dinámicas según la capa activa."""

    cfg = LAYER_CONFIGS[active_layer]

    st.markdown(
        f"""
        <style>
        :root {{
            --active-layer-color: {cfg['color']};
            --active-layer-soft: {cfg['soft']};
            --active-layer-border: {cfg['color']}55;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )