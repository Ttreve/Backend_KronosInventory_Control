from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base


class OrdenCompra(Base):
    __tablename__ = "ordenesCompra"

    idOrdenesCompra: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=False,
        comment="Identificador único de la orden de compra.",
    )

    codigo: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Código de identificación asignado a la orden de compra.",
    )

    fechaOrden: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        comment="Fecha y hora en que se registra la orden de compra.",
    )

    cantidad: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        comment="Cantidad de unidades del producto solicitadas en la orden de compra.",
    )

    precioUnitario: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        comment="Precio de cada unidad del producto incluida en la orden de compra.",
    )

    estado: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Estado actual de la orden de compra, por ejemplo, pendiente, enviada o recibida.",
    )

    proveedor_idProveedor: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("proveedores.idProveedor", name="fk_ordenesCompra_proveedor1"),
        nullable=False,
        comment="Clave foránea que identifica al proveedor encargado de suministrar los productos de la orden.",
    )

    inventario_codInventario: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("inventarios.id", name="fk_ordenesCompra_inventario1"),
        nullable=False,
        comment="Clave foránea que identifica el producto del inventario incluido en la orden de compra.",
    )
