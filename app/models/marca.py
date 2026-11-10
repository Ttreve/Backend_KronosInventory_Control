from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base


class Marca(Base):
    __tablename__ = "marcas"

    idMarca: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        comment="Clave primaria. Identificador de la marca comercial del producto.",
    )

    nombreMarca: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Nombre de la marca.",
    )
