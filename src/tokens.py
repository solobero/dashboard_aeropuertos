# Paleta principal de color. Se centraliza para mantener consistencia visual.
COLORS = {
    "bg": "#F8FAFC",
    "surface": "#FFFFFF",
    "surface_soft": "#F1F5F9",
    "border": "#E2E8F0",
    "text": "#0F172A",
    "muted": "#64748B",
    "blue": "#2563EB",
    "blue_soft": "#DBEAFE",
    "cyan": "#0891B2",
    "cyan_soft": "#CFFAFE",
    "green": "#10B981",
    "green_soft": "#D1FAE5",
    "purple": "#7C3AED",
    "purple_soft": "#EDE9FE",
    "rose": "#E11D48",
    "rose_soft": "#FFE4E6",
    "orange": "#F97316",
    "orange_soft": "#FFEDD5",
    "red": "#EF4444",
    "red_soft": "#FEE2E2",
    "yellow": "#F59E0B",
    "yellow_soft": "#FEF3C7",
    "graphite": "#111827",
    "graphite_soft": "#E5E7EB",
}

# Colores de burbujas no meteorológicas: bajo → medio → alto.
# En estas capas, el tamaño y el color codifican magnitud.
VALUE_SCALE_COLORS = {
    "low": "#EF4444",      # rojo: valor bajo
    "mid": "#F59E0B",      # amarillo/naranja: valor medio
    "high": "#16A34A",     # verde: valor alto
    "missing": "#94A3B8",  # gris: sin dato
}

# Configuración de capas reales del dataset.
LAYER_CONFIGS = {
    "operacion": {
        "label": "Operación",
        "title": "Actividad aeroportuaria registrada",
        "description": "Tamaño y color reflejan operaciones acumuladas: llegadas, salidas y otras operaciones del periodo seleccionado. Unidad: operaciones.",
        "icon": "plane",
        "color": COLORS["blue"],
        "soft": COLORS["blue_soft"],
        "metric": "operaciones_total",
        "display": "Operaciones",
        "unit": "operaciones",
        "unit_label": "operaciones",
        "agg": "sum",
    },
    "pasajeros": {
        "label": "Pasajeros",
        "title": "Flujo de viajeros por aeropuerto",
        "description": "Tamaño y color muestran personas movilizadas en el periodo. Unidad: pasajeros registrados.",
        "icon": "users",
        "color": COLORS["green"],
        "soft": COLORS["green_soft"],
        "metric": "pasajeros_total",
        "display": "Pasajeros",
        "unit": "personas",
        "unit_label": "pasajeros",
        "agg": "sum",
    },
    "carga": {
        "label": "Carga",
        "title": "Movimiento logístico de mercancías",
        "description": "Tamaño y color resumen mercancías movilizadas por aeropuerto. Unidad visual: toneladas.",
        "icon": "box",
        "color": COLORS["purple"],
        "soft": COLORS["purple_soft"],
        "metric": "carga_total_kg",
        "display": "Carga",
        "unit": "kg",
        "unit_label": "toneladas",
        "agg": "sum",
    },
    "conectividad": {
        "label": "Conectividad",
        "title": "Conexión territorial del aeropuerto",
        "description": "Permite explorar destinos, orígenes y empresas registradas. Unidad: promedio de la métrica seleccionada.",
        "icon": "network",
        "color": COLORS["graphite"],
        "soft": COLORS["graphite_soft"],
        "metric": "n_destinos_total",
        "display": "Destinos",
        "unit": "destinos",
        "unit_label": "destinos promedio",
        "agg": "mean",
    },
    "clima": {
        "label": "Clima",
        "title": "Condiciones meteorológicas observadas",
        "description": "Color refleja porcentaje promedio de reportes METAR con lluvia, niebla, baja visibilidad, viento fuerte o IFR aproximado. Unidad: porcentaje (%).",
        "icon": "cloud",
        "color": COLORS["cyan"],
        "soft": COLORS["cyan_soft"],
        "metric": "prop_lluvia",
        "display": "Lluvia",
        "unit": "%",
        "unit_label": "% de reportes METAR",
        "agg": "mean",
    },
}

# Subcapas meteorológicas soportadas por columnas reales del dataset.
CLIMATE_METRICS = {
    "Lluvia": "prop_lluvia",
    "Niebla": "prop_niebla",
    "Tormenta": "prop_tormenta",
    "Baja visibilidad": "prop_baja_visibilidad",
    "Viento fuerte": "prop_viento_fuerte",
    "IFR aprox.": "prop_ifr_aprox",
}

# Submétricas de conectividad soportadas por columnas reales del dataset.
CONNECTIVITY_METRICS = {
    "Destinos": "n_destinos_total",
    "Orígenes": "n_origenes_total",
    "Empresas salida": "n_empresas_salida",
    "Empresas llegada": "n_empresas_llegada",
}

# Columnas que NO deben usarse en esta herramienta porque pertenecen al modelo o al target.
MODEL_COLUMNS_TO_HIDE = {
    "target_operaciones_total_mes_siguiente",
    "target_q33_operaciones",
    "target_q66_operaciones",
    "target_nivel_operacion_mes_siguiente",
}
