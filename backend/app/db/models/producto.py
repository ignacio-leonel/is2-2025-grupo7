from sqlalchemy import Column, Integer, String
from backend.app.db.base import base # clase de la base de dato de SQLAlchemy

class ProductoORM(base):
    __tablename__ = "productos"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    sku = Column(String, unique=True, index=True)
    categoria = Column(String)
    descripcion = Column(String)
    unidad_medida = Column(String)