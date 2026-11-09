from datetime import datetime

from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base
from app.models.mixins import UUIDPrimaryKeyMixin


class Categoria(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "categorias"

    nombre: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    descripcion: Mapped[str | None] = mapped_column(Text)
    icono: Mapped[str | None] = mapped_column(String(100))
    creado_en: Mapped[datetime | None] = mapped_column(DateTime, server_default=func.current_timestamp())