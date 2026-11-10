from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base


class Alerta(Base):
    __tablename__ = "alertas"

    idalertas: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=False,
        comment="Identificador único de cada alerta generada en el sistema.",
    )

    estado: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Estado actual de la alerta, por ejemplo, pendiente o atendida.",
    )

    mensaje: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Descripción breve del motivo o situación que generó la alerta.",
    )

    fechaAlerta: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        comment="Fecha y hora en que se generó la alerta.",
    )

    inventario_codInventario: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("inventarios.id", name="fk_alertas_inventario1"),
        nullable=False,
        comment="Clave foránea que identifica el producto del inventario relacionado con la alerta.",
    )
