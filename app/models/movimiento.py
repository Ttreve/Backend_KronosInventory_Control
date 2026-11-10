from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base


class Movimiento(Base):
    __tablename__ = "movimientos"

    idMovimiento: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        comment="Clave primaria. Registro único de cada transacción de inventario.",
    )

    fechaMovimiento: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        comment="Fecha en la que se ejecuta el movimiento.",
    )

    precioUnitario: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        comment="Costo o valor unitario del producto al momento de realizar el movimiento.",
    )

    cantidad: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        comment="Cantidad de producto que entra o sale.",
    )

    subtotal: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        comment="Valor total de la transacción para ese lote de productos (precioUnitario por cantidad).",
    )

    tipoMovimiento: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        comment="Identificador del tipo de movimiento realizado (entrada, salida).",
    )

    usuario_identificacion: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("usuarios.identificacion", name="fk_movimiento_usuario1"),
        nullable=False,
        comment="Clave foránea que registra qué empleado o usuario del sistema realizó el movimiento.",
    )

    inventario_codInventario: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("inventarios.id", name="fk_movimiento_inventario1"),
        nullable=False,
        comment="Clave foránea que determina el producto relacionado con el movimiento.",
    )

    detalleVenta_idDetalleVenta: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("detalleVentas.idDetalleVenta", name="fk_movimiento_detalleVenta1"),
        nullable=False,
        comment="Clave foránea que relaciona el movimiento con el detalle de venta correspondiente.",
    )
