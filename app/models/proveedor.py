from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base


class Proveedor(Base):
    __tablename__ = "proveedores"

    idProveedor: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        comment="Llave primaria. Identificador único e irrepetible para registrar y buscar cada proveedor sin duplicados.",
    )

    tipoProducto: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Campo de texto. Almacena la categoría o el tipo de servicio que ofrece el proveedor.",
    )

    usuario_identificacion: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("usuarios.identificacion", name="fk_proveedor_usuario1"),
        primary_key=True,
        autoincrement=False,
        comment="Llave foránea que conecta los atributos de la clase padre.",
    )
