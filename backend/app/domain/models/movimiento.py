from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional
from .producto import Producto
from .deposito import Deposito
from .usuario import Usuario
class TipoMovimiento(str, Enum):
    INGRESO = "ingreso"
    EGRESO = "egreso"
    TRASLADO = "traslado"
@dataclass
class Movimiento:
    id: Optional[int]
    producto: Producto # referencia al producto
    deposito_origen: Optional[Deposito]  # depósito de origen, opcional porque un ingreso solo requiere depósito destino
    deposito_destino: Optional[Deposito] # depósito de destino, opcional porque un egreso solo requiere depósito origen
    usuario: Usuario   # usuario que realiza el movimiento
    cantidad: int
    fecha: datetime
    tipo: TipoMovimiento



