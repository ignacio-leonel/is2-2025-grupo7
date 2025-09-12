# Este módulo permite paginar una lista de objetos Producto en consola.
# El usuario puede elegir cuántos productos ver por página y navegar entre páginas.
# Cada producto se muestra con sus atributos principales y el listado está numerado globalmente.

def paginar_productos(productos):
    """
    Muestra una lista paginada y numerada de objetos Producto en consola.
    Permite al usuario elegir la cantidad de productos por página y navegar entre páginas.
    """
    total = len(productos)
    if total == 0:
        print("No hay productos para mostrar.")
        return

    por_pagina = int(input("¿Cuántos productos por página? "))
    paginas = (total + por_pagina - 1) // por_pagina

    while True:
        pagina = int(input(f"¿Qué página quieres ver? (1-{paginas}) "))
        if pagina < 1 or pagina > paginas:
            print("Página inválida.")
            continue

        inicio = (pagina - 1) * por_pagina
        fin = min(inicio + por_pagina, total)
        print(f"\nMostrando página {pagina}/{paginas}:")

        for i, producto in enumerate(productos[inicio:fin], start=inicio + 1):
            print(
                f"{i}. ID: {producto.id} | Nombre: {producto.nombre} | SKU: {producto.sku} | "
                f"Categoría: {producto.categoria} | Descripción: {producto.descripcion} | "
                f"Stock global: {producto.stock_global}"
            )

        otra = input("¿Ver otra página? (s/n): ").lower()
        if otra != "s":
            break

# Ejemplo de uso:
if __name__ == "__main__":
    from backend.app.domain.models.producto import Producto

    # Lista de ejemplo con objetos Producto
    productos = [
        Producto(id=1, nombre="Producto A", sku="A001", categoria="Cat1", descripcion="Desc A"),
        Producto(id=2, nombre="Producto B", sku="B002", categoria="Cat2", descripcion="Desc B"),
        Producto(id=3, nombre="Producto C", sku="C003", categoria="Cat1", descripcion="Desc C"),
        Producto(id=4, nombre="Producto D", sku="D004", categoria="Cat3", descripcion="Desc D"),
        Producto(id=5, nombre="Producto E", sku="E005", categoria="Cat2", descripcion="Desc E"),
        Producto(id=6, nombre="Producto F", sku="F006", categoria="Cat1", descripcion="Desc F"),
    ]
    paginar_productos(productos)