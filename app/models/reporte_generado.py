from datetime import datetime
from decimal import Decimal

from sqlalchemy import JSON, DateTime, Integer, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base
from app.models.mixins import UUIDPrimaryKeyMixin


class ReporteGenerado(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "reportes_generados"

    tipo: Mapped[str] = mapped_column(String(50), nullable=False)
    categoria: Mapped[str | None] = mapped_column(String(100))
    cantidad: Mapped[int | None] = mapped_column(Integer)
    fecha: Mapped[datetime | None] = mapped_column(DateTime, server_default=func.current_timestamp())
    filtros: Mapped[dict | None] = mapped_column(JSON)
    valor_total: Mapped[Decimal | None] = mapped_column(Numeric(14, 2))