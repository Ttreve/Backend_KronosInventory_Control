import enum


class UserRole(str, enum.Enum):
    """Roles del sistema (los mismos que usa el frontend)."""

    JEFE = "jefe"
    ADMINISTRADOR = "administrador"
    EMPLEADO = "empleado"
    CLIENTE = "cliente"
    PROVEEDOR = "proveedor"