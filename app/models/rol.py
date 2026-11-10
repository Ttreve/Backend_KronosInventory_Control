from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base


class Rol(Base):
    __tablename__ = "roles"

    idRol: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=False,
        comment="Identificador único que permite distinguir cada rol registrado dentro del sistema.",
    )

    nombreRol: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Nombre que describe el tipo de rol asignado a un usuario dentro del sistema, como Jefe empleado cliente o proveedor.",
    )
