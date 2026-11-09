from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.enums.estados import EstadoVenta
from app.infrastructure.database.base import Base
from app.models.mixins import UUIDPrimaryKeyMixin
from app.models.types import columna_enum


class Venta(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "ventas"

    cliente_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("perfiles.id", ondelete="SET NULL")
    )
    cliente_nombre: Mapped[str | None] = mapped_column(String(150))
    descuento: Mapped[Decimal | None] = mapped_column(Numeric(12, 2), default=0)
    total: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)
    metodo_pago: Mapped[str | None] = mapped_column(String(50))
    comprobante_pago: Mapped[str | None] = mapped_column(Text)
    estado: Mapped[EstadoVenta] = mapped_column(
        columna_enum(EstadoVenta, "estado_venta"), nullable=False, default=EstadoVenta.PENDIENTE
    )
    fecha: Mapped[datetime | None] = mapped_column(DateTime, server_default=func.current_timestamp())