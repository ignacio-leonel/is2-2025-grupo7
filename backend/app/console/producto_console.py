import sys #Para poder terminar el programa con sys.exit(0)
from backend.app.db.session import SessionLocal, init_db 
#SessionLocal crea un objeto session para hablar con la base de datos, init_db inicializa la base de datos (crea tablas si no existen).
from backend.app.db.models.producto import ProductoORM #importa el modelo ORM que representa la tabla productos.
from sqlalchemy.exc import IntegrityError #Para manejar errores de integridad en la base de datos.
from backend.app.console.validaciones import validar_producto, sku_unico #Trae Funciones de Validación

def listar_productos(session):
    try:
        productos = session.query(ProductoORM).all()  #trae todos los registros de la tabla productos
        if not productos:
            print("ℹ️ No hay productos registrados.")
            return
        print("\n--- Lista de Productos ---")
        for p in productos:
            print(f"[{p.id}] {p.nombre} (SKU: {p.sku}) - {p.categoria} - {p.unidad_medida}")
    except Exception as e:
        print(f"❌ Error al listar productos: {e}")

def agregar_producto(session):
    print("\n--- Agregar Producto ---")
    nombre = input("Nombre: ").strip()
    sku = input("SKU: ").strip()
    categoria = input("Categoría: ").strip()
    descripcion = input("Descripción: ").strip()
    unidad_medida = input("Unidad de medida: ").strip()

    #1- Validaciones de formato
    errores = validar_producto(nombre, sku, categoria, descripcion, unidad_medida)
    if errores:
        print("❌ " + "; ".join(errores))
        return

    #2- Validación de SKU único
    if not sku_unico(session, sku):
        print("❌ Error: ya existe un producto con ese SKU.")
        return

    # Crea el objeto ORM nuevo (es una fila de la tabla). 
    # session.add(nuevo): lo marca para inserción. 
    # session.commit(): guarda en la BD.
    try:
        nuevo = ProductoORM(
            nombre=nombre,
            sku=sku,
            categoria=categoria,
            descripcion=descripcion,
            unidad_medida=unidad_medida
        )
        session.add(nuevo)
        session.commit()
        print("✅ Producto agregado con éxito.")
    except IntegrityError:
        session.rollback()
        print("❌ Error de integridad en la base de datos.")
    except Exception as e:
        session.rollback()
        print(f"❌ Error al agregar producto: {e}")

def main():
    init_db()
    session = SessionLocal()
    try:
        while True:
            print("\n--- Consola de Productos ---")
            print("1. Listar productos")
            print("2. Agregar producto")
            print("3. Salir")
            opcion = input("Elige una opción: ").strip()

            if opcion == "1":
                listar_productos(session)
            elif opcion == "2":
                agregar_producto(session)
            elif opcion == "3":
                print("Saliendo...")
                break
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
    finally:
        session.close()
        sys.exit(0)

if __name__ == "__main__":
    main()