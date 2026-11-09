from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base
from app.models.mixins import UUIDPrimaryKeyMixin


class Proveedor(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "proveedores"

    nombre: Mapped[str] = mapped_column(String(150), nullable=False)
    nit: Mapped[str | None] = mapped_column(String(30))
    telefono: Mapped[str | None] = mapped_column(String(30))
    direccion: Mapped[str | None] = mapped_column(String(255))
    correo: Mapped[str | None] = mapped_column(String(150))
    tipo_producto: Mapped[str | None] = mapped_column(String(100))
    activo: Mapped[bool | None] = mapped_column(Boolean, default=True)
    creado_en: Mapped[datetime | None] = mapped_column(DateTime, server_default=func.current_timestamp())
    perfil_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("perfiles.id", ondelete="SET NULL")
    )