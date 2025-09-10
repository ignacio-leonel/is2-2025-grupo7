from sqlalchemy import Column, Integer, String, Float
from backend.app.db.base import Base

# Modelo ORM para productos
class ProductoORM(Base):
    __tablename__ = "producto"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True)         # Nombre único
    descripcion = Column(String, nullable=True)  # Descripción opcional
    precio = Column(Float)                        # Precio del producto
    stock = Column(Integer)                       # Cantidad en stock
    categoria = Column(String, nullable=True)    # Categoría opcional
