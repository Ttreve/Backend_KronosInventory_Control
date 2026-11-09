import enum


class TipoMovimiento(str, enum.Enum):
    ENTRADA = "entrada"
    SALIDA = "salida"


class EstadoOrden(str, enum.Enum):
    PENDIENTE = "pendiente"
    CONFIRMADA = "confirmada"
    RECHAZADA = "rechazada"


class OrigenOrden(str, enum.Enum):
    INTERNO = "interno"
    CLIENTE = "cliente"


class EstadoGarantia(str, enum.Enum):
    PENDIENTE = "pendiente"
    EN_REVISION = "en_revision"
    APROBADA = "aprobada"
    RECHAZADA = "rechazada"


class EstadoVenta(str, enum.Enum):
    PAGADO = "pagado"
    PENDIENTE = "pendiente"
    ANULADA = "anulada"