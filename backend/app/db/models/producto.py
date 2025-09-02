<<<<<<< HEAD
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ProductORM(Base):
    __tablename__= "products"

    id= Column(Integer, primary_key=True, autoincrement=True)
    nombre=Column(String, nullable=False)
    SKU=Column(String, unique=True, nullable=False)
    categoria=Column(String, nullable=False)
    descripcion=Column(String)
    unidad_medida=Column(Integer, nullable=False )

  
=======

""""

class ProductORM:
    def __init__(self, id, nombre, SKU, categoria, descripcion, unidad_medida):
        self.id= id
        self.nombre = nombre
        self.SKU = SKU
        self.categoria = categoria
        self.descripcion = descripcion
        self.unidad_medida = unidad_medida

esta clase solo existia en memoria, no estaba conectada a una base de datos real

"""

# necesito que se rechace duplicados para que alembic pueda crear las migraciones

from sqlalchemy import Column, Integer, String
from backend.app.db.base import Base # clase de la base de dato de SQLAlchemy


class ProductoORM(Base):
    __tablename__ = "productos"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique = True, index = True)
    sku = Column(String, unique = True, index = True)
    categoria = Column(String)
    descripcion = Column(String)
    unidad_medida = Column(String)
    
    
    
    
>>>>>>> origin/master
