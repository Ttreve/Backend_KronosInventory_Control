from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base
from app.models.mixins import UUIDPrimaryKeyMixin


class Producto(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "productos"

    codigo: Mapped[str | None] = mapped_column(String(50), index=True)
    nombre: Mapped[str] = mapped_column(String(150), nullable=False)
    categoria: Mapped[str | None] = mapped_column(String(100))
    stock_actual: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    umbral_minimo: Mapped[int] = mapped_column(Integer, nullable=False, default=5)
    ubicacion: Mapped[str | None] = mapped_column(String(100))
    precio: Mapped[Decimal | None] = mapped_column(Numeric(12, 2))
    creado_en: Mapped[datetime | None] = mapped_column(DateTime, server_default=func.current_timestamp())
    categoria_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("categorias.id", ondelete="SET NULL")
    )
    imagen_url: Mapped[str | None] = mapped_column(Text)