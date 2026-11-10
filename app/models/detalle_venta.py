from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base


class DetalleVenta(Base):
    __tablename__ = "detalleVentas"

    idDetalleVenta: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        comment="Llave primaria. Código numérico único para identificar de forma individual cada renglón o artículo dentro de una orden de compra.",
    )

    subTotal: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        comment="Monto parcial calculado para este artículo en específico.",
    )

    cantidad: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        comment="Número de unidades vendidas de este artículo específico en esta venta.",
    )

    precioUnitario: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        comment="Precio al que se vendió cada unidad del artículo en ese momento.",
    )

    venta_idVenta: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("ventas.idVenta", name="fk_detalleVenta_venta1"),
        nullable=False,
        comment="Clave foránea que agrupa este detalle dentro del código de venta general.",
    )

    inventario_codInventario: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("inventarios.id", name="fk_detalleVenta_inventario1"),
        nullable=False,
        comment="Clave foránea que descuenta el producto del inventario.",
    )
