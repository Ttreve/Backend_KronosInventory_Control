from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric, String
from sqlalchemy.dialects.mysql import MEDIUMBLOB
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base


class Inventario(Base):
    __tablename__ = "inventarios"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=False,
        comment="Llave primaria. Código numérico único para identificar cada artículo del inventario.",
    )

    codigo: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Código de identificación asignado al producto dentro del inventario.",
    )

    nombre: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Almacena el nombre comercial o descripción del artículo.",
    )

    stock: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        comment="Indica la cantidad física disponible en existencia dentro del inventario.",
    )

    umbralMinimo: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        comment="Cantidad mínima de existencias establecida para el producto antes de generar una alerta.",
    )

    precioVenta: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        comment="Valor de venta establecido para cada unidad del producto.",
    )

    modelo: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="Modelo o especificación técnica del producto.",
    )

    imagenProducto: Mapped[bytes] = mapped_column(
        MEDIUMBLOB,
        nullable=False,
        comment="Imagen del producto almacenada en formato binario.",
    )

    unidadMedida_idUnidadMedida: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("unidadVentas.idUnidadVenta", name="fk_inventario_unidadMedida1"),
        nullable=False,
        comment="Clave foránea que define cómo es la unidad de cada producto.",
    )

    marca_idMarca: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("marcas.idMarca", name="fk_inventario_marca1"),
        nullable=False,
        comment="Clave foránea que indica la marca del producto.",
    )

    categoria_idCategoria: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("categorias.idCategoria", name="fk_inventario_categoria1"),
        nullable=False,
        comment="Clave foránea que clasifica el producto en una categoría.",
    )
