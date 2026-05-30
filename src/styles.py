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
        div[data-testid="stVerticalBlock"] {{ gap: 0.85rem; }}
        .ad-brand {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            font-weight: 800;
            font-size: 1.45rem;
            color: {COLORS['text']};
            letter-spacing: -0.03em;
            white-space: nowrap;
        }}
        .ad-brand span {{ color: {COLORS['blue']}; }}
        .ad-logo {{
            width: 38px;
            height: 38px;
            border-radius: 12px;
            background: linear-gradient(135deg, {COLORS['blue']}, {COLORS['cyan']});
            display: grid;
            place-items: center;
            color: white;
            box-shadow: 0 10px 24px rgba(37, 99, 235, .25);
        }}
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
        .ad-kpi-number {{
            font-weight: 850;
            font-size: 1.9rem;
            letter-spacing: -0.04em;
            color: {COLORS['text']};
            margin-top: .35rem;
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

        .ad-layer-nav {{
            display: grid;
            grid-template-columns: repeat(5, minmax(0, 1fr));
            gap: .65rem;
            align-items: center;
        }}
        .ad-layer-chip {{
            height: 3.1rem;
            border-radius: 17px;
            border: 1px solid {COLORS['border']};
            background: #FFFFFF;
            color: {COLORS['text']};
            text-decoration: none !important;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: .45rem;
            font-weight: 700;
            box-shadow: 0 8px 24px rgba(15, 23, 42, .045);
            transition: color .15s ease, background .15s ease, border-color .15s ease, transform .15s ease, box-shadow .15s ease;
        }}
        .ad-layer-chip:hover {{
            color: var(--layer-color);
            background: var(--layer-soft);
            border-color: var(--layer-color);
            transform: translateY(-1px);
            box-shadow: 0 14px 30px rgba(15, 23, 42, .075);
        }}
        .ad-layer-chip.is-active {{
            color: var(--layer-color);
            background: linear-gradient(180deg, #FFFFFF, var(--layer-soft));
            border-color: var(--layer-color);
            box-shadow: 0 14px 34px rgba(15, 23, 42, .08);
        }}
        .ad-layer-icon {{ display: grid; place-items: center; }}

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
        .ad-layer-context:hover {{ border-color: var(--layer-color); }}
        .ad-layer-context-icon {{
            width: 42px;
            height: 42px;
            border-radius: 15px;
            display: grid;
            place-items: center;
            background: var(--layer-soft);
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
        .ad-covid-chip {{
            display: inline-flex;
            align-items: center;
            gap: .45rem;
            width: fit-content;
            margin: 0 0 .35rem 0;
            padding: .45rem .72rem;
            border-radius: 999px;
            border: 1px solid #FDBA74;
            background: #FFF7ED;
            color: #9A3412;
            font-size: .80rem;
            font-weight: 650;
        }}
        .ad-covid-chip span {{
            font-weight: 900;
            color: #C2410C;
        }}

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
        label:hover, .stRadio:hover label {{ color: var(--active-layer-color, {COLORS['blue']}) !important; }}
        .folium-map {{
            border-radius: 24px !important;
            overflow: hidden;
        }}
        iframe {{
            border-radius: 24px !important;
        }}

        /* La marca del encabezado vuelve a la portada en la misma pestaña. */
        .ad-brand-link,
        .ad-brand-link:visited,
        .ad-brand-link:hover,
        .ad-brand-link:active {{
            text-decoration: none !important;
            color: inherit !important;
        }}

        .ad-app-header .ad-brand,
        .ad-app-header .ad-brand * {{
            cursor: pointer !important;
            pointer-events: auto !important;
            text-decoration: none !important;
        }}

        .ad-landing {{
            min-height: 100vh;
            display: grid;
            grid-template-columns: 0.95fr 1.25fr;
            align-items: center;
            gap: 2rem;
            padding: 3.2rem 4rem;
            background: radial-gradient(circle at 20% 15%, #DBEAFE 0, transparent 30%), radial-gradient(circle at 95% 20%, #CFFAFE 0, transparent 24%), linear-gradient(135deg, #F8FAFC, #EEF6FF);
        }}
        .ad-landing-spacer {{
            height: clamp(2rem, 9vh, 7rem);
        }}
        .ad-landing-title {{
            color: {COLORS['text']};
            font-size: clamp(2.2rem, 4.5vw, 4.7rem);
            line-height: .98;
            letter-spacing: -0.07em;
            font-weight: 900;
            margin: 1rem 0 2rem 0;
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
        }}
        .ad-landing-subtitle {{
            max-width: 680px;
            margin-top: -1rem;
            margin-bottom: 1.3rem;
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

        .ad-landing-copy-only {{
            padding: 2rem 1.5rem 2rem 3rem;
        }}
        .ad-landing-brand {{
            margin-bottom: 2rem;
        }}
        button[data-testid="stBaseButton-primary"] {{
            min-height: 3.35rem;
            padding-left: 1.35rem !important;
            padding-right: 1.35rem !important;
        }}
        .ad-landing-cta {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-height: 3.35rem;
            border-radius: 18px;
            background: {COLORS['blue']};
            color: white !important;
            border: 1px solid {COLORS['blue']};
            padding: 0 1.35rem;
            font-weight: 800;
            text-decoration: none !important;
            box-shadow: 0 18px 36px rgba(37, 99, 235, .25);
            transition: background .15s ease, transform .15s ease, box-shadow .15s ease;
        }}
        .ad-landing-cta:hover {{
            background: #1D4ED8;
            transform: translateY(-1px);
            box-shadow: 0 24px 46px rgba(37, 99, 235, .30);
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
