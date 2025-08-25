

from pydantic import BaseModel


class ProductoBase(BaseModel):
    name: str
    price: float
    stock: int
    

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdatte(ProductoBase):
    pass


class ProductoRead(BaseModel):
    id: int
    
    class config:
        orm_mode = True