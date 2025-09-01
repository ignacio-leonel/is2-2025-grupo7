from backend.app.models.producto import Producto
from backend.app.db import db  # Asegúrate de tener tu instancia de db

#Recibe un diccionario con los atributos del producto y lo agrega a la base de datos.
class ProductoRepository:
    @staticmethod
    def add(producto_data):
        producto = Producto(producto_data)
        db.session.add(producto)
        db.session.commit()
        return producto
#Devuelve una lista de todos los productos.
    @staticmethod
    def get_all():
        return Producto.query.all()