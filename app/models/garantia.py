from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import MEDIUMBLOB
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base


class Garantia(Base):
    __tablename__ = "garantias"

    idGarantia: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        comment="Llave primaria. Código numérico único para identificar cada tipo de póliza o término de garantía en el sistema.",
    )

    fechaInicio: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        comment="Fecha a partir de la cual empieza a regir la garantía (usualmente la fecha de compra o fabricación).",
    )

    fechaFin: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        comment="Fecha límite de vencimiento de la cobertura de la garantía.",
    )

    estado: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Estado de la garantía (ej. Activa, Vencida, En Reclamación).",
    )

    observacion: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Términos, condiciones especiales o notas sobre lo que cubre o no cubre la garantía.",
    )

    motivo: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Razón por la cual el cliente solicita hacer efectiva la garantía.",
    )

    tipoFalla: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Tipo de daño o defecto presentado por el producto.",
    )

    evidenciaImg: Mapped[bytes] = mapped_column(
        MEDIUMBLOB,
        nullable=False,
        comment="Imagen que sirve como evidencia del daño o falla reportada.",
    )

    detalleventa_idDetalleVenta: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("detalleVentas.idDetalleVenta", name="fk_garantia_detalleventa1"),
        nullable=False,
        comment="Clave foránea que relaciona la garantía con el artículo específico registrado en el detalle de la venta.",
    )
