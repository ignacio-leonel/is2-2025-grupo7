from dataclasses import dataclass
from datetime import datetime
from .producto import Producto
from .deposito import Deposito
from .usuario import Usuario

@dataclass
class Movimiento:
    id: int
    producto: Producto                  # referencia al producto
    deposito_origen: Deposito           # depósito de origen
    deposito_destino: Deposito          # depósito de destino
    usuario: Usuario                    # usuario que realiza el movimiento
    cantidad: int
    fecha: datetime
    tipo: str  # 'ingreso', 'egreso', 'traslado'