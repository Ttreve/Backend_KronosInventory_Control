from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base


class Categoria(Base):
    __tablename__ = "categorias"

    idCategoria: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=False,
        comment="Clave primaria. Identificador de la categoría del producto.",
    )

    nombreCategoria: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Nombre de la categoría.",
    )
