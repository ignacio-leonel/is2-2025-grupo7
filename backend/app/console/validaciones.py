import re
from backend.app.db.models.producto import ProductoORM

UNIDADES_PERMITIDAS = ["u", "kg", "l", "m", "cm"] 

# Validaciones básicas (no involucran a la base de datos)
def validar_producto(nombre, sku, categoria, descripcion=None, unidad_medida=None):
    """ Valida los campos básicos de un producto. Devuelve una lista de errores (vacía si no hay errores)."""
    errores = []

    # Nombre obligatorio y longitud mínima
    if not nombre or len(nombre) < 3:
        errores.append("Nombre obligatorio (mínimo 3 caracteres)")

    # SKU obligatorio, solo letras, números y guiones
    if not sku:
        errores.append("SKU obligatorio")
    elif not re.match(r'^[A-Za-z0-9-]+$', sku):
        errores.append("SKU solo puede contener letras, números y guiones")

    # Categoría obligatoria y longitud mínima
    if not categoria or len(categoria) < 3:
        errores.append("Categoría obligatoria (mínimo 3 caracteres)")

    # Descripción opcional, longitud máxima
    if descripcion and len(descripcion) > 255:
        errores.append("Descripción demasiado larga (máximo 255 caracteres)")

    # Unidad de medida opcional, solo valores permitidos
    if unidad_medida and unidad_medida not in UNIDADES_PERMITIDAS:
        errores.append(f"Unidad de medida inválida. Valores permitidos: {', '.join(UNIDADES_PERMITIDAS)}")

    return errores

# Validación SKU única en consola (antes de insertar en la BD, que también tiene una restricción de SKU)
def sku_unico(session, sku):
    """Valida si un SKU ya existe en la base de datos. Devuelve True si el SKU no existe (es único), False si ya existe.
    """
    return session.query(ProductoORM).filter_by(sku=sku).first() is None