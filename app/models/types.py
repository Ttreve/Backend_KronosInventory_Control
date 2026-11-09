import enum

from sqlalchemy import Enum


def columna_enum(clase: type[enum.Enum], nombre: str, longitud: int = 20) -> Enum:
    """Enum guardado como VARCHAR con CHECK, igual que en Supabase."""
    return Enum(
        clase,
        name=nombre,
        native_enum=False,
        create_constraint=True,
        length=longitud,
        values_callable=lambda e: [m.value for m in e],
    )