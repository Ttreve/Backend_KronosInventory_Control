from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.enums.user_role import UserRole
from app.infrastructure.database.base import Base
from app.models.mixins import UUIDPrimaryKeyMixin
from app.models.types import columna_enum


class Perfil(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "perfiles"

    nombre: Mapped[str | None] = mapped_column(String(100))
    apellido: Mapped[str | None] = mapped_column(String(100))
    telefono: Mapped[str | None] = mapped_column(String(30))
    direccion: Mapped[str | None] = mapped_column(String(255))
    localidad: Mapped[str | None] = mapped_column(String(100))
    barrio: Mapped[str | None] = mapped_column(String(100))
    rol: Mapped[UserRole] = mapped_column(
        columna_enum(UserRole, "user_role"),
        nullable=False,
        default=UserRole.CLIENTE,
    )
    creado_en: Mapped[datetime | None] = mapped_column(DateTime, server_default=func.current_timestamp())