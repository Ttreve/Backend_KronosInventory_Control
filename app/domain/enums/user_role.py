import enum


class UserRole(enum.IntEnum):
    """Ids de la tabla `roles` (se usarán en la autenticación)."""

    CLIENTE = 1
    PROVEEDOR = 2
    JEFE = 3
    EMPLEADO = 4