import uuid

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


def generar_uuid() -> str:
    return str(uuid.uuid4())


class UUIDPrimaryKeyMixin:
    """Llave primaria uuid guardada como texto de 36 caracteres."""

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generar_uuid)