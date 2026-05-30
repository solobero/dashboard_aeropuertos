from __future__ import annotations

import pandas as pd

MONTHS_ES = {
    1: "ene",
    2: "feb",
    3: "mar",
    4: "abr",
    5: "may",
    6: "jun",
    7: "jul",
    8: "ago",
    9: "sep",
    10: "oct",
    11: "nov",
    12: "dic",
}

AIRPORT_TYPE_LABELS = {
    "large_airport": "Aeropuerto grande",
    "medium_airport": "Aeropuerto mediano",
    "small_airport": "Aeropuerto pequeño",
    "closed": "Cerrado",
    "heliport": "Helipuerto",
    "seaplane_base": "Base de hidroaviones",
    "balloonport": "Aeródromo de globos",
    "Sin tipo": "Sin tipo",
}

REGION_LABELS = {
    "Amazonas Department": "Amazonas",
    "Antioquía Department": "Antioquia",
    "Arauca Department": "Arauca",
    "Atlántico Department": "Atlántico",
    "Bogotá Capital District": "Bogotá D.C.",
    "Bolívar Department": "Bolívar",
    "Caldas Department": "Caldas",
    "Caquetá Department": "Caquetá",
    "Casanare Department": "Casanare",
    "Cauca Department": "Cauca",
    "Chocó Department": "Chocó",
    "Cundinamarca Department": "Cundinamarca",
    "César Department": "Cesar",
    "Córdoba Department": "Córdoba",
    "Guainía Department": "Guainía",
    "Guaviare Department": "Guaviare",
    "Huila Department": "Huila",
    "La Guajira Department": "La Guajira",
    "Magdalena Department": "Magdalena",
    "Meta Department": "Meta",
    "Nariño Department": "Nariño",
    "Norte de Santander Department": "Norte de Santander",
    "Putumayo Department": "Putumayo",
    "Quindio Department": "Quindío",
    "Risaralda Department": "Risaralda",
    "San Andrés, Providencia y Santa Catalina Department": "San Andrés y Providencia",
    "Santander Department": "Santander",
    "Sucre Department": "Sucre",
    "Tolima Department": "Tolima",
    "Valle del Cauca Department": "Valle del Cauca",
    "Vaupés Department": "Vaupés",
    "Vichada Department": "Vichada",
    "Sin región": "Sin región",
}


def display_airport_type(value: str | None) -> str:
    """Devuelve una etiqueta en español para el tipo de aeropuerto."""
    if value is None or pd.isna(value):
        return "Sin tipo"
    return AIRPORT_TYPE_LABELS.get(str(value), str(value).replace("_", " ").title())


def display_region(value: str | None) -> str:
    """Devuelve una etiqueta en español para el departamento o región."""
    if value is None or pd.isna(value):
        return "Sin región"
    return REGION_LABELS.get(str(value), str(value).replace(" Department", ""))


def display_month(value) -> str:
    """Formatea una fecha mensual como 'ene 2020'."""
    ts = pd.to_datetime(value)
    return f"{MONTHS_ES[int(ts.month)]} {int(ts.year)}"
