from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    identificacion: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=False,
        comment="Llave primaria. Código numérico único para identificar a cada usuario del sistema.",
    )

    nombre: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Campo de texto. Almacena el primer o segundo nombre de la persona.",
    )

    apellidos: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Campo de texto. Guarda los apellidos del usuario.",
    )

    correoElectronico: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Campo de texto. Registra el email para notificaciones e inicio de sesión.",
    )

    telefono: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        comment="Número de teléfono o celular de contacto.",
    )

    contrasena: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="Campo de texto. Guarda la clave encriptada para el acceso seguro al sistema.",
    )

    rol_idRol: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("roles.idRol", name="fk_usuario_rol1"),
        nullable=False,
        comment="Campo que referencia el identificador del rol asignado al usuario, permitiendo relacionar la tabla Usuario con la tabla Rol.",
    )

    direccion_idDireccion: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("direcciones.idDireccion", name="fk_usuario_direccion1"),
        nullable=False,
        comment="Clave foránea que vincula al usuario con su dirección residencial o comercial.",
    )
