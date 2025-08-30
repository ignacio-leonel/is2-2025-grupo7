from dataclasses import dataclass, field
from typing import Optional,List
from .movimiento import Movimiento 
@dataclass
class Producto:
    id: int
    nombre: str
    sku: str
    categoria: str
    descripcion: Optional[str] = None #Puede no tener valor
    stock_global: int = field(default=0, init=False) #No se pasa en el constructor; es Calculado
    movimientos: List[Movimiento] = field(default_factory=list) #Relación Producto → Movimiento