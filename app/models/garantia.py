from datetime import datetime
from decimal import Decimal

from sqlalchemy import JSON, DateTime, ForeignKey, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.enums.estados import EstadoGarantia
from app.infrastructure.database.base import Base
from app.models.mixins import UUIDPrimaryKeyMixin
from app.models.types import columna_enum


class Garantia(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "garantias"

    orden_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("ordenes_compra.id", ondelete="SET NULL")
    )
    numero_orden: Mapped[str | None] = mapped_column(String(50))
    cliente_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("perfiles.id", ondelete="SET NULL")
    )
    cliente_nombre: Mapped[str | None] = mapped_column(String(150))
    producto: Mapped[str | None] = mapped_column(String(150))
    motivo: Mapped[str | None] = mapped_column(Text)
    estado: Mapped[EstadoGarantia] = mapped_column(
        columna_enum(EstadoGarantia, "estado_garantia"), nullable=False, default=EstadoGarantia.PENDIENTE
    )
    observacion: Mapped[str | None] = mapped_column(Text)
    fecha: Mapped[datetime | None] = mapped_column(DateTime, server_default=func.current_timestamp())
    bitacora: Mapped[list | None] = mapped_column(JSON)
    observaciones: Mapped[list | None] = mapped_column(JSON)
    imagen_nombre: Mapped[str | None] = mapped_column(String(255))
    cliente_destino: Mapped[str | None] = mapped_column(String(150))
    correo: Mapped[str | None] = mapped_column(String(150))
    numero_factura: Mapped[str | None] = mapped_column(String(50))
    precio: Mapped[Decimal | None] = mapped_column(Numeric(12, 2))
    tipo_falla: Mapped[str | None] = mapped_column(String(100))
    tipo: Mapped[str | None] = mapped_column(String(50))
    numero_solicitud: Mapped[str | None] = mapped_column(String(50))
    observacion_inicial: Mapped[str | None] = mapped_column(Text)
    observacion_actual: Mapped[str | None] = mapped_column(Text)
    fecha_creacion: Mapped[datetime | None] = mapped_column(DateTime, server_default=func.current_timestamp())
    fecha_finalizacion: Mapped[datetime | None] = mapped_column(DateTime)