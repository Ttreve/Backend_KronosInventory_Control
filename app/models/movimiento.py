from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.enums.estados import TipoMovimiento
from app.infrastructure.database.base import Base
from app.models.mixins import UUIDPrimaryKeyMixin
from app.models.types import columna_enum


class Movimiento(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "movimientos"

    producto_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("productos.id", ondelete="SET NULL"), index=True
    )
    tipo: Mapped[TipoMovimiento] = mapped_column(columna_enum(TipoMovimiento, "tipo_movimiento"), nullable=False)
    cantidad: Mapped[int] = mapped_column(Integer, nullable=False)
    motivo: Mapped[str | None] = mapped_column(Text)
    responsable: Mapped[str | None] = mapped_column(String(150))
    fecha: Mapped[datetime | None] = mapped_column(DateTime, server_default=func.current_timestamp())