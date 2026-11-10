from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base


class Venta(Base):
    __tablename__ = "ventas"

    idVenta: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        comment="Llave primaria. Código numérico único para identificar y rastrear cada transacción de compra realizada.",
    )

    descuento: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        comment="Campo numérico. Guarda el porcentaje o monto deducido del precio original de la transacción.",
    )

    fechaVenta: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        comment="Fecha en la que se procesó la venta.",
    )

    estado: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Situación de la venta (ej. Pendiente, Pagado, Cancelado).",
    )

    totalVenta: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        comment="Monto total final cobrado al cliente.",
    )

    comprobantePago: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Referencia, enlace o número del recibo o comprobante de la transacción bancaria o de caja.",
    )

    metodoPago: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Forma en que pagó el cliente (ej. Efectivo, Tarjeta, Transferencia).",
    )

    cliente_idCliente: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("clientes.idCliente", name="fk_venta_cliente1"),
        nullable=False,
        comment="Clave foránea que identifica al cliente que realizó la compra.",
    )
