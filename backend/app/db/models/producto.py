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

  