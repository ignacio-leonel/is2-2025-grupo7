from dataclasses import dataclass,field
from typing import List
from .movimiento import Movimiento 

@dataclass
class Deposito:
    id: int
    nombre: str
    ubicacion: str
    movimientos_origen: List[Movimiento] = field(default_factory=list)   # Relación Depósito → Movimientos como origen
    movimientos_destino: List[Movimiento] = field(default_factory=list)  # Relación Depósito → Movimientos como destino