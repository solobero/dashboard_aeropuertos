import math


def format_number(value: float | int | None, decimals: int = 0) -> str:
    """Formatea números con separador de miles en estilo español."""
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return "—"
    return f"{value:,.{decimals}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def format_compact(value: float | int | None) -> str:
    """Convierte números grandes a formato compacto para tarjetas y tooltips."""
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return "—"
    abs_value = abs(value)
    if abs_value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.1f} B".replace(".", ",")
    if abs_value >= 1_000_000:
        return f"{value / 1_000_000:.1f} M".replace(".", ",")
    if abs_value >= 1_000:
        return f"{value / 1_000:.1f} K".replace(".", ",")
    return format_number(value, 0)


def format_metric(value: float | int | None, unit: str = "") -> str:
    """Formatea métricas según unidad de negocio.

    Nota: las proporciones meteorológicas llegan como 0.12, pero se
    muestran como 12,0 %. La carga llega en kg y se muestra en toneladas.
    """
    if unit == "%":
        return f"{format_number((value or 0) * 100, 1)} %"
    if unit == "kg":
        tonnes = (value or 0) / 1000
        return f"{format_compact(tonnes)} t"
    return format_compact(value)


def unit_display_name(unit: str) -> str:
    """Devuelve etiqueta corta de unidad para ejes, leyendas y subtítulos."""
    mapping = {
        "%": "% de reportes METAR",
        "kg": "toneladas",
        "operaciones": "operaciones",
        "personas": "pasajeros",
        "destinos": "destinos promedio",
        "orígenes": "orígenes promedio",
        "empresas": "empresas promedio",
    }
    return mapping.get(unit, unit or "valor")


def convert_for_visual(value, unit: str):
    """Convierte valores crudos a la unidad visual usada en gráficos."""
    if unit == "%":
        return value * 100
    if unit == "kg":
        return value / 1000
    return value


def format_month_label(value) -> str:
    """Convierte una fecha mensual a etiqueta corta legible."""
    return value.strftime("%Y-%m")
