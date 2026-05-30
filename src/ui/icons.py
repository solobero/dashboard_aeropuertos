from src.tokens import COLORS


SVG_PATHS = {
    "plane": '<path d="M2 16l20-10-7 18-4-7-7-1z"/><path d="M11 17l4 7"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "box": '<path d="M21 16V8a2 2 0 0 0-1-1.73L13 2.27a2 2 0 0 0-2 0L4 6.27A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><path d="M3.27 6.96L12 12.01l8.73-5.05"/><path d="M12 22.08V12"/>',
    "network": '<circle cx="12" cy="5" r="3"/><circle cx="5" cy="19" r="3"/><circle cx="19" cy="19" r="3"/><path d="M10.7 7.7L6.3 16.3"/><path d="M13.3 7.7l4.4 8.6"/><path d="M8 19h8"/>',
    "cloud": '<path d="M17.5 19H8a6 6 0 1 1 1.2-11.88A7 7 0 0 1 22 12a4.5 4.5 0 0 1-4.5 7z"/>',
    "pin": '<path d="M12 21s7-4.35 7-11a7 7 0 1 0-14 0c0 6.65 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4"/><path d="M8 2v4"/><path d="M3 10h18"/>',
    "filter": '<path d="M3 5h18"/><path d="M6 12h12"/><path d="M10 19h4"/>',
    "tower": '<path d="M7 22h10"/><path d="M12 2v20"/><path d="M8 7h8"/><path d="M9 12h6"/><path d="M10 17h4"/>',
    "eye": '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    "wind": '<path d="M3 8h12a3 3 0 1 0-3-3"/><path d="M3 12h18"/><path d="M3 16h12a3 3 0 1 1-3 3"/>',
}


def svg_icon(name: str, color: str = COLORS["blue"], size: int = 22) -> str:
    """Devuelve un ícono SVG inline, sin depender de imágenes externas."""
    path = SVG_PATHS.get(name, SVG_PATHS["plane"])
    return (
        f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
        f'stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{path}</svg>'
    )
