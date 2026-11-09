from decimal import Decimal

from sqlalchemy import CheckConstraint, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base
from app.models.mixins import UUIDPrimaryKeyMixin


class DetalleVenta(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "detalle_ventas"
    __table_args__ = (CheckConstraint("cantidad > 0", name="ck_detalle_ventas_cantidad"),)

    venta_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("ventas.id", ondelete="CASCADE"), nullable=False, index=True
    )
    producto_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("productos.id", ondelete="SET NULL")
    )
    producto_nombre: Mapped[str | None] = mapped_column(String(150))
    cantidad: Mapped[int] = mapped_column(Integer, nullable=False)
    precio_unitario: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    subtotal: Mapped[Decimal | None] = mapped_column(Numeric(14, 2))