from dataclasses import dataclass, field
from typing import List
from .movimiento import Movimiento 

@dataclass
class Usuario:
    id: int
    username: str
    email: str
    is_active: bool
    movimientos: List[Movimiento] = field(default_factory=list)  # Relación Usuario → Movimiento