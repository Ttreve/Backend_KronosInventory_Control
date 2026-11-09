from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.enums.estados import EstadoOrden, OrigenOrden
from app.infrastructure.database.base import Base
from app.models.mixins import UUIDPrimaryKeyMixin
from app.models.types import columna_enum


class OrdenCompra(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "ordenes_compra"

    codigo: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    producto_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("productos.id", ondelete="SET NULL")
    )
    producto_nombre: Mapped[str | None] = mapped_column(String(150))
    cantidad: Mapped[int] = mapped_column(Integer, nullable=False)
    proveedor_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("proveedores.id", ondelete="SET NULL")
    )
    proveedor_nombre: Mapped[str | None] = mapped_column(String(150))
    cliente_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("perfiles.id", ondelete="SET NULL")
    )
    cliente_nombre: Mapped[str | None] = mapped_column(String(150))
    precio_unitario: Mapped[Decimal | None] = mapped_column(Numeric(12, 2))
    origen: Mapped[OrigenOrden] = mapped_column(columna_enum(OrigenOrden, "origen_orden"), nullable=False)
    estado: Mapped[EstadoOrden] = mapped_column(
        columna_enum(EstadoOrden, "estado_orden"), nullable=False, default=EstadoOrden.PENDIENTE
    )
    observacion: Mapped[str | None] = mapped_column(Text)
    fecha: Mapped[datetime | None] = mapped_column(DateTime, server_default=func.current_timestamp())