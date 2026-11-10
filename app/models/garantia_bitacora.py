from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base


class GarantiaBitacora(Base):
    __tablename__ = "garantiaBitacoras"

    idBitacoras: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=False,
        comment="Identificador único de cada registro de seguimiento de una garantía.",
    )

    fechaRegistro: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        comment="Fecha y hora en que se registra una actualización o seguimiento de la garantía.",
    )

    estado: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Estado de la garantía en el momento del seguimiento registrado.",
    )

    comentario: Mapped[str | None] = mapped_column(
        String(45),
        comment="Observación adicional sobre el seguimiento de la garantía.",
    )

    garantia_idGarantia: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("garantias.idGarantia", name="fk_garantiaBitacoras_garantia1"),
        nullable=False,
        comment="Clave foránea que relaciona el registro de seguimiento con la garantía correspondiente.",
    )
