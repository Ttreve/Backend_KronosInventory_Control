from sqlalchemy import Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base


class Cliente(Base):
    __tablename__ = "clientes"

    idCliente: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        comment="Llave primaria y foránea. Hereda el identificador único de la tabla usuario para enlazar los datos personales del cliente.",
    )

    carritoActivo: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        comment="Campo booleano (TINYINT(1)). Funciona como bandera para indicar con un 1 o 0 si el cliente tiene un carrito de compras pendiente o activo.",
    )

    usuario_identificacion: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("usuarios.identificacion", name="fk_cliente_usuario1"),
        primary_key=True,
        autoincrement=False,
        comment="Llave foránea que conecta los atributos de la clase padre.",
    )
