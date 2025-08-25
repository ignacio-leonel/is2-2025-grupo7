# app/domain/models/producto.py
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Producto:
    id: int
    nombre: str
    sku: str
    descripcion: Optional[str] = None #Puede no tener valor
    stock_global: int = field(default=0, init=False) #No se pasa en el constructor; es Calculado