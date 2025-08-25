

from pydantic import BaseModel


class Producto(BaseModel):
    name: str
    price: float
    stock: int
    

class ProductoCreate(Producto):
    pass

class ProductoUpdate(Producto):
    pass


class ProductoRead(Producto):
    id: int
    
    class config:
        orm_mode = True