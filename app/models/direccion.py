from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base


class Direccion(Base):
    __tablename__ = "direcciones"

    idDireccion: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        comment="Llave primaria. Identificador único asignado automáticamente para registrar y organizar cada domicilio en el sistema.",
    )

    barrio: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Campo de texto. Almacena el nombre del vecindario, zona o sector residencial de la dirección.",
    )

    ciudad: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Campo de texto. Registra el municipio o la ciudad donde se ubica el domicilio.",
    )

    localidad: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Campo de texto. Guarda la subdivisión administrativa o comuna interna de la ciudad, útil para la logística de envíos.",
    )

    direccionCompleta: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
        comment="Dirección completa del domicilio, incluyendo nomenclatura y detalles necesarios para ubicarlo.",
    )
